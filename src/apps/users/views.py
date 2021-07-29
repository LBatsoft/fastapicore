from .models import *
from .schema import *
from fastapi import APIRouter,Depends
from typing import List
from fastapi import HTTPException
from pydantic import BaseModel
from .service import *
from src.apps.auth.security import get_password_hash,verify_password
user_router = APIRouter()
@user_router.get('/users')
async def get_all_users():
    return await user_service.all()


@user_router.get('/printusers')
async def get_all_users() -> None:
    users = User.all()
    async for user in users:
        print(user.username)
    user =await User.first()
    print(user.username)
    return None


@user_router.post("/signup", response_model=UserIn_Pydantic)
async def create_user(user: User_Pydantic):
    return await user_service.create_user(user)

async def something_print():
    print("awefawfawef")
    return  "awfawefawef"
