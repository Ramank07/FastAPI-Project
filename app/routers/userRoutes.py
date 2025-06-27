from fastapi import FastAPI, Response, status, HTTPException,Depends,APIRouter
from typing import Optional,List
from ..database import engine, get_db
from .. import models,schemas
from sqlalchemy.orm import Session

router=APIRouter(
    prefix='/user/post',
    tags=["User"]
)

# Get all User

@router.get('/',response_model=List[schemas.Postresponse])
def get_post(db: Session= Depends(get_db)):
    all_posts=db.query(models.Post).all()
    return all_posts



# Create User

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.Postresponse)
def create_post(post:schemas.UserPost,db: Session= Depends(get_db)):
    # find_user=db.query(models.Post).filter(models.Post.email==post.email).first()
    # if find_user:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User Already exist of {post.email} email")
    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



# Get one particular user by passing emai as Path parameter

@router.get('/{email}',response_model=List[schemas.Postresponse])
def get_one_detail(email:str, db: Session=Depends(get_db)):
    single_detail=db.query(models.Post).filter(models.Post.email==email).all()
    if not single_detail :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No user found of email: {email}")
    return single_detail



# update one user by passing email in path parameter

@router.put('/{id}',response_model=schemas.UpdatePostResponse)
def update_post(id:int,updated_detail:schemas.UpdatePost, db: Session=Depends(get_db)):
    find_user=db.query(models.Post).filter(models.Post.id==id)
    updated_post=find_user.first()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No user found of id: {id}")
    find_user.update(updated_detail.dict(),synchronize_session=False)
    db.commit()
    return find_user.first()



# Deleting one particular user by passing email in path parameter

@router.delete('/{id}',response_model=schemas.Postresponse)
def delete_post(id:int, db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)

    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'item {id} already deleted or not found')
    

    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)