import api from "./client";
import type { User, TokenResponse, LoginPayload, RegisterPayload } from "@/types";

export const authApi = {
  login: async (data: LoginPayload): Promise<TokenResponse> => {
    const res = await api.post("/auth/login", data);
    return res.data;
  },
  register: async (data: RegisterPayload): Promise<User> => {
    const res = await api.post("/auth/register", data);
    return res.data;
  },
  getMe: async (): Promise<User> => {
    const res = await api.get("/auth/me");
    return res.data;
  },
};
