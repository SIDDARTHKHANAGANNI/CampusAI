import { Menu } from "lucide-react";
import { useAuth } from "@/contexts/AuthContext";
import { getAvatarUrl } from "@/lib/utils";

interface Props {
  onToggleSidebar: () => void;
}

export default function Navbar({ onToggleSidebar }: Props) {
  const { user } = useAuth();

  return (
    <header className="h-16 bg-white border-b border-[#dde0d5] flex items-center justify-between px-6">
      <div className="flex items-center gap-3">
        <button
          onClick={onToggleSidebar}
          className="lg:hidden text-slate-500 hover:text-slate-900 transition-colors"
        >
          <Menu size={22} />
        </button>
        <span className="text-lg font-bold text-[#343A40] lg:hidden">CampusAI</span>
      </div>

      <div className="flex items-center gap-3">
        <span className="text-sm font-medium text-[#6c757d] hidden sm:block">
          {user?.name}
        </span>
        <img
          src={getAvatarUrl(user?.name || "User")}
          alt="Avatar"
          className="w-8 h-8 rounded-full bg-[#E8F5EE]"
        />
      </div>
    </header>
  );
}
