from fastapi import FastAPI
from sqlmodel import SQLModel

from dbconnect import engine
from routers import database_operation, weblink


app=FastAPI()
app.include_router(database_operation.router)
app.include_router(weblink.router)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


