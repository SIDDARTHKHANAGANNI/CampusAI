import api from "./client";
import type { Project, ProjectCreate, ProjectUpdate } from "@/types";

export const projectsApi = {
  getAll: async (): Promise<Project[]> => {
    const res = await api.get("/students/me/projects");
    return res.data;
  },
  create: async (data: ProjectCreate): Promise<Project> => {
    const res = await api.post("/students/me/projects", data);
    return res.data;
  },
  update: async (id: number, data: ProjectUpdate): Promise<Project> => {
    const res = await api.put(`/students/me/projects/${id}`, data);
    return res.data;
  },
  remove: async (id: number): Promise<void> => {
    await api.delete(`/students/me/projects/${id}`);
  },
};
