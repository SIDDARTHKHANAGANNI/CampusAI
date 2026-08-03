import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "@/contexts/AuthContext";
import { studentApi } from "@/api/student";
import type { StudentProfile } from "@/types";
import { Spinner } from "@/components/ui/Spinner";
import {
  TrendingUp, BarChart3, AlertTriangle, Calendar,
  Code2, FolderGit2, GraduationCap, Target, FileText, Compass,
  ArrowRight, UserPlus, Briefcase, Route, Sparkles,
} from "lucide-react";

const quickLinks = [
  { to: "/skills", icon: Code2, label: "Skills", desc: "Manage your tech skills", color: "bg-slate-100 text-slate-900" },
  { to: "/projects", icon: FolderGit2, label: "Projects", desc: "Showcase your work", color: "bg-slate-100 text-slate-900" },
  { to: "/academics", icon: GraduationCap, label: "Academics", desc: "Track semester records", color: "bg-slate-100 text-slate-900" },
  { to: "/career-goals", icon: Target, label: "Career Goals", desc: "Plan your future", color: "bg-slate-100 text-slate-900" },
];

const mlLinks = [
  { to: "/resume-analysis", icon: FileText, label: "Resume Analysis", desc: "AI-powered resume feedback", color: "bg-[#E8F5EE] text-[#343A40]" },
  { to: "/resume-matching", icon: Briefcase, label: "Resume–Job Matching", desc: "Match resume to job descriptions", color: "bg-[#E8F5EE] text-[#343A40]" },
  { to: "/placement-readiness", icon: Compass, label: "Placement Readiness", desc: "Predict placement preparedness", color: "bg-[#E8F5EE] text-[#343A40]" },
  { to: "/academic-risk", icon: AlertTriangle, label: "Academic Risk", desc: "Early risk detection", color: "bg-[#E8F5EE] text-[#343A40]" },
  { to: "/learning-path", icon: Route, label: "Learning Path", desc: "Personalized skill roadmap", color: "bg-[#E8F5EE] text-[#343A40]" },
  { to: "/career-recommendation", icon: Sparkles, label: "Career Recommendation", desc: "Discover ideal career paths", color: "bg-[#E8F5EE] text-[#343A40]" },
];

export default function DashboardPage() {
  const { user } = useAuth();
  const [profile, setProfile] = useState<StudentProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const [noProfile, setNoProfile] = useState(false);

  useEffect(() => {
    studentApi
      .getProfile()
      .then(setProfile)
      .catch((err) => {
        if (err.response?.status === 404) setNoProfile(true);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Spinner />;

  if (noProfile) {
    return (
      <div className="flex flex-col items-center justify-center py-20 text-center">
        <div className="w-16 h-16 rounded-2xl bg-slate-100 flex items-center justify-center mb-6">
          <UserPlus size={28} className="text-slate-900" />
        </div>
        <h2 className="text-2xl font-semibold text-slate-900 mb-2">Welcome to CampusAI!</h2>
        <p className="text-slate-500 mb-6 max-w-md">
          Set up your student profile to unlock all features — skill tracking, academic analytics, resume scoring, and more.
        </p>
        <Link
          to="/profile/create"
          className="bg-slate-900 hover:bg-slate-800 text-white font-medium px-6 py-2.5 rounded-xl transition-colors"
        >
          Create Your Profile
        </Link>
      </div>
    );
  }

  const stats = [
    { label: "CGPA", value: profile?.cgpa?.toFixed(2) ?? "—", icon: TrendingUp },
    { label: "Attendance", value: profile?.attendance != null ? `${profile.attendance}%` : "—", icon: BarChart3 },
    { label: "Backlogs", value: profile?.backlogs ?? 0, icon: AlertTriangle },
    { label: "Year", value: profile?.current_year ?? "—", icon: Calendar },
  ];

  return (
    <div className="space-y-8">
      {/* Welcome */}
      <div>
        <h1 className="text-2xl font-semibold text-slate-900">
          Welcome back, {user?.name?.split(" ")[0]} 👋
        </h1>
        <p className="text-slate-500 text-sm mt-1">{profile?.college}</p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((s) => (
          <div key={s.label} className="bg-white rounded-2xl border border-slate-200 p-5">
            <div className="w-9 h-9 rounded-xl bg-slate-100 text-slate-900 flex items-center justify-center mb-3">
              <s.icon size={18} />
            </div>
            <p className="text-2xl font-bold text-slate-900">{s.value}</p>
            <p className="text-xs font-medium text-slate-500 mt-0.5">{s.label}</p>
          </div>
        ))}
      </div>

      {/* Quick Links */}
      <div>
        <h2 className="text-lg font-semibold text-slate-900 mb-4">Quick Access</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {quickLinks.map((l) => (
            <Link
              key={l.to}
              to={l.to}
              className="bg-white rounded-2xl border border-slate-200 p-5 hover:border-slate-400 transition-colors group"
            >
              <div className={`w-10 h-10 rounded-xl ${l.color} flex items-center justify-center mb-3`}>
                <l.icon size={20} />
              </div>
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="font-semibold text-slate-900 text-sm">{l.label}</h3>
                  <p className="text-xs text-slate-500 mt-0.5">{l.desc}</p>
                </div>
                <ArrowRight size={16} className="text-slate-400 group-hover:text-slate-900 transition-colors" />
              </div>
            </Link>
          ))}
        </div>
      </div>

      {/* AI Features */}
      <div>
        <h2 className="text-lg font-semibold text-slate-900 mb-1">AI Features</h2>
        <p className="text-sm text-slate-500 mb-4">ML-powered tools to boost your career readiness</p>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {mlLinks.map((l) => (
            <Link
              key={l.to}
              to={l.to}
              className="bg-white rounded-2xl border border-[#B7E4C7]/40 p-5 hover:border-[#B7E4C7] transition-colors group"
            >
              <div className={`w-10 h-10 rounded-xl ${l.color} flex items-center justify-center mb-3`}>
                <l.icon size={20} />
              </div>
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="font-semibold text-slate-900 text-sm">{l.label}</h3>
                  <p className="text-xs text-slate-500 mt-0.5">{l.desc}</p>
                </div>
                <ArrowRight size={16} className="text-[#B7E4C7] group-hover:text-[#343A40] transition-colors" />
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}