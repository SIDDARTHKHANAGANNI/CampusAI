from pydantic import BaseModel, ConfigDict, EmailStr, Field


# Data required when a new user registers
class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=128
    )


# Data required when a user logs in
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Safe user information returned by the API
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


# JWT token returned after successful login
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"