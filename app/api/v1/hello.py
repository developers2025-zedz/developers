from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def ok():
    return {"message": "ok"}


@router.get("/hello")
async def say_hello():
    return {"message": "Hello, world!"}
