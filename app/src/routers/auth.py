from fastapi import APIRouter
from app.src.dependencies import SessionDep
from app.src.domain.user.schemas import UserCreate
from app.src.domain.user.service import create_user

router=APIRouter()


router.post("/login")


router.post("/register")
create_user()


router.get("/token")