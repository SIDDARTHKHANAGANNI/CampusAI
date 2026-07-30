import { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { loginSchema, type LoginForm } from "@/schemas/auth";
import { useAuth } from "@/contexts/AuthContext";
import { Link, useNavigate } from "react-router-dom";
import { Loader2 } from "lucide-react";

export default function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [error, setError] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<LoginForm>({ resolver: zodResolver(loginSchema) });

  const onSubmit = async (data: LoginForm) => {
    setError("");
    try {
      await login(data);
      navigate("/dashboard");
    } catch (err: any) {
      setError(err.response?.data?.detail || "Login failed. Please try again.");
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-slate-900 mb-2">CampusAI</h1>
          <p className="text-slate-500 text-sm">Your AI-powered campus companion</p>
        </div>

        <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-8">
          <h2 className="text-2xl font-semibold text-slate-900 mb-1">Welcome back</h2>
          <p className="text-slate-500 text-sm mb-6">Sign in to your account</p>
          {error && (
            <div className="bg-[#FFF5F0] text-[#8B4513] text-sm font-medium px-4 py-3 rounded-xl mb-4">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <div>
              <label className="text-sm font-medium text-[#6c757d] mb-1.5 block">Email</label>
              <input
                type="email"
                {...register("email")}
                className="w-full bg-[#F6F7F2] border border-[#dde0d5] rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-[#B7E4C7] focus:border-[#B7E4C7] transition-all text-sm"
                placeholder="you@example.com"
              />
              {errors.email && <p className="text-[#8B4513] text-xs mt-1">{errors.email.message}</p>}
            </div>

            <div>
              <label className="text-sm font-medium text-[#6c757d] mb-1.5 block">Password</label>
              <input
                type="password"
                {...register("password")}
                className="w-full bg-[#F6F7F2] border border-[#dde0d5] rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-[#B7E4C7] focus:border-[#B7E4C7] transition-all text-sm"
                placeholder="••••••••"
              />
              {errors.password && <p className="text-[#8B4513] text-xs mt-1">{errors.password.message}</p>}
            </div>

            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full bg-[#343A40] hover:bg-[#2a2f33] disabled:opacity-60 text-white font-medium py-2.5 rounded-xl transition-colors flex items-center justify-center gap-2"
            >
              {isSubmitting && <Loader2 size={16} className="animate-spin" />}
              {isSubmitting ? "Signing in..." : "Sign In"}
            </button>
          </form>

          <p className="text-center text-sm text-[#8d9490] mt-6">
            Don't have an account?{" "}
            <Link to="/register" className="text-[#343A40] font-medium hover:text-[#343A40]">
              Register
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
