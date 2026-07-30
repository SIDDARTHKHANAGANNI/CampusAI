import { Routes, Route, Navigate } from "react-router-dom";
import { useAuth } from "@/contexts/AuthContext";
import { Loader2 } from "lucide-react";

import LoginPage from "@/pages/auth/LoginPage";
import RegisterPage from "@/pages/auth/RegisterPage";
import AppShell from "@/components/layout/AppShell";
import DashboardPage from "@/pages/dashboard/DashboardPage";
import ProfilePage from "@/pages/profile/ProfilePage";
import EditProfilePage from "@/pages/profile/EditProfilePage";
import CreateProfilePage from "@/pages/profile/CreateProfilePage";
import SkillsPage from "@/pages/skills/SkillsPage";
import ProjectsPage from "@/pages/projects/ProjectsPage";
import AcademicsPage from "@/pages/academics/AcademicsPage";
import CareerGoalsPage from "@/pages/career/CareerGoalsPage";
import ResumeScorePage from "@/pages/resume/ResumeScorePage";
import ResumeMatchPage from "@/pages/resume/ResumeMatchPage";
import TargetRolePage from "@/pages/resume/TargetRolePage";
import NotFoundPage from "@/pages/NotFoundPage";

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { token, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div className="flex h-screen items-center justify-center">
        <Loader2 className="h-8 w-8 animate-spin text-slate-400" />
      </div>
    );
  }

  if (!token) return <Navigate to="/login" replace />;
  return <>{children}</>;
}

function GuestRoute({ children }: { children: React.ReactNode }) {
  const { token, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div className="flex h-screen items-center justify-center">
        <Loader2 className="h-8 w-8 animate-spin text-slate-400" />
      </div>
    );
  }

  if (token) return <Navigate to="/dashboard" replace />;
  return <>{children}</>;
}

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<GuestRoute><LoginPage /></GuestRoute>} />
      <Route path="/register" element={<GuestRoute><RegisterPage /></GuestRoute>} />

      <Route element={<ProtectedRoute><AppShell /></ProtectedRoute>}>
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/profile/edit" element={<EditProfilePage />} />
        <Route path="/profile/create" element={<CreateProfilePage />} />
        <Route path="/skills" element={<SkillsPage />} />
        <Route path="/projects" element={<ProjectsPage />} />
        <Route path="/academics" element={<AcademicsPage />} />
        <Route path="/career-goals" element={<CareerGoalsPage />} />
        <Route path="/resume-score" element={<ResumeScorePage />} />
        <Route path="/resume-match" element={<ResumeMatchPage />} />
        <Route path="/target-role" element={<TargetRolePage />} />
      </Route>

      <Route path="/" element={<Navigate to="/dashboard" replace />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}