import { useState, useEffect } from "react";
import { skillsApi } from "@/api/skills";
import type { Skill } from "@/types";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { skillSchema, type SkillForm } from "@/schemas/forms";
import { Spinner } from "@/components/ui/Spinner";
import { PageHeader } from "@/components/ui/PageHeader";
import { EmptyState } from "@/components/ui/EmptyState";
import Modal from "@/components/ui/Modal";
import { Code2, Plus, Pencil, Loader2 } from "lucide-react";

const proficiencyLevels = ["Beginner", "Intermediate", "Advanced", "Expert"];

export default function SkillsPage() {
  const [skills, setSkills] = useState<Skill[]>([]);
  const [loading, setLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [editing, setEditing] = useState<Skill | null>(null);
  const [error, setError] = useState("");

  const load = () => {
    skillsApi.getAll().then(setSkills).catch(() => setError("Failed to load skills")).finally(() => setLoading(false));
  };

  useEffect(load, []);

  const { register, handleSubmit, reset, formState: { errors, isSubmitting } } = useForm<SkillForm>({
    resolver: zodResolver(skillSchema),
  });

  const openAdd = () => { setEditing(null); reset({ name: "", category: "", proficiency: "Intermediate" }); setModalOpen(true); };
  const openEdit = (s: Skill) => { setEditing(s); reset({ name: s.name, category: s.category || "", proficiency: s.proficiency }); setModalOpen(true); };

  const onSubmit = async (data: SkillForm) => {
    try {
      if (editing) {
        await skillsApi.update(editing.id, data);
      } else {
        await skillsApi.create(data);
      }
      setModalOpen(false);
      load();
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to save skill");
    }
  };

  if (loading) return <Spinner />;

  return (
    <div className="space-y-6">
      <PageHeader title="Skills" description="Manage your technical skills" action={
        <button onClick={openAdd} className="bg-violet-500 hover:bg-violet-600 text-white font-medium px-4 py-2 rounded-xl transition-colors flex items-center gap-2 text-sm">
          <Plus size={16} /> Add Skill
        </button>
      } />

      {error && <div className="bg-rose-50 text-rose-600 text-sm font-medium px-4 py-3 rounded-xl">{error}</div>}

      {skills.length === 0 ? (
        <EmptyState icon={Code2} title="No skills yet" description="Add your first skill to get started" action={
          <button onClick={openAdd} className="bg-violet-500 hover:bg-violet-600 text-white font-medium px-4 py-2 rounded-xl transition-colors text-sm">Add Skill</button>
        } />
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {skills.map((s) => (
            <div key={s.id} className="bg-white rounded-2xl border border-stone-200 p-5 flex flex-col gap-3">
              <div className="flex items-start justify-between">
                <div>
                  <h3 className="font-semibold text-stone-700 text-sm">{s.name}</h3>
                  {s.category && <span className="text-xs font-medium text-violet-500 bg-violet-50 px-2 py-0.5 rounded-lg mt-1 inline-block">{s.category}</span>}
                </div>
                <button onClick={() => openEdit(s)} className="text-stone-300 hover:text-violet-500 transition-colors"><Pencil size={14} /></button>
              </div>
              <span className="text-xs font-medium text-stone-400 bg-stone-50 px-2.5 py-1 rounded-lg self-start">{s.proficiency}</span>
            </div>
          ))}
        </div>
      )}

      <Modal open={modalOpen} onClose={() => setModalOpen(false)} title={editing ? "Edit Skill" : "Add Skill"}>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label className="text-sm font-medium text-stone-500 mb-1.5 block">Skill Name</label>
            <input type="text" {...register("name")} className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm" />
            {errors.name && <p className="text-rose-500 text-xs mt-1">{errors.name.message}</p>}
          </div>
          <div>
            <label className="text-sm font-medium text-stone-500 mb-1.5 block">Category (optional)</label>
            <input type="text" {...register("category")} placeholder="e.g. Frontend, Backend" className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm" />
          </div>
          <div>
            <label className="text-sm font-medium text-stone-500 mb-1.5 block">Proficiency</label>
            <select {...register("proficiency")} className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm">
              {proficiencyLevels.map((l) => <option key={l} value={l}>{l}</option>)}
            </select>
            {errors.proficiency && <p className="text-rose-500 text-xs mt-1">{errors.proficiency.message}</p>}
          </div>
          <button type="submit" disabled={isSubmitting} className="w-full bg-violet-500 hover:bg-violet-600 disabled:opacity-60 text-white font-medium py-2.5 rounded-xl transition-colors flex items-center justify-center gap-2">
            {isSubmitting && <Loader2 size={16} className="animate-spin" />}
            {isSubmitting ? "Saving..." : editing ? "Update Skill" : "Add Skill"}
          </button>
        </form>
      </Modal>
    </div>
  );
}
