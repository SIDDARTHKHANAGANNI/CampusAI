import api from "./client";
import type { StudentProfile, StudentCreate, StudentUpdate, Student } from "@/types";

export const studentApi = {
  getProfile: async (): Promise<StudentProfile> => {
    const res = await api.get("/students/me/profile");
    return res.data;
  },
  createProfile: async (data: StudentCreate): Promise<Student> => {
    const res = await api.post("/students/me/profile", data);
    return res.data;
  },
  updateProfile: async (data: StudentUpdate): Promise<Student> => {
    const res = await api.put("/students/me/profile", data);
    return res.data;
  },
};
