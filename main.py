from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib import fastapi
# from starlette.middleware.sessions import SessionMiddleware
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


from src.config import settings
# from src.app import routers
import logging
fastapi.logging = logging.getLogger('uvicorn')

app = FastAPI(
    title="Useful",
    description="Author - DJWOMS",
    version="0.2.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
# app.include_router(routers.api_router, prefix=settings.API_V1_STR)
db_config = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": 'fastapicore',
                "host": 'postgresdb',
                "password": 'newpassword',
                "port": '5432',
                "user": 'sakthi',
            },
        }
    },
    "apps": {
        "models": {
            "models": settings.APPS_MODELS,
            "default_connection": "default",
        }

    },
    "generate_schemas":False,
    "add_exception_handlers":True,
}

register_tortoise(app, config=db_config)
