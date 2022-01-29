import asyncio
from typing import Optional
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from src.db.services import initialize_storage
from src.api.update import get_updates
from src.api.group import get_groups

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await initialize_storage()


@app.get("/")
async def main_page():
    return FileResponse('src/static/index.html')


@app.get("/ping")
async def test_connection():
    return {"result": "true"}


@app.get("/update")
async def get_update(
    last: Optional[bool] = Query(
        None,
        description="If enable - you will get the last update information." +
                    "<br>If not - you will get all update information.")
):
    return await get_updates(last)


@app.get("/groups")
async def groups(
    list_of_names: Optional[bool] = Query(
        None,
        description="If enable - " +
                    "you will get the list of names of all groups."),
    name: Optional[str] = Query(
        None,
        description="Name of group, that you want to get. Example - 0432-06")
):
    return await get_groups(list_of_names, name)
