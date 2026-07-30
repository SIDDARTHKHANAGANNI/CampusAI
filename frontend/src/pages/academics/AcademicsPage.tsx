import { useState, useEffect } from "react";
import { academicsApi } from "@/api/academics";
import type { AcademicRecord } from "@/types";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { academicSchema, type AcademicForm } from "@/schemas/forms";
import { Spinner } from "@/components/ui/Spinner";
import { PageHeader } from "@/components/ui/PageHeader";
import { EmptyState } from "@/components/ui/EmptyState";
import Modal from "@/components/ui/Modal";
import { GraduationCap, Plus, Pencil, Trash2, Loader2 } from "lucide-react";

export default function AcademicsPage() {
  const [records, setRecords] = useState<AcademicRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [editing, setEditing] = useState<AcademicRecord | null>(null);
  const [deleting, setDeleting] = useState<number | null>(null);
  const [error, setError] = useState("");

  const load = () => {
    academicsApi.getAll().then((data) => setRecords(data.sort((a, b) => a.semester - b.semester))).catch(() => setError("Failed to load")).finally(() => setLoading(false));
  };
  useEffect(load, []);

  const { register, handleSubmit, reset, formState: { errors, isSubmitting } } = useForm<AcademicForm>({
    resolver: zodResolver(academicSchema),
  });

  const openAdd = () => { setEditing(null); reset({ semester: (records.length + 1), semester_gpa: 0, attendance: undefined, backlogs: 0 }); setModalOpen(true); };
  const openEdit = (r: AcademicRecord) => { setEditing(r); reset({ semester: r.semester, semester_gpa: r.semester_gpa, attendance: r.attendance, backlogs: r.backlogs }); setModalOpen(true); };

  const onSubmit = async (data: AcademicForm) => {
    try {
      if (editing) {
        await academicsApi.update(editing.id, data);
      } else {
        await academicsApi.create(data);
      }
      setModalOpen(false);
      load();
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to save");
    }
  };

  const handleDelete = async (id: number) => {
    setDeleting(id);
    try { await academicsApi.remove(id); load(); } catch { setError("Failed to delete"); }
    finally { setDeleting(null); }
  };

  if (loading) return <Spinner />;

  return (
    <div className="space-y-6">
      <PageHeader title="Academic Records" description="Track your semester-wise performance" action={
        <button onClick={openAdd} className="bg-slate-900 hover:bg-slate-800 text-white font-medium px-4 py-2 rounded-xl transition-colors flex items-center gap-2 text-sm">
          <Plus size={16} /> Add Semester
        </button>
      } />

      {error && <div className="bg-red-50 text-red-700 text-sm font-medium px-4 py-3 rounded-xl">{error}</div>}

      {records.length === 0 ? (
        <EmptyState icon={GraduationCap} title="No records yet" description="Add your first semester record" action={
          <button onClick={openAdd} className="bg-slate-900 hover:bg-slate-800 text-white font-medium px-4 py-2 rounded-xl transition-colors text-sm">Add Semester</button>
        } />
      ) : (
        <div className="bg-white rounded-2xl border border-slate-200 overflow-hidden">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-slate-200">
                <th className="text-left px-5 py-3 font-medium text-slate-500">Semester</th>
                <th className="text-left px-5 py-3 font-medium text-slate-500">GPA</th>
                <th className="text-left px-5 py-3 font-medium text-slate-500">Attendance</th>
                <th className="text-left px-5 py-3 font-medium text-slate-500">Backlogs</th>
                <th className="text-right px-5 py-3 font-medium text-slate-500">Actions</th>
              </tr>
            </thead>
            <tbody>
              {records.map((r) => (
                <tr key={r.id} className="border-b border-slate-100 last:border-0 hover:bg-slate-50 transition-colors">
                  <td className="px-5 py-3.5 font-semibold text-slate-900">Sem {r.semester}</td>
                  <td className="px-5 py-3.5">
                    <span className={`font-semibold ${r.semester_gpa >= 7 ? "text-emerald-600" : r.semester_gpa >= 5 ? "text-amber-600" : "text-red-600"}`}>
                      {r.semester_gpa.toFixed(2)}
                    </span>
                  </td>
                  <td className="px-5 py-3.5 text-slate-600">{r.attendance != null ? `${r.attendance}%` : "—"}</td>
                  <td className="px-5 py-3.5">
                    <span className={`text-xs font-medium px-2 py-0.5 rounded-lg ${r.backlogs > 0 ? "bg-red-50 text-red-700" : "bg-emerald-50 text-emerald-700"}`}>
                      {r.backlogs}
                    </span>
                  </td>
                  <td className="px-5 py-3.5 text-right">
                    <button onClick={() => openEdit(r)} className="text-slate-400 hover:text-slate-900 transition-colors p-1"><Pencil size={14} /></button>
                    <button onClick={() => handleDelete(r.id)} disabled={deleting === r.id} className="text-slate-400 hover:text-red-600 transition-colors p-1 ml-1"><Trash2 size={14} /></button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <Modal open={modalOpen} onClose={() => setModalOpen(false)} title={editing ? "Edit Semester" : "Add Semester"}>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label className="text-sm font-medium text-slate-600 mb-1.5 block">Semester</label>
            <input type="number" {...register("semester")} min={1} max={12} className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-slate-300 focus:border-slate-400 transition-all text-sm" />
            {errors.semester && <p className="text-red-600 text-xs mt-1">{errors.semester.message}</p>}
          </div>
          <div>
            <label className="text-sm font-medium text-slate-600 mb-1.5 block">Semester GPA (0-10)</label>
            <input type="number" step="0.01" {...register("semester_gpa")} min={0} max={10} className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-slate-300 focus:border-slate-400 transition-all text-sm" />
            {errors.semester_gpa && <p className="text-red-600 text-xs mt-1">{errors.semester_gpa.message}</p>}
          </div>
          <div>
            <label className="text-sm font-medium text-slate-600 mb-1.5 block">Attendance %</label>
            <input type="number" step="0.1" {...register("attendance")} min={0} max={100} className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-slate-300 focus:border-slate-400 transition-all text-sm" placeholder="Optional" />
          </div>
          <div>
            <label className="text-sm font-medium text-slate-600 mb-1.5 block">Backlogs</label>
            <input type="number" {...register("backlogs")} min={0} className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-slate-300 focus:border-slate-400 transition-all text-sm" />
            {errors.backlogs && <p className="text-red-600 text-xs mt-1">{errors.backlogs.message}</p>}
          </div>
          <button type="submit" disabled={isSubmitting} className="w-full bg-slate-900 hover:bg-slate-800 disabled:opacity-60 text-white font-medium py-2.5 rounded-xl transition-colors flex items-center justify-center gap-2">
            {isSubmitting && <Loader2 size={16} className="animate-spin" />}
            {isSubmitting ? "Saving..." : editing ? "Update" : "Add Semester"}
          </button>
        </form>
      </Modal>
    </div>
  );
}