import api from "./client";
import type { CareerGoal, CareerGoalCreate, CareerGoalUpdate } from "@/types";

export const careerGoalsApi = {
  getAll: async (): Promise<CareerGoal[]> => {
    const res = await api.get("/students/me/career-goals");
    return res.data;
  },
  create: async (data: CareerGoalCreate): Promise<CareerGoal> => {
    const res = await api.post("/students/me/career-goals", data);
    return res.data;
  },
  update: async (id: number, data: CareerGoalUpdate): Promise<CareerGoal> => {
    const res = await api.put(`/students/me/career-goals/${id}`, data);
    return res.data;
  },
  remove: async (id: number): Promise<void> => {
    await api.delete(`/students/me/career-goals/${id}`);
  },
};
