from .schemas import UserCreate, UserLogin
from ...dependencies import SessionDep as session
from .models import User
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import bcrypt


# Function to hash the password
async def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


async def create_user(user_data:UserCreate, session: AsyncSession) -> User:
    # Check whether username already exists then raise the exception
    query = select(User).where(User.username == user_data.username)
    result = await session.execute(query)
    existing_user = result.scalars().first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists. Please choose another username."
        )
    else:
        user= User(**user_data.dict())
        user.hashed_password= await hash_password(user.hashed_password)
        session.add(user)

        await session.commit()

        await session.refresh(user)
        return user

async def authenticate_user(userlogin:UserLogin, session: AsyncSession):
    query = select(User).where(User.username == userlogin.username)
    result = await session.execute(query)
    user= result.scalars().first()
    if user and bcrypt.checkpw(userlogin.hashed_password.encode("utf-8"), user.hashed_password.encode("utf-8")):
        return {"ID":user.id, "User name":user.username}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")


