import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "@/contexts/AuthContext";
import { studentApi } from "@/api/student";
import type { StudentProfile } from "@/types";
import { Spinner } from "@/components/ui/Spinner";
import {
  TrendingUp, BarChart3, AlertTriangle, Calendar,
  Code2, FolderGit2, GraduationCap, Target, FileText, Compass,
  ArrowRight, UserPlus,
} from "lucide-react";

const quickLinks = [
  { to: "/skills", icon: Code2, label: "Skills", desc: "Manage your tech skills", color: "bg-violet-50 text-violet-500" },
  { to: "/projects", icon: FolderGit2, label: "Projects", desc: "Showcase your work", color: "bg-sky-50 text-sky-500" },
  { to: "/academics", icon: GraduationCap, label: "Academics", desc: "Track semester records", color: "bg-amber-50 text-amber-500" },
  { to: "/career-goals", icon: Target, label: "Career Goals", desc: "Plan your future", color: "bg-emerald-50 text-emerald-500" },
  { to: "/resume-score", icon: FileText, label: "Resume Score", desc: "ATS compatibility check", color: "bg-rose-50 text-rose-500" },
  { to: "/target-role", icon: Compass, label: "Target Role", desc: "Readiness analysis", color: "bg-indigo-50 text-indigo-500" },
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
        <div className="w-16 h-16 rounded-2xl bg-violet-50 flex items-center justify-center mb-6">
          <UserPlus size={28} className="text-violet-500" />
        </div>
        <h2 className="text-2xl font-semibold text-stone-800 mb-2">Welcome to CampusAI!</h2>
        <p className="text-stone-400 mb-6 max-w-md">
          Set up your student profile to unlock all features — skill tracking, academic analytics, resume scoring, and more.
        </p>
        <Link
          to="/profile/create"
          className="bg-violet-500 hover:bg-violet-600 text-white font-medium px-6 py-2.5 rounded-xl transition-colors"
        >
          Create Your Profile
        </Link>
      </div>
    );
  }

  const stats = [
    { label: "CGPA", value: profile?.cgpa?.toFixed(2) ?? "—", icon: TrendingUp, color: "bg-violet-50 text-violet-500 border-violet-200" },
    { label: "Attendance", value: profile?.attendance != null ? `${profile.attendance}%` : "—", icon: BarChart3, color: "bg-sky-50 text-sky-500 border-sky-200" },
    { label: "Backlogs", value: profile?.backlogs ?? 0, icon: AlertTriangle, color: "bg-rose-50 text-rose-500 border-rose-200" },
    { label: "Year", value: profile?.current_year ?? "—", icon: Calendar, color: "bg-amber-50 text-amber-500 border-amber-200" },
  ];

  return (
    <div className="space-y-8">
      {/* Welcome */}
      <div>
        <h1 className="text-2xl font-semibold text-stone-800">
          Welcome back, {user?.name?.split(" ")[0]} 👋
        </h1>
        <p className="text-stone-400 text-sm mt-1">{profile?.college}</p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((s) => (
          <div key={s.label} className={`bg-white rounded-2xl border p-5 ${s.color.split(" ")[2] || "border-stone-200"}`}>
            <div className={`w-9 h-9 rounded-xl ${s.color.split(" ").slice(0, 2).join(" ")} flex items-center justify-center mb-3`}>
              <s.icon size={18} />
            </div>
            <p className="text-2xl font-bold text-stone-800">{s.value}</p>
            <p className="text-xs font-medium text-stone-400 mt-0.5">{s.label}</p>
          </div>
        ))}
      </div>

      {/* Quick Links */}
      <div>
        <h2 className="text-lg font-semibold text-stone-700 mb-4">Quick Access</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {quickLinks.map((l) => (
            <Link
              key={l.to}
              to={l.to}
              className="bg-white rounded-2xl border border-stone-200 p-5 hover:border-violet-200 transition-colors group"
            >
              <div className={`w-10 h-10 rounded-xl ${l.color} flex items-center justify-center mb-3`}>
                <l.icon size={20} />
              </div>
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="font-semibold text-stone-700 text-sm">{l.label}</h3>
                  <p className="text-xs text-stone-400 mt-0.5">{l.desc}</p>
                </div>
                <ArrowRight size={16} className="text-stone-300 group-hover:text-violet-400 transition-colors" />
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}
