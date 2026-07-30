import api from "./client";
import type { AcademicRecord, AcademicCreate, AcademicUpdate } from "@/types";

export const academicsApi = {
  getAll: async (): Promise<AcademicRecord[]> => {
    const res = await api.get("/students/me/academics");
    return res.data;
  },
  create: async (data: AcademicCreate): Promise<AcademicRecord> => {
    const res = await api.post("/students/me/academics", data);
    return res.data;
  },
  update: async (id: number, data: AcademicUpdate): Promise<AcademicRecord> => {
    const res = await api.put(`/students/me/academics/${id}`, data);
    return res.data;
  },
  remove: async (id: number): Promise<void> => {
    await api.delete(`/students/me/academics/${id}`);
  },
};
