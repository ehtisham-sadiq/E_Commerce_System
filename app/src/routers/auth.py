from fastapi import APIRouter
from ..domain.user.schemas import UserCreate, UserLogin
from ..dependencies import SessionDep
from ..domain.user.schemas import UserCreate
from ..domain.user.service import create_user, authenticate_user
from sqlalchemy.ext.asyncio import AsyncSession

router=APIRouter()


@router.post("/login")
async def user_login(user:UserLogin,session:SessionDep):
    return await authenticate_user(user,session)


@router.post("/register")
async def user(user:UserCreate, session:SessionDep):
    return  await create_user(user,session)


@router.get("/token")
async def get_user_by_token():
    return {"message": "This endpoint could return a user detail after decoding the token."}