from .schemas import UserCreate, UserLogin
from ...dependencies import SessionDep as session
from .models import User
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def create_user(user_data:UserCreate, session: AsyncSession) -> User:
    user= User(**user_data.dict())
    session.add(user)

    await session.commit()

    await session.refresh(user)
    return user

async def authenticate_user(userlogin:UserLogin, session: AsyncSession):
    query = select(User).where(User.username == userlogin.username , User.hashed_password==userlogin.hashed_password)
    result = await session.execute(query)
    return result.scalars().all()


