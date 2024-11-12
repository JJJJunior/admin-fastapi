from fastapi import FastAPI
from dotenv import load_dotenv
from tortoise import Tortoise
import os
from routers import user, upload

# 读取配置文件
load_dotenv()
# 初始化api
app = FastAPI()


async def init_db():
    await Tortoise.init(
        db_url=f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}",
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()


@app.get("/")
async def root():
    return {"message": "Server is running..."}


@app.on_event("startup")
async def startup():
    await init_db()


@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()


app.include_router(user.router, prefix="/api")
app.include_router(upload.router, prefix="/api")
