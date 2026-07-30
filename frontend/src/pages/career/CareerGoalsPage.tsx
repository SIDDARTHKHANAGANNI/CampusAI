import { useState, useEffect } from "react";
import { careerGoalsApi } from "@/api/careerGoals";
import type { CareerGoal } from "@/types";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { careerGoalSchema, type CareerGoalForm } from "@/schemas/forms";
import { Spinner } from "@/components/ui/Spinner";
import { PageHeader } from "@/components/ui/PageHeader";
import { EmptyState } from "@/components/ui/EmptyState";
import Modal from "@/components/ui/Modal";
import { Target, Plus, Pencil, Trash2, Loader2 } from "lucide-react";

export default function CareerGoalsPage() {
  const [goals, setGoals] = useState<CareerGoal[]>([]);
  const [loading, setLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [editing, setEditing] = useState<CareerGoal | null>(null);
  const [deleting, setDeleting] = useState<number | null>(null);
  const [error, setError] = useState("");

  const load = () => {
    careerGoalsApi.getAll().then(setGoals).catch(() => setError("Failed to load")).finally(() => setLoading(false));
  };
  useEffect(load, []);

  const { register, handleSubmit, reset, formState: { errors, isSubmitting } } = useForm<CareerGoalForm>({
    resolver: zodResolver(careerGoalSchema),
  });

  const openAdd = () => { setEditing(null); reset({ target_role: "", target_company_type: "", target_timeline: "" }); setModalOpen(true); };
  const openEdit = (g: CareerGoal) => { setEditing(g); reset({ target_role: g.target_role, target_company_type: g.target_company_type || "", target_timeline: g.target_timeline || "" }); setModalOpen(true); };

  const onSubmit = async (data: CareerGoalForm) => {
    try {
      if (editing) {
        await careerGoalsApi.update(editing.id, data);
      } else {
        await careerGoalsApi.create(data);
      }
      setModalOpen(false);
      load();
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to save");
    }
  };

  const handleDelete = async (id: number) => {
    setDeleting(id);
    try { await careerGoalsApi.remove(id); load(); } catch { setError("Failed to delete"); }
    finally { setDeleting(null); }
  };

  if (loading) return <Spinner />;

  return (
    <div className="space-y-6">
      <PageHeader title="Career Goals" description="Plan your career path" action={
        <button onClick={openAdd} className="bg-violet-500 hover:bg-violet-600 text-white font-medium px-4 py-2 rounded-xl transition-colors flex items-center gap-2 text-sm">
          <Plus size={16} /> Add Goal
        </button>
      } />

      {error && <div className="bg-rose-50 text-rose-600 text-sm font-medium px-4 py-3 rounded-xl">{error}</div>}

      {goals.length === 0 ? (
        <EmptyState icon={Target} title="No career goals yet" description="Define your career goals" action={
          <button onClick={openAdd} className="bg-violet-500 hover:bg-violet-600 text-white font-medium px-4 py-2 rounded-xl transition-colors text-sm">Add Goal</button>
        } />
      ) : (
        <div className="space-y-4">
          {goals.map((g) => (
            <div key={g.id} className="bg-white rounded-2xl border border-stone-200 p-5 flex items-center justify-between">
              <div className="space-y-1">
                <h3 className="font-semibold text-stone-700">{g.target_role}</h3>
                <div className="flex items-center gap-2">
                  {g.target_company_type && <span className="text-xs font-medium text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-lg">{g.target_company_type}</span>}
                  {g.target_timeline && <span className="text-xs text-stone-400">{g.target_timeline}</span>}
                </div>
              </div>
              <div className="flex items-center gap-1">
                <button onClick={() => openEdit(g)} className="text-stone-300 hover:text-violet-500 transition-colors p-1"><Pencil size={14} /></button>
                <button onClick={() => handleDelete(g.id)} disabled={deleting === g.id} className="text-stone-300 hover:text-rose-500 transition-colors p-1"><Trash2 size={14} /></button>
              </div>
            </div>
          ))}
        </div>
      )}

      <Modal open={modalOpen} onClose={() => setModalOpen(false)} title={editing ? "Edit Goal" : "Add Goal"}>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label className="text-sm font-medium text-stone-500 mb-1.5 block">Target Role</label>
            <input type="text" {...register("target_role")} placeholder="e.g. Software Engineer" className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm" />
            {errors.target_role && <p className="text-rose-500 text-xs mt-1">{errors.target_role.message}</p>}
          </div>
          <div>
            <label className="text-sm font-medium text-stone-500 mb-1.5 block">Company Type (optional)</label>
            <input type="text" {...register("target_company_type")} placeholder="e.g. Startup, FAANG, MNC" className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm" />
          </div>
          <div>
            <label className="text-sm font-medium text-stone-500 mb-1.5 block">Timeline (optional)</label>
            <input type="text" {...register("target_timeline")} placeholder="e.g. Within 6 months" className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm" />
          </div>
          <button type="submit" disabled={isSubmitting} className="w-full bg-violet-500 hover:bg-violet-600 disabled:opacity-60 text-white font-medium py-2.5 rounded-xl transition-colors flex items-center justify-center gap-2">
            {isSubmitting && <Loader2 size={16} className="animate-spin" />}
            {isSubmitting ? "Saving..." : editing ? "Update" : "Add Goal"}
          </button>
        </form>
      </Modal>
    </div>
  );
}
