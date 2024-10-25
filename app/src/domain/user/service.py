from schemas import UserCreate, UserLogin
from app.src.dependencies import SessionDep
from app.src.database import engine
from sqlmodel import SQLModel, select
from app.src.domain.user.models import User
from fastapi import HTTPException, status

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


#session=SessionDep
async def create_user(user:UserCreate, session:SessionDep):
    async with session:
        query = select(User).where(User.username == user.username)
        existing_user = await session.exec(query)
        user_found = existing_user.first()
        if user_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username  already exists")
        new_user = User(username=user.username, hashed_password= user.password, email=user.email)
        session.add(new_user)

        await session.commit()

        await session.refresh(new_user)
    return new_user

async def authenticate_user(userlogin:UserLogin, session:SessionDep):
    async with session:
        query = select(User).where(User.username == userlogin.username & User.hashed_password==userlogin.password)
        result = await session.exec(query)
        user= result.first()
        if user:
            return {"message": "user validated"}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")


