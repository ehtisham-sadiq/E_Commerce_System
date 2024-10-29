from .schemas import UserCreate, UserLogin, UserOut
from .models import User
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import bcrypt
import datetime
from dotenv import load_dotenv
import os
import jwt


load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY= os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

# Function to hash the password
async def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def create_access_token(data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


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
        user.password= await hash_password(user.password)
        session.add(user)

        await session.commit()

        await session.refresh(user)
        return user.username

async def authenticate_user(userlogin:UserLogin, session: AsyncSession):

    query = select(User).where(User.username == userlogin.username)
    result = await session.execute(query)
    user= result.scalars().first()
    if user and bcrypt.checkpw(userlogin.password.encode("utf-8"), user.password.encode("utf-8")):
        token = create_access_token(data={"sub": user.username})
        return {"username": user.username, "token": token}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    

async def get_by_token(token: str, session: AsyncSession):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError as e:
        raise credentials_exception
    query = select(User).where(User.username == username)
    result = await session.execute(query)
    user= result.scalars().first()
    if not user:
        raise credentials_exception
    return UserOut(id=user.id,  username=user.username, email=user.email)



