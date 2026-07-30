// ---- Auth ----
export interface User {
  id: number;
  name: string;
  email: string;
  is_active: boolean;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export interface LoginPayload {
  email: string;
  password: string;
}

export interface RegisterPayload {
  name: string;
  email: string;
  password: string;
}

// ---- Student ----
export interface Student {
  id: number;
  name: string;
  email: string;
  college: string;
  degree: string;
  branch: string;
  current_year: number;
  graduation_year: number;
  cgpa: number;
  attendance: number | null;
  backlogs: number;
  target_role: string;
}

export interface StudentProfile extends Student {
  academic_records: AcademicRecord[];
  skills: Skill[];
  projects: Project[];
  career_goals: CareerGoal[];
}

export interface StudentCreate {
  name: string;
  email: string;
  college: string;
  degree: string;
  branch: string;
  current_year: number;
  graduation_year: number;
  cgpa: number;
  attendance?: number | null;
  backlogs?: number;
  target_role: string;
}

export type StudentUpdate = Partial<StudentCreate>;

// ---- Academic ----
export interface AcademicRecord {
  id: number;
  student_id: number;
  semester: number;
  semester_gpa: number;
  attendance: number | null;
  backlogs: number;
}

export interface AcademicCreate {
  semester: number;
  semester_gpa: number;
  attendance?: number | null;
  backlogs?: number;
}

export type AcademicUpdate = Partial<AcademicCreate>;

// ---- Skill ----
export interface Skill {
  id: number;
  student_id: number;
  name: string;
  category: string | null;
  proficiency: string;
}

export interface SkillCreate {
  name: string;
  category?: string | null;
  proficiency: string;
}

export type SkillUpdate = Partial<SkillCreate>;

// ---- Project ----
export interface Project {
  id: number;
  student_id: number;
  title: string;
  description: string | null;
  technologies: string | null;
  github_url: string | null;
}

export interface ProjectCreate {
  title: string;
  description?: string | null;
  technologies?: string | null;
  github_url?: string | null;
}

export type ProjectUpdate = Partial<ProjectCreate>;

// ---- Career Goal ----
export interface CareerGoal {
  id: number;
  student_id: number;
  target_role: string;
  target_company_type: string | null;
  target_timeline: string | null;
}

export interface CareerGoalCreate {
  target_role: string;
  target_company_type?: string | null;
  target_timeline?: string | null;
}

export type CareerGoalUpdate = Partial<CareerGoalCreate>;
