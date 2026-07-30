import { z } from "zod";

export const studentSchema = z.object({
  name: z.string().min(2, "Min 2 characters").max(100),
  email: z.string().email("Enter a valid email"),
  college: z.string().min(2, "Min 2 characters").max(200),
  degree: z.string().min(2, "Min 2 characters").max(100),
  branch: z.string().min(2, "Min 2 characters").max(100),
  current_year: z.coerce.number().int().min(1).max(6),
  graduation_year: z.coerce.number().int().min(2020).max(2040),
  cgpa: z.coerce.number().min(0).max(10),
  attendance: z.coerce.number().min(0).max(100).nullable().optional(),
  backlogs: z.coerce.number().int().min(0).default(0),
  target_role: z.string().min(2, "Min 2 characters").max(100),
});

export type StudentForm = z.infer<typeof studentSchema>;

export const academicSchema = z.object({
  semester: z.coerce.number().int().min(1).max(12),
  semester_gpa: z.coerce.number().min(0).max(10),
  attendance: z.coerce.number().min(0).max(100).nullable().optional(),
  backlogs: z.coerce.number().int().min(0).default(0),
});

export type AcademicForm = z.infer<typeof academicSchema>;

export const skillSchema = z.object({
  name: z.string().min(1, "Required").max(100),
  category: z.string().max(100).nullable().optional(),
  proficiency: z.string().min(1, "Required").max(50),
});

export type SkillForm = z.infer<typeof skillSchema>;

export const projectSchema = z.object({
  title: z.string().min(1, "Title is required"),
  description: z.string().nullable().optional(),
  technologies: z.string().nullable().optional(),
  github_url: z.string().url("Must be a valid URL").nullable().optional().or(z.literal("")),
});

export type ProjectForm = z.infer<typeof projectSchema>;

export const careerGoalSchema = z.object({
  target_role: z.string().min(1, "Target role is required"),
  target_company_type: z.string().nullable().optional(),
  target_timeline: z.string().nullable().optional(),
});

export type CareerGoalForm = z.infer<typeof careerGoalSchema>;
