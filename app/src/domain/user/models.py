from pydantic import EmailStr
from sqlalchemy import Column, Integer, String
from app.src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username= Column(String, index=True)
    hashed_password= Column(String)
    email= Column(String,default=None)