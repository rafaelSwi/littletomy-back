from fastapi import APIRouter, Response, Depends, status, HTTPException
from schemas.user import UserCreate, UserPublic
from crud.user import create_user, check_user_existence, get_user_by_id
from typing import Annotated
from sqlalchemy.orm import Session
from models import User
from database import get_db

user_router = APIRouter()


@user_router.post(
    "",
    response_model=UserPublic,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo usuário",
    description="Cria um novo usuário no sistema, verificando a duplicidade de username e email.",
)
def create_new_user(
    user_data: UserCreate,
    db: Annotated[Session, Depends(get_db)],
):
    if check_user_existence(db, user_data.username, user_data.email_address):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already registered"
        )
    
    return create_user(db=db, user_data=user_data)
