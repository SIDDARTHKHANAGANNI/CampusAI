import { NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "@/contexts/AuthContext";
import {
  LayoutDashboard, User, Code2, FolderGit2, GraduationCap,
  Target, FileText, Briefcase, Compass, LogOut, X,
} from "lucide-react";

const links = [
  { to: "/dashboard", icon: LayoutDashboard, label: "Dashboard" },
  { to: "/profile", icon: User, label: "Profile" },
  { to: "/skills", icon: Code2, label: "Skills" },
  { to: "/projects", icon: FolderGit2, label: "Projects" },
  { to: "/academics", icon: GraduationCap, label: "Academics" },
  { to: "/career-goals", icon: Target, label: "Career Goals" },
  { to: "/resume-score", icon: FileText, label: "Resume Score" },
  { to: "/resume-match", icon: Briefcase, label: "Resume Match" },
  { to: "/target-role", icon: Compass, label: "Target Role" },
];

interface Props {
  open: boolean;
  onClose: () => void;
}

export default function Sidebar({ open, onClose }: Props) {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <>
      {/* Backdrop for mobile */}
      {open && (
        <div className="fixed inset-0 z-30 bg-black/20 lg:hidden" onClick={onClose} />
      )}

      <aside
        className={`fixed top-0 left-0 z-40 h-full w-64 bg-white border-r border-stone-200 flex flex-col transition-transform duration-200 lg:translate-x-0 ${
          open ? "translate-x-0" : "-translate-x-full"
        }`}
      >
        {/* Brand */}
        <div className="flex items-center justify-between px-6 h-16 border-b border-stone-100">
          <span className="text-xl font-bold text-violet-600">CampusAI</span>
          <button onClick={onClose} className="lg:hidden text-stone-400 hover:text-stone-600">
            <X size={20} />
          </button>
        </div>

        {/* Nav */}
        <nav className="flex-1 overflow-y-auto px-3 py-4 space-y-1">
          {links.map((l) => (
            <NavLink
              key={l.to}
              to={l.to}
              onClick={onClose}
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-colors ${
                  isActive
                    ? "bg-violet-50 text-violet-600"
                    : "text-stone-500 hover:bg-violet-50 hover:text-violet-600"
                }`
              }
            >
              <l.icon size={18} />
              {l.label}
            </NavLink>
          ))}
        </nav>

        {/* Logout */}
        <div className="px-3 py-4 border-t border-stone-100">
          <button
            onClick={handleLogout}
            className="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-stone-400 hover:text-rose-500 hover:bg-rose-50 transition-colors w-full"
          >
            <LogOut size={18} />
            Logout
          </button>
        </div>
      </aside>
    </>
  );
}
