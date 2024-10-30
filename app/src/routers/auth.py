from fastapi import APIRouter, Depends, HTTPException, status
from ..domain.users.schemas import UserCreate, UserLogin
from ..dependencies import SessionDep
from ..domain.users.schemas import UserCreate
from ..domain.users.service import create_user, authenticate_user, get_by_token
from fastapi.security import OAuth2PasswordBearer

router=APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/login")
async def user_login(user:UserLogin,session:SessionDep):
    try:
        result = await authenticate_user(user, session)
        return result
    except HTTPException as e:
        raise e
    #return await authenticate_user(user,session)


@router.post("/register")
async def user(user:UserCreate, session:SessionDep):
    try:
        result = await create_user(user, session)
        return result
    except HTTPException as e:
        raise e
    #return  await create_user(user,session)


@router.get("/token")
async def get_user_by_token(session: SessionDep,token:str = Depends(oauth2_scheme)):
    user_info= await get_by_token(token, session)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")
    return user_info