import schemas, models, utils
from fastapi import HTTPException, status, APIRouter, Depends
from typing import List
from sqlmodel import Session
from typing import Annotated
from db import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.get("/", response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}", response_model=schemas.UserOut)
def get_posts(id: int, db: Session = Depends(get_db)):
    posts = db.query(models.User).filter(models.User.id==id).first()
    return posts

@router.post("/", response_model=schemas.UserOut)
def create_users(user:schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user