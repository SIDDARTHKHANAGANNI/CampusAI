import { PageHeader } from "@/components/ui/PageHeader";
import { Upload, Sparkles } from "lucide-react";

export default function PlacementReadinessPage() {
  return (
    <div className="space-y-6">
      <PageHeader title="Placement Readiness Prediction" description="Know how prepared you are for placements" />

      <div className="bg-[#FFF8E8] border border-[#E8DFC0] rounded-2xl p-5 flex items-start gap-3">
        <Sparkles size={20} className="text-[#8B6914] mt-0.5 shrink-0" />
        <div>
          <p className="text-sm font-semibold text-[#8B6914]">ML Integration Coming Soon</p>
          <p className="text-sm text-[#8B6914] mt-0.5">This feature will analyze your profile, skills, academics, and resume to predict your placement readiness with a confidence score and improvement suggestions.</p>
        </div>
      </div>

      <div className="bg-white rounded-2xl border border-[#dde0d5] p-6 space-y-4">
        <div>
          <label className="text-sm font-medium text-[#6c757d] mb-1.5 block">Target Role</label>
          <input type="text" className="w-full bg-[#F6F7F2] border border-[#dde0d5] rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-[#B7E4C7] focus:border-[#B7E4C7] transition-all text-sm" placeholder="e.g. Software Engineer at Google" />
        </div>

        <div className="border-2 border-dashed border-[#dde0d5] rounded-xl p-10 text-center">
          <Upload size={32} className="text-[#adb5b0] mx-auto mb-3" />
          <p className="text-sm font-medium text-[#6c757d]">Upload your resume (PDF)</p>
          <p className="text-xs text-[#8d9490] mt-1">Optional — improves prediction accuracy</p>
        </div>

        <button disabled className="w-full bg-[#eef0ea] text-[#8d9490] font-medium py-2.5 rounded-xl cursor-not-allowed">
          Predict Readiness — Coming Soon
        </button>
      </div>
    </div>
  );
}