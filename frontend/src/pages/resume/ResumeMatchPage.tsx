import { PageHeader } from "@/components/ui/PageHeader";
import { Upload, Sparkles } from "lucide-react";

export default function ResumeMatchingPage() {
  return (
    <div className="space-y-6">
      <PageHeader title="Resume–Job Matching" description="See how well your resume matches a job description" />

      <div className="bg-[#FFF8E8] border border-[#E8DFC0] rounded-2xl p-5 flex items-start gap-3">
        <Sparkles size={20} className="text-[#8B6914] mt-0.5 shrink-0" />
        <div>
          <p className="text-sm font-semibold text-[#8B6914]">ML Integration Coming Soon</p>
          <p className="text-sm text-[#8B6914] mt-0.5">This feature will compare your resume against a job description, calculate a match score, and identify missing skills and keywords.</p>
        </div>
      </div>

      <div className="bg-white rounded-2xl border border-[#dde0d5] p-6 space-y-4">
        <div className="border-2 border-dashed border-[#dde0d5] rounded-xl p-10 text-center">
          <Upload size={32} className="text-[#adb5b0] mx-auto mb-3" />
          <p className="text-sm font-medium text-[#6c757d]">Upload your resume (PDF)</p>
          <p className="text-xs text-[#8d9490] mt-1">Drag & drop or click to browse</p>
        </div>

        <div>
          <label className="text-sm font-medium text-[#6c757d] mb-1.5 block">Job Description</label>
          <textarea rows={5} className="w-full bg-[#F6F7F2] border border-[#dde0d5] rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-[#B7E4C7] focus:border-[#B7E4C7] transition-all text-sm resize-none" placeholder="Paste the complete job description here..." />
        </div>

        <button disabled className="w-full bg-[#eef0ea] text-[#8d9490] font-medium py-2.5 rounded-xl cursor-not-allowed">
          Calculate Match — Coming Soon
        </button>
      </div>
    </div>
  );
}