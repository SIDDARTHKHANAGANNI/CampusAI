import api from "./client";
import type { Skill, SkillCreate, SkillUpdate } from "@/types";

export const skillsApi = {
  getAll: async (): Promise<Skill[]> => {
    const res = await api.get("/students/me/skills");
    return res.data;
  },
  create: async (data: SkillCreate): Promise<Skill> => {
    const res = await api.post("/students/me/skills", data);
    return res.data;
  },
  update: async (id: number, data: SkillUpdate): Promise<Skill> => {
    const res = await api.put(`/students/me/skills/${id}`, data);
    return res.data;
  },
};
