from fastapi import Depends, FastAPI
from sqlmodel import Field, Session, create_engine
from typing import Annotated
from db import engine, Base
from routers import post, user, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Post API!"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


'''
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

'''