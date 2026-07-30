import { useState, useEffect } from "react";
import { projectsApi } from "@/api/projects";
import type { Project } from "@/types";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { projectSchema, type ProjectForm } from "@/schemas/forms";
import { Spinner } from "@/components/ui/Spinner";
import { PageHeader } from "@/components/ui/PageHeader";
import { EmptyState } from "@/components/ui/EmptyState";
import Modal from "@/components/ui/Modal";
import { FolderGit2, Plus, Pencil, Trash2, ExternalLink, Loader2 } from "lucide-react";

export default function ProjectsPage() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [editing, setEditing] = useState<Project | null>(null);
  const [deleting, setDeleting] = useState<number | null>(null);
  const [error, setError] = useState("");

  const load = () => {
    projectsApi.getAll().then(setProjects).catch(() => setError("Failed to load projects")).finally(() => setLoading(false));
  };
  useEffect(load, []);

  const { register, handleSubmit, reset, formState: { errors, isSubmitting } } = useForm<ProjectForm>({
    resolver: zodResolver(projectSchema),
  });

  const openAdd = () => { setEditing(null); reset({ title: "", description: "", technologies: "", github_url: "" }); setModalOpen(true); };
  const openEdit = (p: Project) => { setEditing(p); reset({ title: p.title, description: p.description || "", technologies: p.technologies || "", github_url: p.github_url || "" }); setModalOpen(true); };

  const onSubmit = async (data: ProjectForm) => {
    try {
      const payload = { ...data, github_url: data.github_url || null };
      if (editing) {
        await projectsApi.update(editing.id, payload);
      } else {
        await projectsApi.create(payload);
      }
      setModalOpen(false);
      load();
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to save project");
    }
  };

  const handleDelete = async (id: number) => {
    setDeleting(id);
    try {
      await projectsApi.remove(id);
      load();
    } catch { setError("Failed to delete"); }
    finally { setDeleting(null); }
  };

  if (loading) return <Spinner />;

  return (
    <div className="space-y-6">
      <PageHeader title="Projects" description="Showcase your work" action={
        <button onClick={openAdd} className="bg-violet-500 hover:bg-violet-600 text-white font-medium px-4 py-2 rounded-xl transition-colors flex items-center gap-2 text-sm">
          <Plus size={16} /> Add Project
        </button>
      } />

      {error && <div className="bg-rose-50 text-rose-600 text-sm font-medium px-4 py-3 rounded-xl">{error}</div>}

      {projects.length === 0 ? (
        <EmptyState icon={FolderGit2} title="No projects yet" description="Add your first project" action={
          <button onClick={openAdd} className="bg-violet-500 hover:bg-violet-600 text-white font-medium px-4 py-2 rounded-xl transition-colors text-sm">Add Project</button>
        } />
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {projects.map((p) => (
            <div key={p.id} className="bg-white rounded-2xl border border-stone-200 p-5 space-y-3">
              <div className="flex items-start justify-between">
                <h3 className="font-semibold text-stone-700">{p.title}</h3>
                <div className="flex items-center gap-1">
                  <button onClick={() => openEdit(p)} className="text-stone-300 hover:text-violet-500 transition-colors p-1"><Pencil size={14} /></button>
                  <button onClick={() => handleDelete(p.id)} disabled={deleting === p.id} className="text-stone-300 hover:text-rose-500 transition-colors p-1"><Trash2 size={14} /></button>
                </div>
              </div>
              {p.description && <p className="text-sm text-stone-400">{p.description}</p>}
              {p.technologies && (
                <div className="flex flex-wrap gap-1.5">
                  {p.technologies.split(",").map((t, i) => (
                    <span key={i} className="text-xs font-medium text-sky-600 bg-sky-50 px-2 py-0.5 rounded-lg">{t.trim()}</span>
                  ))}
                </div>
              )}
              {p.github_url && (
                <a href={p.github_url} target="_blank" rel="noreferrer" className="text-xs text-violet-500 hover:text-violet-600 flex items-center gap-1">
                  <ExternalLink size={12} /> GitHub
                </a>
              )}
            </div>
          ))}
        </div>
      )}

      <Modal open={modalOpen} onClose={() => setModalOpen(false)} title={editing ? "Edit Project" : "Add Project"}>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label className="text-sm font-medium text-stone-500 mb-1.5 block">Title</label>
            <input type="text" {...register("title")} className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm" />
            {errors.title && <p className="text-rose-500 text-xs mt-1">{errors.title.message}</p>}
          </div>
          <div>
            <label className="text-sm font-medium text-stone-500 mb-1.5 block">Description</label>
            <textarea {...register("description")} rows={3} className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm resize-none" />
          </div>
          <div>
            <label className="text-sm font-medium text-stone-500 mb-1.5 block">Technologies (comma-separated)</label>
            <input type="text" {...register("technologies")} placeholder="React, Python, FastAPI" className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm" />
          </div>
          <div>
            <label className="text-sm font-medium text-stone-500 mb-1.5 block">GitHub URL</label>
            <input type="text" {...register("github_url")} placeholder="https://github.com/..." className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm" />
            {errors.github_url && <p className="text-rose-500 text-xs mt-1">{errors.github_url.message}</p>}
          </div>
          <button type="submit" disabled={isSubmitting} className="w-full bg-violet-500 hover:bg-violet-600 disabled:opacity-60 text-white font-medium py-2.5 rounded-xl transition-colors flex items-center justify-center gap-2">
            {isSubmitting && <Loader2 size={16} className="animate-spin" />}
            {isSubmitting ? "Saving..." : editing ? "Update" : "Add Project"}
          </button>
        </form>
      </Modal>
    </div>
  );
}
