from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    hashed_password: str
    email: Optional[EmailStr] = None
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    hashed_password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr]


