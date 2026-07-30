import { Link } from "react-router-dom";

export default function NotFoundPage() {
  return (
    <div className="min-h-screen bg-[#faf8f6] flex items-center justify-center p-4">
      <div className="text-center">
        <p className="text-7xl font-bold text-stone-200 mb-4">404</p>
        <h1 className="text-xl font-semibold text-stone-700 mb-2">Page not found</h1>
        <p className="text-stone-400 text-sm mb-6">The page you're looking for doesn't exist.</p>
        <Link
          to="/dashboard"
          className="bg-violet-500 hover:bg-violet-600 text-white font-medium px-6 py-2.5 rounded-xl transition-colors inline-block"
        >
          Go to Dashboard
        </Link>
      </div>
    </div>
  );
}
