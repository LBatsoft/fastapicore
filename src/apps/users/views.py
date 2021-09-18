import uuid
from fastapi import APIRouter, Depends, BackgroundTasks, Response, status, Request
from typing import List
from fastapi import HTTPException
from pydantic import BaseModel
from .service import *
from tortoise.query_utils import Q
from src.apps.auth.security import get_password_hash,verify_password
from src.apps.auth.permissions import get_user
from src.apps.auth.models import Verification
from .models import *
from .schema import *
from starlette.responses import JSONResponse
# from starlette.requests import Request
from src.apps.auth.send_email import *
from src.apps.auth.schema import VerificationOut
user_router = APIRouter()
@user_router.get('/users')
async def get_all_users():
    return await user_service.all()


@user_router.get('/verify')
async def verify_user(token: uuid.UUID):
    obj = await Verification.get(link=token.link).prefetch_related('user')
    if obj:
        user = await User.get(id=obj.user.id)
        user.is_active = True
        user.save()
        await Verification.get(link=token.link).delete()
        return JSONResponse({"SUCCESS: ACTIVATED"},status_code=200)
    return JSONResponse({"error":"link is not avaialable"},status_code=500)
    
    


@user_router.get('/printusers')
async def get_all_users() -> None:
    users = User.all()
    async for user in users:
        print(user.username)
    user =await User.first()
    print(user.username)
    return None


@user_router.post("/signup", response_model=UserIn_Pydantic)
async def create_user(user: User_Pydantic,tasks:BackgroundTasks,response:Response):
    if await User.filter(Q(username=user.username)|Q(email=user.email)).exists():
        user = await User.filter(Q(username=user.username) | Q(email=user.email)).first()
        if  user.is_active:
            return JSONResponse({"error":"user already exists"},status_code=500)
        verification_link = await Verification.create(user=user)
        tasks.add_task(
            send_account_activate, user.email, user.username, user.password, verification_link.link
        )
        return JSONResponse({"res": "underprocesss"}, status_code=201)
    user_create = await user_service.create_user(user)
    user_obj = await User.get(username=user.username)
    verification_link =await Verification.create(user=user_obj)
    tasks.add_task(
        send_account_activate, user.email, user.username, user.password, verification_link.link
    )
    return JSONResponse({"res":"underprocesss"},status_code=201)
    


async def something_print():
    print("awefawfawef")
    return  "awfawefawef"

@user_router.get('/playrequest/{item}')
def play_request(request: Request,item:int):
    print(request)
    print(request.query_params)
    print(request.path_params)
    print(request.query_params['path'])




async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@user_router.get('/checkdepends')
async def get_depends(commons:dict = Depends(common_parameters)) -> dict:
    return commons


@user_router.get('/authtoken')
async def get_depends(user:User = Depends(get_user)):
    return await User_Pydantic.from_tortoise_orm(user)
