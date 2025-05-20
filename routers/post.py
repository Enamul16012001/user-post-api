import schemas, models, oauth2
from fastapi import HTTPException, status, APIRouter, Depends
from typing import List, Optional
from sqlmodel import Session
from typing import Annotated
from db import get_db
from sqlalchemy import or_


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), search: Optional[str] = ""):
    posts = db.query(models.Post).filter(
        or_(
            models.Post.title.contains(search),
            models.Post.content.contains(search)
        )
    ).all()
    return posts


@router.get("/{id}", response_model=schemas.Post)
def get_post_by_id(id: int, db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).filter(models.Post.id==id).first()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post:schemas.PostCreate, db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete("/{id}")
def delete_posts(id:int, db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id==id)
    post = post_query.first()

    if post_query == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()

    return post

@router.put("/{id}")
def update_post(id: int, updated_post: schemas.PostUpdate, db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.update(updated_post.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return post
