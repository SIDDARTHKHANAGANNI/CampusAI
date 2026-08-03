import { PageHeader } from "@/components/ui/PageHeader";
import { Sparkles, Compass } from "lucide-react";

export default function CareerRecommendationPage() {
  return (
    <div className="space-y-6">
      <PageHeader title="Career Recommendation" description="Discover career paths that match your profile" />

      <div className="bg-[#FFF8E8] border border-[#E8DFC0] rounded-2xl p-5 flex items-start gap-3">
        <Sparkles size={20} className="text-[#8B6914] mt-0.5 shrink-0" />
        <div>
          <p className="text-sm font-semibold text-[#8B6914]">ML Integration Coming Soon</p>
          <p className="text-sm text-[#8B6914] mt-0.5">This feature will analyze your skills, academics, projects, and interests to recommend the best career paths with match percentages and required skill gaps.</p>
        </div>
      </div>

      <div className="bg-white rounded-2xl border border-[#dde0d5] p-6 space-y-5">
        <div className="flex items-center gap-3 p-4 rounded-xl bg-[#F6F7F2]">
          <div className="w-10 h-10 rounded-xl bg-[#E8F5EE] flex items-center justify-center">
            <Compass size={20} className="text-[#343A40]" />
          </div>
          <div>
            <p className="text-sm font-semibold text-[#343A40]">How it works</p>
            <p className="text-xs text-[#8d9490]">We'll match your complete profile against industry roles and suggest top career paths ranked by compatibility.</p>
          </div>
        </div>

        <div>
          <label className="text-sm font-medium text-[#6c757d] mb-1.5 block">Interests (optional)</label>
          <input type="text" className="w-full bg-[#F6F7F2] border border-[#dde0d5] rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-[#B7E4C7] focus:border-[#B7E4C7] transition-all text-sm" placeholder="e.g. AI, Web Development, Cloud" />
        </div>

        <div>
          <label className="text-sm font-medium text-[#6c757d] mb-1.5 block">Preferred Company Type</label>
          <select className="w-full bg-[#F6F7F2] border border-[#dde0d5] rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-[#B7E4C7] focus:border-[#B7E4C7] transition-all text-sm">
            <option value="">Any</option>
            <option value="startup">Startup</option>
            <option value="mnc">MNC</option>
            <option value="faang">FAANG</option>
            <option value="product">Product Company</option>
            <option value="service">Service Company</option>
          </select>
        </div>

        <button disabled className="w-full bg-[#eef0ea] text-[#8d9490] font-medium py-2.5 rounded-xl cursor-not-allowed">
          Get Recommendations — Coming Soon
        </button>
      </div>
    </div>
  );
}
