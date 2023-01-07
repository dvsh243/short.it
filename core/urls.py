from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core.settings import connect_to_mongo
from app.routers import test, create, redirect, analytics

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    print("[START] Starting FastAPI")

    await connect_to_mongo()


app.include_router( create.router )
app.include_router( redirect.router )
app.include_router( analytics.router )

app.include_router( test.router )