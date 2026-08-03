import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { 
  User, 
  Settings, 
  FolderGit2, 
  GraduationCap, 
  Target, 
  FileText, 
  FileSearch, 
  TrendingUp, 
  AlertTriangle, 
  Map, 
  Compass,
  Menu,
  X,
  ChevronDown,
  ArrowRight
} from 'lucide-react';

const LandingPage: React.FC = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const features = [
    {
      title: "Student Profile",
      description: "Track your academic info, CGPA, attendance, and target role in one place",
      icon: <User className="w-5 h-5 text-[#343A40]" />
    },
    {
      title: "Skill Management",
      description: "Add, organize, and rate your technical skills by proficiency level",
      icon: <Settings className="w-5 h-5 text-[#343A40]" />
    },
    {
      title: "Project Portfolio",
      description: "Showcase your projects with descriptions, tech stack, and GitHub links",
      icon: <FolderGit2 className="w-5 h-5 text-[#343A40]" />
    },
    {
      title: "Academic Records",
      description: "Monitor semester-wise GPA, attendance, and backlog trends",
      icon: <GraduationCap className="w-5 h-5 text-[#343A40]" />
    },
    {
      title: "Career Goals",
      description: "Set and track your target roles, company preferences, and timelines",
      icon: <Target className="w-5 h-5 text-[#343A40]" />
    },
    {
      title: "Resume Analysis",
      description: "Get AI-generated feedback on resume structure, keywords, and formatting",
      icon: <FileText className="w-5 h-5 text-[#343A40]" />
    },
    {
      title: "Resume–Job Matching",
      description: "Compare your resume against job descriptions to find skill gaps",
      icon: <FileSearch className="w-5 h-5 text-[#343A40]" />
    },
    {
      title: "Placement Readiness",
      description: "Assess your preparation level for campus placements",
      icon: <TrendingUp className="w-5 h-5 text-[#343A40]" />
    },
    {
      title: "Academic Risk Detection",
      description: "Identify potential academic risks early with trend analysis",
      icon: <AlertTriangle className="w-5 h-5 text-[#343A40]" />
    },
    {
      title: "Learning Path Generator",
      description: "Get a personalized roadmap to learn missing skills for your target role",
      icon: <Map className="w-5 h-5 text-[#343A40]" />
    },
    {
      title: "Career Recommendation",
      description: "Discover career paths that match your current skill set and interests",
      icon: <Compass className="w-5 h-5 text-[#343A40]" />
    }
  ];

  const howItWorks = [
    {
      step: "01",
      title: "Create Your Profile",
      description: "Add your academic details, skills, projects, and career goals to build your student profile."
    },
    {
      step: "02",
      title: "Get Insights",
      description: "Our AI tools analyze your profile to surface patterns, gaps, and opportunities in your journey."
    },
    {
      step: "03",
      title: "Take Action",
      description: "Use personalized recommendations to improve your skills, resume, and career readiness."
    }
  ];

  return (
    <div className="font-['Outfit'] min-h-screen bg-[#F6F7F2] text-[#343A40]">
      {/* ========== NAVBAR ========== */}
      <nav
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
          isScrolled
            ? 'bg-white/90 backdrop-blur-md shadow-sm border-b border-gray-100'
            : 'bg-transparent'
        }`}
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            {/* Logo */}
            <div className="flex-shrink-0 flex items-center">
              <Link
                to="/"
                className="text-xl tracking-wide text-[#343A40]"
                style={{ fontFamily: "'Nunito', sans-serif", fontWeight: 900 }}
              >
                CAMPUS AI
              </Link>
            </div>
            
            {/* Desktop Nav Links — center */}
            <div className="hidden md:flex items-center space-x-8">
              <a
                href="#about"
                className="text-[#343A40]/70 hover:text-[#343A40] font-medium text-sm transition-colors"
              >
                About
              </a>
              <a
                href="#features"
                className="text-[#343A40]/70 hover:text-[#343A40] font-medium text-sm transition-colors"
              >
                Features
              </a>
              <a
                href="#how-it-works"
                className="text-[#343A40]/70 hover:text-[#343A40] font-medium text-sm transition-colors"
              >
                How It Works
              </a>
              <a
                href="#contact"
                className="text-[#343A40]/70 hover:text-[#343A40] font-medium text-sm transition-colors"
              >
                Contact
              </a>
            </div>

            {/* Desktop Auth Buttons — right */}
            <div className="hidden md:flex items-center space-x-3">
              <Link
                to="/login"
                className="text-[#343A40] hover:text-black font-medium text-sm transition-colors px-4 py-2 rounded-full hover:bg-[#343A40]/5"
              >
                Sign In
              </Link>
              <Link
                to="/register"
                className="bg-[#343A40] hover:bg-black text-white rounded-full px-5 py-2 font-semibold text-sm transition-all hover:shadow-lg hover:shadow-[#343A40]/20"
              >
                Sign Up
              </Link>
            </div>

            {/* Mobile menu button */}
            <div className="md:hidden flex items-center">
              <button
                onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
                className="text-[#343A40] hover:text-black focus:outline-none p-2 rounded-lg hover:bg-[#343A40]/5 transition-colors"
              >
                {isMobileMenuOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
              </button>
            </div>
          </div>
        </div>

        {/* Mobile Menu */}
        {isMobileMenuOpen && (
          <div className="md:hidden bg-white/95 backdrop-blur-md border-b border-gray-100">
            <div className="px-4 pt-2 pb-4 space-y-1">
              <a 
                href="#about" 
                className="block px-3 py-2.5 text-sm font-medium text-[#343A40]/70 hover:text-[#343A40] hover:bg-[#F6F7F2] rounded-lg transition-colors"
                onClick={() => setIsMobileMenuOpen(false)}
              >
                About
              </a>
              <a 
                href="#features" 
                className="block px-3 py-2.5 text-sm font-medium text-[#343A40]/70 hover:text-[#343A40] hover:bg-[#F6F7F2] rounded-lg transition-colors"
                onClick={() => setIsMobileMenuOpen(false)}
              >
                Features
              </a>
              <a 
                href="#how-it-works" 
                className="block px-3 py-2.5 text-sm font-medium text-[#343A40]/70 hover:text-[#343A40] hover:bg-[#F6F7F2] rounded-lg transition-colors"
                onClick={() => setIsMobileMenuOpen(false)}
              >
                How It Works
              </a>
              <a 
                href="#contact" 
                className="block px-3 py-2.5 text-sm font-medium text-[#343A40]/70 hover:text-[#343A40] hover:bg-[#F6F7F2] rounded-lg transition-colors"
                onClick={() => setIsMobileMenuOpen(false)}
              >
                Contact
              </a>
              <div className="pt-3 border-t border-gray-100 mt-2 space-y-1">
                <Link 
                  to="/login" 
                  className="block px-3 py-2.5 text-sm font-medium text-[#343A40] hover:bg-[#F6F7F2] rounded-lg transition-colors"
                  onClick={() => setIsMobileMenuOpen(false)}
                >
                  Sign In
                </Link>
                <Link 
                  to="/register" 
                  className="block px-3 py-2.5 text-sm font-semibold text-white bg-[#343A40] hover:bg-black rounded-lg transition-colors text-center"
                  onClick={() => setIsMobileMenuOpen(false)}
                >
                  Sign Up
                </Link>
              </div>
            </div>
          </div>
        )}
      </nav>

      {/* ========== HERO SECTION ========== */}
      <section className="pt-16 min-h-screen flex flex-col items-center justify-center bg-[#F6F7F2] px-4 relative overflow-hidden">
        {/* Subtle background decoration */}
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute top-1/4 -left-32 w-96 h-96 bg-[#B7E4C7]/20 rounded-full blur-3xl"></div>
          <div className="absolute bottom-1/4 -right-32 w-96 h-96 bg-[#B7E4C7]/15 rounded-full blur-3xl"></div>
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-[#B7E4C7]/10 rounded-full blur-3xl"></div>
        </div>

        <div className="text-center max-w-4xl mx-auto relative z-10">
          {/* Small badge above the heading */}
          <div className="inline-flex items-center gap-2 bg-white/60 backdrop-blur-sm border border-[#B7E4C7]/40 rounded-full px-4 py-1.5 mb-8">
            <div className="w-2 h-2 rounded-full bg-[#52B788] animate-pulse"></div>
            <span className="text-xs font-medium text-[#343A40]/60 tracking-wide uppercase">
              Open-source student platform
            </span>
          </div>

          {/* Main heading with rounded font */}
          <h1
            className="text-7xl sm:text-8xl md:text-9xl text-[#343A40] tracking-tight mb-6 leading-none"
            style={{ fontFamily: "'Nunito', sans-serif", fontWeight: 900 }}
          >
            CAMPUS AI
          </h1>

          {/* Tagline — honest, no fake claims */}
          <p className="text-base sm:text-lg md:text-xl text-[#343A40]/55 mb-10 max-w-2xl mx-auto leading-relaxed font-light">
            A student-focused platform to organize your academics, track skills,
            manage projects, and explore career paths — all in one place.
          </p>

          {/* CTA buttons */}
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link 
              to="/register" 
              className="group w-full sm:w-auto bg-[#343A40] hover:bg-black text-white rounded-full px-8 py-3.5 font-semibold transition-all hover:shadow-xl hover:shadow-[#343A40]/15 flex items-center justify-center gap-2"
            >
              Get Started
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </Link>
            <a 
              href="#features" 
              className="w-full sm:w-auto border-2 border-[#343A40]/20 text-[#343A40] hover:border-[#343A40] hover:bg-[#343A40] hover:text-white rounded-full px-8 py-3.5 font-semibold transition-all"
            >
              Explore Features
            </a>
          </div>
        </div>

        {/* Scroll indicator */}
        <div className="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 animate-bounce">
          <span className="text-xs text-[#343A40]/30 font-medium tracking-widest uppercase">Scroll</span>
          <ChevronDown className="w-4 h-4 text-[#343A40]/30" />
        </div>
      </section>

      {/* ========== ABOUT SECTION ========== */}
      <section id="about" className="bg-white py-24 px-4">
        <div className="max-w-3xl mx-auto text-center">
          <span className="inline-block text-xs font-semibold text-[#52B788] tracking-widest uppercase mb-4">
            About CampusAI
          </span>
          <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-[#343A40] mb-6 leading-tight">
            Built for students,{' '}
            <span className="text-[#52B788]">by students</span>
          </h2>
          <p className="text-base sm:text-lg text-[#343A40]/65 leading-relaxed max-w-2xl mx-auto">
            CampusAI is a platform that brings together your academic data, 
            skills, projects, and career goals into one dashboard. It uses AI-based tools 
            to help you analyze your resume, discover skill gaps, and plan your learning path.
          </p>
        </div>
      </section>

      {/* ========== FEATURES SECTION ========== */}
      <section id="features" className="bg-[#F6F7F2] py-24 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <span className="inline-block text-xs font-semibold text-[#52B788] tracking-widest uppercase mb-4">
              Features
            </span>
            <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-[#343A40] mb-4">
              Everything you need
            </h2>
            <p className="text-base sm:text-lg text-[#343A40]/55 max-w-2xl mx-auto">
              Tools to help you track, analyze, and organize your academic and career journey.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {features.map((feature, index) => (
              <div 
                key={index} 
                className="group bg-white rounded-2xl p-6 hover:shadow-lg hover:shadow-[#B7E4C7]/20 transition-all duration-300 border border-transparent hover:border-[#B7E4C7]/30"
              >
                <div className="w-11 h-11 rounded-xl bg-[#B7E4C7]/25 group-hover:bg-[#B7E4C7]/40 flex items-center justify-center mb-4 transition-colors">
                  {feature.icon}
                </div>
                <h3 className="text-lg font-semibold text-[#343A40] mb-2">{feature.title}</h3>
                <p className="text-sm text-[#343A40]/55 leading-relaxed">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ========== HOW IT WORKS SECTION ========== */}
      <section id="how-it-works" className="bg-white py-24 px-4">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-16">
            <span className="inline-block text-xs font-semibold text-[#52B788] tracking-widest uppercase mb-4">
              How It Works
            </span>
            <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-[#343A40] mb-4">
              Three simple steps
            </h2>
            <p className="text-base sm:text-lg text-[#343A40]/55 max-w-xl mx-auto">
              Getting started with CampusAI is straightforward.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {howItWorks.map((item, index) => (
              <div key={index} className="text-center relative">
                {/* Connector line for desktop */}
                {index < howItWorks.length - 1 && (
                  <div className="hidden md:block absolute top-8 left-[60%] w-[80%] h-[2px] bg-gradient-to-r from-[#B7E4C7] to-[#B7E4C7]/20"></div>
                )}
                <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-[#F6F7F2] border-2 border-[#B7E4C7]/30 mb-5 relative z-10">
                  <span
                    className="text-xl text-[#52B788]"
                    style={{ fontFamily: "'Nunito', sans-serif", fontWeight: 900 }}
                  >
                    {item.step}
                  </span>
                </div>
                <h3 className="text-lg font-semibold text-[#343A40] mb-2">{item.title}</h3>
                <p className="text-sm text-[#343A40]/55 leading-relaxed max-w-xs mx-auto">
                  {item.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ========== CTA SECTION ========== */}
      <section className="bg-[#343A40] py-20 px-4">
        <div className="max-w-3xl mx-auto text-center">
          <h2
            className="text-3xl sm:text-4xl md:text-5xl text-white mb-4 tracking-tight"
            style={{ fontFamily: "'Nunito', sans-serif", fontWeight: 800 }}
          >
            Ready to get started?
          </h2>
          <p className="text-base sm:text-lg text-gray-400 mb-8 max-w-xl mx-auto">
            Create your free account and start organizing your academic journey today.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link
              to="/register"
              className="group w-full sm:w-auto bg-white text-[#343A40] hover:bg-[#F6F7F2] rounded-full px-8 py-3.5 font-semibold transition-all hover:shadow-xl flex items-center justify-center gap-2"
            >
              Create Account
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </Link>
            <Link
              to="/login"
              className="w-full sm:w-auto border-2 border-white/20 text-white hover:border-white/50 rounded-full px-8 py-3.5 font-semibold transition-all"
            >
              Sign In
            </Link>
          </div>
        </div>
      </section>

      {/* ========== CONTACT SECTION ========== */}
      <section id="contact" className="bg-[#F6F7F2] py-24 px-4">
        <div className="max-w-3xl mx-auto text-center">
          <span className="inline-block text-xs font-semibold text-[#52B788] tracking-widest uppercase mb-4">
            Contact
          </span>
          <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-[#343A40] mb-6">
            Get in touch
          </h2>
          <p className="text-base sm:text-lg text-[#343A40]/55 leading-relaxed mb-8">
            Have questions or feedback? We'd love to hear from you.
          </p>
          <a
            href="mailto:hello@campusai.dev"
            className="inline-flex items-center gap-2 bg-white border border-[#343A40]/10 rounded-full px-6 py-3 font-medium text-[#343A40] hover:border-[#343A40]/30 hover:shadow-md transition-all"
          >
            hello@campusai.dev
          </a>
        </div>
      </section>

      {/* ========== FOOTER ========== */}
      <footer className="bg-[#343A40] text-white py-10 px-4 border-t border-white/5">
        <div className="max-w-7xl mx-auto">
          <div className="flex flex-col md:flex-row justify-between items-center gap-6">
            <div>
              <span
                className="text-lg tracking-wide"
                style={{ fontFamily: "'Nunito', sans-serif", fontWeight: 900 }}
              >
                CAMPUS AI
              </span>
            </div>
            <div className="flex flex-wrap justify-center gap-6">
              <a href="#about" className="text-gray-400 hover:text-white transition-colors text-sm">About</a>
              <a href="#features" className="text-gray-400 hover:text-white transition-colors text-sm">Features</a>
              <a href="#how-it-works" className="text-gray-400 hover:text-white transition-colors text-sm">How It Works</a>
              <a href="#contact" className="text-gray-400 hover:text-white transition-colors text-sm">Contact</a>
              <Link to="/login" className="text-gray-400 hover:text-white transition-colors text-sm">Sign In</Link>
            </div>
            <div className="text-gray-500 text-sm">
              &copy; {new Date().getFullYear()} CampusAI
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;
