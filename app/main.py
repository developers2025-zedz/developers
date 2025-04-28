import uvicorn
from fastapi import FastAPI
from app.api.v1.hello import router as hello_router

app = FastAPI(title="FastAPI Docker Example", docs_url="/")
app.include_router(hello_router, prefix="/api/v1")
