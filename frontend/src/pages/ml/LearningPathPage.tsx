import { PageHeader } from "@/components/ui/PageHeader";
import { Sparkles, Route } from "lucide-react";

export default function LearningPathPage() {
  return (
    <div className="space-y-6">
      <PageHeader title="Learning Path Generator" description="Get a personalized roadmap to your dream role" />

      <div className="bg-[#FFF8E8] border border-[#E8DFC0] rounded-2xl p-5 flex items-start gap-3">
        <Sparkles size={20} className="text-[#8B6914] mt-0.5 shrink-0" />
        <div>
          <p className="text-sm font-semibold text-[#8B6914]">ML Integration Coming Soon</p>
          <p className="text-sm text-[#8B6914] mt-0.5">This feature will analyze your current skills, target role, and industry trends to generate a step-by-step learning roadmap with recommended courses and resources.</p>
        </div>
      </div>

      <div className="bg-white rounded-2xl border border-[#dde0d5] p-6 space-y-4">
        <div className="flex items-center gap-3 p-4 rounded-xl bg-[#F6F7F2]">
          <div className="w-10 h-10 rounded-xl bg-[#E8F5EE] flex items-center justify-center">
            <Route size={20} className="text-[#343A40]" />
          </div>
          <div>
            <p className="text-sm font-semibold text-[#343A40]">How it works</p>
            <p className="text-xs text-[#8d9490]">Based on your existing skills and career goals, we'll generate a personalized learning path with timelines and milestones.</p>
          </div>
        </div>

        <div>
          <label className="text-sm font-medium text-[#6c757d] mb-1.5 block">Target Role</label>
          <input type="text" className="w-full bg-[#F6F7F2] border border-[#dde0d5] rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-[#B7E4C7] focus:border-[#B7E4C7] transition-all text-sm" placeholder="e.g. Full Stack Developer" />
        </div>

        <div>
          <label className="text-sm font-medium text-[#6c757d] mb-1.5 block">Timeline</label>
          <select className="w-full bg-[#F6F7F2] border border-[#dde0d5] rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-[#B7E4C7] focus:border-[#B7E4C7] transition-all text-sm">
            <option value="">Select timeline</option>
            <option value="3">3 months</option>
            <option value="6">6 months</option>
            <option value="12">12 months</option>
          </select>
        </div>

        <button disabled className="w-full bg-[#eef0ea] text-[#8d9490] font-medium py-2.5 rounded-xl cursor-not-allowed">
          Generate Learning Path — Coming Soon
        </button>
      </div>
    </div>
  );
}
