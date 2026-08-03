import { PageHeader } from "@/components/ui/PageHeader";
import { Sparkles, AlertTriangle } from "lucide-react";

export default function AcademicRiskPage() {
  return (
    <div className="space-y-6">
      <PageHeader title="Academic Risk Prediction" description="Identify potential academic risks early" />

      <div className="bg-[#FFF8E8] border border-[#E8DFC0] rounded-2xl p-5 flex items-start gap-3">
        <Sparkles size={20} className="text-[#8B6914] mt-0.5 shrink-0" />
        <div>
          <p className="text-sm font-semibold text-[#8B6914]">ML Integration Coming Soon</p>
          <p className="text-sm text-[#8B6914] mt-0.5">This feature will analyze your academic history, attendance patterns, and backlog trends to predict potential risks and suggest preventive actions.</p>
        </div>
      </div>

      <div className="bg-white rounded-2xl border border-[#dde0d5] p-6 space-y-5">
        <div className="flex items-center gap-3 p-4 rounded-xl bg-[#F6F7F2]">
          <div className="w-10 h-10 rounded-xl bg-[#E8F5EE] flex items-center justify-center">
            <AlertTriangle size={20} className="text-[#343A40]" />
          </div>
          <div>
            <p className="text-sm font-semibold text-[#343A40]">How it works</p>
            <p className="text-xs text-[#8d9490]">We'll use your semester GPA trends, attendance, and backlogs to generate a risk assessment with actionable recommendations.</p>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div className="rounded-xl border border-[#dde0d5] p-4 text-center">
            <p className="text-2xl font-bold text-[#343A40]">—</p>
            <p className="text-xs text-[#8d9490] mt-1">Risk Score</p>
          </div>
          <div className="rounded-xl border border-[#dde0d5] p-4 text-center">
            <p className="text-2xl font-bold text-[#343A40]">—</p>
            <p className="text-xs text-[#8d9490] mt-1">Risk Level</p>
          </div>
          <div className="rounded-xl border border-[#dde0d5] p-4 text-center">
            <p className="text-2xl font-bold text-[#343A40]">—</p>
            <p className="text-xs text-[#8d9490] mt-1">Trend</p>
          </div>
        </div>

        <button disabled className="w-full bg-[#eef0ea] text-[#8d9490] font-medium py-2.5 rounded-xl cursor-not-allowed">
          Predict Academic Risk — Coming Soon
        </button>
      </div>
    </div>
  );
}
