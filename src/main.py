from typing import Optional
from fastapi import FastAPI, Query, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from src.db.services import initialize_storage
from src.api.update import get_updates
from src.api.group import get_groups
from src.cron import run_cron

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
    await run_cron()


@app.get("/")
@limiter.limit("5/second")
async def main_page(request: Request, response: Response):
    return FileResponse('src/static/index.html')


@app.get("/ping")
@limiter.limit("5/second")
async def test_connection(request: Request, response: Response):
    return {"result": "true"}


@app.get("/update")
@limiter.limit("5/second")
async def get_update(
    request: Request,
    response: Response,
    last: Optional[bool] = Query(
        None,
        description="If enable - you will get the last update information." +
        "<br>If not - you will get all update information.")):
    return await get_updates(last)


@app.get("/groups")
@limiter.limit("5/second")
async def groups(request: Request,
                 response: Response,
                 list_of_names: Optional[str] = Query(
                     None,
                     enum=["list", "structure"],
                     description="list - you will get list of groups" +
                     "<br> structure - you will get structure of groups"),
                 name: Optional[str] = Query(
                     None,
                     description="Name of group, that you want to get." +
                     " Example - 0431-06" +
                     "<br> all - you will get all groups with details.")):
    return await get_groups(list_of_names, name)
