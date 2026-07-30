import { PageHeader } from "@/components/ui/PageHeader";
import { Upload, Sparkles } from "lucide-react";

export default function TargetRolePage() {
  return (
    <div className="space-y-6">
      <PageHeader title="Target Role Readiness" description="Evaluate how ready you are for your dream role" />

      <div className="bg-amber-50 border border-amber-200 rounded-2xl p-5 flex items-start gap-3">
        <Sparkles size={20} className="text-amber-600 mt-0.5 shrink-0" />
        <div>
          <p className="text-sm font-semibold text-amber-800">ML Integration Coming Soon</p>
          <p className="text-sm text-amber-700 mt-0.5">This feature will analyze your profile and resume to calculate readiness for your target role.</p>
        </div>
      </div>

      <div className="bg-white rounded-2xl border border-slate-200 p-6 space-y-4">
        <div>
          <label className="text-sm font-medium text-slate-600 mb-1.5 block">Target Role</label>
          <input type="text" className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-slate-300 focus:border-slate-400 transition-all text-sm" placeholder="e.g. Software Engineer at Google" />
        </div>

        <div className="border-2 border-dashed border-slate-200 rounded-xl p-10 text-center">
          <Upload size={32} className="text-slate-400 mx-auto mb-3" />
          <p className="text-sm font-medium text-slate-600">Upload your resume (PDF)</p>
          <p className="text-xs text-slate-500 mt-1">Drag & drop or click to browse</p>
        </div>

        <button disabled className="w-full bg-slate-100 text-slate-400 font-medium py-2.5 rounded-xl cursor-not-allowed">
          Analyze Readiness — Coming Soon
        </button>
      </div>
    </div>
  );
}