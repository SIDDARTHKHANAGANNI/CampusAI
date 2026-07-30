import { PageHeader } from "@/components/ui/PageHeader";
import { Upload, Sparkles } from "lucide-react";

export default function ResumeMatchPage() {
  return (
    <div className="space-y-6">
      <PageHeader title="Resume Match" description="Match your resume against job descriptions" />

      <div className="bg-amber-50 border border-amber-200 rounded-2xl p-5 flex items-start gap-3">
        <Sparkles size={20} className="text-amber-500 mt-0.5 shrink-0" />
        <div>
          <p className="text-sm font-semibold text-amber-700">ML Integration Coming Soon</p>
          <p className="text-sm text-amber-600 mt-0.5">This feature will compare your resume with a job description and identify skill gaps.</p>
        </div>
      </div>

      <div className="bg-white rounded-2xl border border-stone-200 p-6 space-y-4">
        <div className="border-2 border-dashed border-stone-200 rounded-xl p-10 text-center">
          <Upload size={32} className="text-stone-300 mx-auto mb-3" />
          <p className="text-sm font-medium text-stone-500">Upload your resume (PDF)</p>
          <p className="text-xs text-stone-400 mt-1">Drag & drop or click to browse</p>
        </div>

        <div>
          <label className="text-sm font-medium text-stone-500 mb-1.5 block">Job Description</label>
          <textarea rows={5} className="w-full bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-violet-200 focus:border-violet-400 transition-all text-sm resize-none" placeholder="Paste the complete job description here..." />
        </div>

        <button disabled className="w-full bg-stone-100 text-stone-400 font-medium py-2.5 rounded-xl cursor-not-allowed">
          Calculate Match — Coming Soon
        </button>
      </div>
    </div>
  );
}
