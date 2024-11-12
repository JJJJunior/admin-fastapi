from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserResponse
from typing import List
from models.user import Users

router = APIRouter()


# 创建用户
@router.post("/users", response_model=UserResponse)
async def create_users(user: UserCreate):
    existing_user = await Users.get(username=user.username)
    if existing_user:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="User already exists")
    user_obj = await Users.create(**user.dict())
    return {"status_code": HTTPStatus.CREATED, "data": user_obj}


# 列出所有用户
@router.get("/users", response_model=List[UserResponse])
async def list_users():
    users = await Users.all()  # 直接获取模型对象
    return users  # 返回模型对象列表，FastAPI 会自动应用 Pydantic 的 from_attributes
