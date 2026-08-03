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
import ResumeAnalysisPage from "@/pages/resume/ResumeScorePage";
import ResumeMatchingPage from "@/pages/resume/ResumeMatchPage";
import PlacementReadinessPage from "@/pages/resume/TargetRolePage";
import AcademicRiskPage from "@/pages/ml/AcademicRiskPage";
import LearningPathPage from "@/pages/ml/LearningPathPage";
import CareerRecommendationPage from "@/pages/ml/CareerRecommendationPage";
import NotFoundPage from "@/pages/NotFoundPage";
import LandingPage from "@/pages/LandingPage";

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
        {/* ML Features */}
        <Route path="/resume-analysis" element={<ResumeAnalysisPage />} />
        <Route path="/resume-matching" element={<ResumeMatchingPage />} />
        <Route path="/placement-readiness" element={<PlacementReadinessPage />} />
        <Route path="/academic-risk" element={<AcademicRiskPage />} />
        <Route path="/learning-path" element={<LearningPathPage />} />
        <Route path="/career-recommendation" element={<CareerRecommendationPage />} />
      </Route>

      <Route path="/" element={<LandingPage />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}