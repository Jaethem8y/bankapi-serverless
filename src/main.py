from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from src.db import host, user, password, port, database
from src.controller.api import router as api_router
from src.documentation import description, tags_metadata

import aiomysql

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(
    title="Bank API",
    description=description,
    version="2.0.0",
    openapi_tags=tags_metadata,
    middleware=middleware,
    # root_path="/dev",
    docs_url='/docs',
    # openapi_url='/dev/openapi.json', 
    redoc_url=None
)

@app.on_event("startup")
async def _startup():
    app.state.pool = await aiomysql.create_pool(host=host, port=port, user=user, password=password, db=database)
    print("startup done")

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.pool = app.state.pool
    response = await call_next(request)
    return response

@app.get(path="/", tags=["useless_intro"])
async def getIndex(request:Request):
  return "Bank API Resource"

app.include_router(api_router)
handler = Mangum(app)
