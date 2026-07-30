import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { studentSchema, type StudentForm } from "@/schemas/forms";
import { studentApi } from "@/api/student";
import { useAuth } from "@/contexts/AuthContext";
import { Loader2 } from "lucide-react";

export default function CreateProfilePage() {
  const navigate = useNavigate();
  const { user } = useAuth();
  const [error, setError] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<StudentForm>({
    resolver: zodResolver(studentSchema),
    defaultValues: {
      name: user?.name || "",
      email: user?.email || "",
      current_year: 1,
      graduation_year: 2027,
      cgpa: 0,
      backlogs: 0,
    },
  });

  const onSubmit = async (data: StudentForm) => {
    setError("");
    try {
      await studentApi.createProfile(data);
      navigate("/dashboard");
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to create profile.");
    }
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6">
      <div>
        <h1 className="text-2xl font-semibold text-slate-900">Create Your Profile</h1>
        <p className="text-slate-500 text-sm mt-1">Fill in your details to get started</p>
      </div>

      {error && (
        <div className="bg-red-50 text-red-700 text-sm font-medium px-4 py-3 rounded-xl">{error}</div>
      )}

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-4">
          <h2 className="text-sm font-semibold text-slate-500 uppercase tracking-wider">Personal</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <Field label="Full Name" error={errors.name?.message}>
              <input type="text" {...register("name")} className="input-field" />
            </Field>
            <Field label="Email" error={errors.email?.message}>
              <input type="email" {...register("email")} className="input-field" />
            </Field>
            <Field label="College" error={errors.college?.message} full>
              <input type="text" {...register("college")} placeholder="Your university" className="input-field" />
            </Field>
          </div>
        </div>

        <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-4">
          <h2 className="text-sm font-semibold text-slate-500 uppercase tracking-wider">Academic</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <Field label="Degree" error={errors.degree?.message}>
              <input type="text" {...register("degree")} placeholder="e.g. B.Tech" className="input-field" />
            </Field>
            <Field label="Branch" error={errors.branch?.message}>
              <input type="text" {...register("branch")} placeholder="e.g. Computer Science" className="input-field" />
            </Field>
            <Field label="Current Year" error={errors.current_year?.message}>
              <input type="number" {...register("current_year")} min={1} max={6} className="input-field" />
            </Field>
            <Field label="Graduation Year" error={errors.graduation_year?.message}>
              <input type="number" {...register("graduation_year")} min={2020} max={2040} className="input-field" />
            </Field>
            <Field label="CGPA" error={errors.cgpa?.message}>
              <input type="number" step="0.01" {...register("cgpa")} min={0} max={10} className="input-field" />
            </Field>
            <Field label="Attendance %" error={errors.attendance?.message}>
              <input type="number" step="0.1" {...register("attendance")} min={0} max={100} className="input-field" placeholder="Optional" />
            </Field>
            <Field label="Backlogs" error={errors.backlogs?.message}>
              <input type="number" {...register("backlogs")} min={0} className="input-field" />
            </Field>
          </div>
        </div>

        <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-4">
          <h2 className="text-sm font-semibold text-slate-500 uppercase tracking-wider">Career</h2>
          <Field label="Target Role" error={errors.target_role?.message}>
            <input type="text" {...register("target_role")} placeholder="e.g. Software Engineer" className="input-field" />
          </Field>
        </div>

        <button
          type="submit"
          disabled={isSubmitting}
          className="w-full bg-slate-900 hover:bg-slate-800 disabled:opacity-60 text-white font-medium py-2.5 rounded-xl transition-colors flex items-center justify-center gap-2"
        >
          {isSubmitting && <Loader2 size={16} className="animate-spin" />}
          {isSubmitting ? "Creating..." : "Create Profile"}
        </button>
      </form>

      <style>{`.input-field { width: 100%; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 0.75rem; padding: 0.625rem 1rem; outline: none; font-size: 0.875rem; transition: all 0.15s; } .input-field:focus { box-shadow: 0 0 0 2px #e2e8f0; border-color: #94a3b8; }`}</style>
    </div>
  );
}

function Field({ label, error, full, children }: { label: string; error?: string; full?: boolean; children: React.ReactNode }) {
  return (
    <div className={full ? "sm:col-span-2" : ""}>
      <label className="text-sm font-medium text-slate-600 mb-1.5 block">{label}</label>
      {children}
      {error && <p className="text-red-600 text-xs mt-1">{error}</p>}
    </div>
  );
}