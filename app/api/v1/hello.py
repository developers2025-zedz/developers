from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class UserData(BaseModel):
    name: str
    phone: str


@router.get("/hello")
async def say_hello():
    return {"message": "Hello, world!"}


@router.post("/create_user")
async def create_user(data: UserData):
    return data
