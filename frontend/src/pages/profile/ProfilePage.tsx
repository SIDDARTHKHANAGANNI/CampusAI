import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { studentApi } from "@/api/student";
import type { StudentProfile } from "@/types";
import { Spinner } from "@/components/ui/Spinner";
import { getAvatarUrl } from "@/lib/utils";
import { Pencil, Mail, Building, BookOpen, Calendar, TrendingUp, Target, AlertTriangle } from "lucide-react";

export default function ProfilePage() {
  const [profile, setProfile] = useState<StudentProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    studentApi
      .getProfile()
      .then(setProfile)
      .catch((err) => {
        if (err.response?.status === 404) navigate("/profile/create");
      })
      .finally(() => setLoading(false));
  }, [navigate]);

  if (loading) return <Spinner />;
  if (!profile) return null;

  const fields = [
    { label: "Email", value: profile.email, icon: Mail },
    { label: "College", value: profile.college, icon: Building },
    { label: "Degree", value: profile.degree, icon: BookOpen },
    { label: "Branch", value: profile.branch, icon: BookOpen },
    { label: "Current Year", value: profile.current_year, icon: Calendar },
    { label: "Graduation Year", value: profile.graduation_year, icon: Calendar },
    { label: "CGPA", value: profile.cgpa, icon: TrendingUp },
    { label: "Attendance", value: profile.attendance != null ? `${profile.attendance}%` : "Not set", icon: TrendingUp },
    { label: "Backlogs", value: profile.backlogs, icon: AlertTriangle },
    { label: "Target Role", value: profile.target_role, icon: Target },
  ];

  return (
    <div className="space-y-6">
      {/* Header Card */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 flex flex-col sm:flex-row items-center gap-6">
        <img
          src={getAvatarUrl(profile.name)}
          alt="Avatar"
          className="w-20 h-20 rounded-full bg-slate-100"
        />
        <div className="flex-1 text-center sm:text-left">
          <h1 className="text-2xl font-semibold text-slate-900">{profile.name}</h1>
          <p className="text-slate-500 text-sm">{profile.branch} • Year {profile.current_year}</p>
          <p className="text-slate-500 text-sm">{profile.college}</p>
        </div>
        <Link
          to="/profile/edit"
          className="bg-slate-900 hover:bg-slate-800 text-white font-medium px-5 py-2 rounded-xl transition-colors flex items-center gap-2 text-sm"
        >
          <Pencil size={16} /> Edit Profile
        </Link>
      </div>

      {/* Info Grid */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6">
        <h2 className="text-lg font-semibold text-slate-900 mb-4">Profile Details</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {fields.map((f) => (
            <div key={f.label} className="flex items-center gap-3 p-3 rounded-xl bg-slate-50">
              <div className="w-8 h-8 rounded-lg bg-slate-100 flex items-center justify-center text-slate-900">
                <f.icon size={16} />
              </div>
              <div>
                <p className="text-xs font-medium text-slate-500">{f.label}</p>
                <p className="text-sm font-semibold text-slate-900">{f.value}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}