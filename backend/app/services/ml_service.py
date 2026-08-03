import re
from typing import List, Dict, Any

ROLE_SKILL_MAPPING = {
    "Software Engineer": ["Python", "Java", "DSA", "System Design", "Git", "REST APIs", "SQL"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "TypeScript", "UI/UX"],
    "Backend Developer": ["Python", "Java", "Node.js", "SQL", "REST APIs", "Docker"],
    "Data Scientist": ["Python", "Statistics", "ML", "Pandas", "NumPy", "SQL", "TensorFlow"],
    "DevOps Engineer": ["Docker", "Kubernetes", "CI/CD", "AWS", "Linux", "Terraform"],
    "ML Engineer": ["Python", "ML", "Deep Learning", "TensorFlow", "PyTorch", "MLOps"],
    "Full Stack Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js", "SQL", "Git"],
    "Mobile Developer": ["Kotlin", "Swift", "React Native", "Flutter", "Firebase"],
    "Cloud Architect": ["AWS", "Azure", "GCP", "Docker", "Kubernetes", "Networking"],
    "Cybersecurity Analyst": ["Networking", "Linux", "Python", "Cryptography", "SIEM"]
}

class MLService:
    
    @staticmethod
    def analyze_resume(resume_text: str, target_role: str = None) -> Dict[str, Any]:
        text_lower = resume_text.lower()
        
        # Determine presence of sections
        sections = {
            "contact_info": any(kw in text_lower for kw in ["email", "phone", "linkedin", "github"]),
            "summary": any(kw in text_lower for kw in ["summary", "objective", "profile"]),
            "experience": any(kw in text_lower for kw in ["experience", "work history", "employment"]),
            "education": any(kw in text_lower for kw in ["education", "university", "college", "degree"]),
            "skills": any(kw in text_lower for kw in ["skills", "technologies", "tools"]),
            "projects": any(kw in text_lower for kw in ["projects", "personal projects", "portfolio"])
        }
        
        section_scores = {
            "contact_info": 1.0 if sections["contact_info"] else 0.0,
            "summary": 0.8 if sections["summary"] else 0.0,
            "experience": 1.0 if sections["experience"] else 0.0,
            "education": 1.0 if sections["education"] else 0.0,
            "skills": 1.0 if sections["skills"] else 0.0,
            "projects": 1.0 if sections["projects"] else 0.0
        }
        
        overall_score = sum(section_scores.values()) / len(section_scores) * 100
        
        suggestions = []
        if not sections["summary"]:
            suggestions.append("Add a professional summary or objective.")
        if not sections["experience"] and not sections["projects"]:
            suggestions.append("Highlight your practical experience through internships or personal projects.")
        
        keywords_found = []
        keywords_missing = []
        
        if target_role and target_role in ROLE_SKILL_MAPPING:
            target_skills = ROLE_SKILL_MAPPING[target_role]
            for skill in target_skills:
                if skill.lower() in text_lower:
                    keywords_found.append(skill)
                else:
                    keywords_missing.append(skill)
                    suggestions.append(f"Consider adding or learning '{skill}' for {target_role} roles.")
        
        return {
            "overall_score": overall_score,
            "section_scores": section_scores,
            "suggestions": suggestions,
            "keywords_found": keywords_found,
            "keywords_missing": keywords_missing
        }

    @staticmethod
    def match_resume_to_job(resume_text: str, job_description: str) -> Dict[str, Any]:
        # Simple extraction of capitalized words or tech terms from JD as proxy for skills
        jd_words = set(re.findall(r'\b[A-Z][a-zA-Z]*\b', job_description))
        resume_lower = resume_text.lower()
        
        matching_skills = []
        missing_skills = []
        
        # Common tech stopwords to ignore
        stopwords = {"The", "We", "Are", "Looking", "For", "A", "An", "And", "With", "In", "To", "Of", "Our", "Team"}
        jd_skills = jd_words - stopwords
        
        for skill in jd_skills:
            if skill.lower() in resume_lower:
                matching_skills.append(skill)
            else:
                missing_skills.append(skill)
                
        total_skills = len(matching_skills) + len(missing_skills)
        match_score = (len(matching_skills) / total_skills * 100) if total_skills > 0 else 0
        
        suggestions = []
        if missing_skills:
            suggestions.append(f"Try to incorporate these keywords if you have the experience: {', '.join(missing_skills[:5])}")
            
        return {
            "match_score": match_score,
            "matching_skills": matching_skills,
            "missing_skills": missing_skills,
            "suggestions": suggestions
        }

    @staticmethod
    def predict_placement_readiness(student: Any, skills: List[Any], projects: List[Any], academics: List[Any]) -> Dict[str, Any]:
        cgpa_score = min((student.cgpa / 10.0) * 100 if student.cgpa else 0, 100)
        
        skill_score = min(len(skills) * 10, 100)
        project_score = min(len(projects) * 20, 100)
        
        backlog_penalty = (student.backlogs * 10) if getattr(student, 'backlogs', 0) else 0
        attendance_val = getattr(student, 'attendance', 75)
        if attendance_val is None:
            attendance_val = 75
        attendance_penalty = max(0, 75 - attendance_val) * 2
        
        readiness_score = (cgpa_score * 0.25) + (skill_score * 0.25) + (project_score * 0.20) + (max(0, 100 - backlog_penalty)) * 0.15 + (max(0, 100 - attendance_penalty)) * 0.15
        readiness_score = max(0, min(readiness_score, 100))
        
        confidence = "High" if readiness_score > 80 else "Medium" if readiness_score > 60 else "Low"
        
        strengths = []
        weaknesses = []
        suggestions = []
        
        if cgpa_score >= 80:
            strengths.append("Strong academic performance")
        else:
            weaknesses.append("CGPA could be improved")
            suggestions.append("Focus on scoring higher in upcoming semesters")
            
        if len(projects) >= 2:
            strengths.append("Good project portfolio")
        else:
            weaknesses.append("Lack of practical projects")
            suggestions.append("Build more hands-on projects to showcase your skills")
            
        if getattr(student, 'backlogs', 0) and student.backlogs > 0:
            weaknesses.append(f"Active backlogs ({student.backlogs})")
            suggestions.append("Clear pending backlogs as a priority")
            
        return {
            "readiness_score": readiness_score,
            "confidence": confidence,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "suggestions": suggestions
        }

    @staticmethod
    def predict_academic_risk(student: Any, academics: List[Any]) -> Dict[str, Any]:
        risk_score = 0
        risk_factors = []
        suggestions = []
        
        student_backlogs = getattr(student, 'backlogs', 0)
        if student_backlogs and student_backlogs > 0:
            risk_score += min(student_backlogs * 20, 50)
            risk_factors.append(f"Has {student_backlogs} active backlogs")
            suggestions.append("Attend remedial classes and focus on clearing backlogs")
            
        student_attendance = getattr(student, 'attendance', 100)
        if student_attendance and student_attendance < 75:
            risk_score += (75 - student_attendance) * 2
            risk_factors.append(f"Low overall attendance ({student_attendance}%)")
            suggestions.append("Improve attendance to avoid being debarred from exams")
            
        trend = "Stable"
        if len(academics) >= 2:
            sorted_acad = sorted(academics, key=lambda x: getattr(x, 'semester', 0))
            if sorted_acad[-1].semester_gpa < sorted_acad[-2].semester_gpa:
                trend = "Declining"
                risk_score += 15
                risk_factors.append("Declining GPA trend in recent semesters")
                suggestions.append("Identify reasons for recent GPA drop and seek help if needed")
            elif sorted_acad[-1].semester_gpa > sorted_acad[-2].semester_gpa:
                trend = "Improving"
                risk_score -= 10
                
        risk_score = max(0, min(risk_score, 100))
        
        if risk_score > 75:
            risk_level = "Critical"
        elif risk_score > 50:
            risk_level = "High"
        elif risk_score > 25:
            risk_level = "Medium"
        else:
            risk_level = "Low"
            
        return {
            "risk_score": risk_score,
            "risk_level": risk_level,
            "trend": trend,
            "risk_factors": risk_factors,
            "suggestions": suggestions
        }

    @staticmethod
    def generate_learning_path(target_role: str, current_skills: List[str], timeline_months: int = 6) -> Dict[str, Any]:
        role_skills = ROLE_SKILL_MAPPING.get(target_role, ROLE_SKILL_MAPPING["Software Engineer"])
        
        current_skills_lower = [s.lower() for s in current_skills]
        missing_skills = [skill for skill in role_skills if skill.lower() not in current_skills_lower]
        
        steps = []
        if not missing_skills:
            steps.append({
                "step": 1,
                "topic": "Advanced Application",
                "description": f"You already have the core skills for {target_role}. Focus on building complex systems.",
                "duration_weeks": timeline_months * 4,
                "resources": ["Build open source projects", "Contribute to GitHub", "System Design Interview Prep"]
            })
            return {"steps": steps}
            
        weeks_per_skill = max(1, (timeline_months * 4) // len(missing_skills))
        
        for i, skill in enumerate(missing_skills):
            steps.append({
                "step": i + 1,
                "topic": f"Master {skill}",
                "description": f"Learn the fundamentals and practical applications of {skill} for a {target_role} role.",
                "duration_weeks": weeks_per_skill,
                "resources": [f"Online courses for {skill}", f"{skill} official documentation", f"Mini-project using {skill}"]
            })
            
        return {"steps": steps}

    @staticmethod
    def recommend_careers(student: Any, skills: List[Any], projects: List[Any]) -> Dict[str, Any]:
        student_skill_names = [getattr(s, 'name', '').lower() for s in skills]
        
        recommendations = []
        
        for role, required_skills in ROLE_SKILL_MAPPING.items():
            matching_skills = [skill for skill in required_skills if skill.lower() in student_skill_names]
            missing_skills = [skill for skill in required_skills if skill.lower() not in student_skill_names]
            
            match_percentage = (len(matching_skills) / len(required_skills)) * 100 if required_skills else 0
            
            # Boost based on projects if any tech matches
            project_techs = []
            for p in projects:
                techs = getattr(p, 'technologies', '')
                if techs:
                    project_techs.extend([t.strip().lower() for t in techs.split(',')])
                    
            if any(skill.lower() in project_techs for skill in required_skills):
                match_percentage += 10
                
            match_percentage = min(match_percentage, 100)
            
            recommendations.append({
                "role": role,
                "match_percentage": round(match_percentage, 2),
                "description": f"A good fit based on your background. Requires {len(required_skills)} key skills.",
                "required_skills": required_skills,
                "skill_gaps": missing_skills
            })
            
        # Sort by match percentage descending
        recommendations.sort(key=lambda x: x["match_percentage"], reverse=True)
        
        return {"recommendations": recommendations[:5]}
