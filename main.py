from fastapi import FastAPI
from fastapi.routing import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class FastAPIConfig(BaseModel):
    title: str = "Starlette Test"
    description: str = "FastAPI App to test starlette bug"
    version: str = "0.1.0"
    root_path: str = "/star"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"


app = FastAPI(**FastAPIConfig().model_dump())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["be.faizanazim11.codes"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"],
    allow_headers=["Access-Control-Allow-Headers", "Content-Type", "Authorization", "Access-Control-Allow-Origin"],
    allow_credentials=True,
)

router = APIRouter(prefix="/star")

@router.get("/hello")
def hello_world():
    return "Hello World"

app.include_router(router)
