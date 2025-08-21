from encryption.functions import authenticate_user, get_password_hash
from sqlalchemy.orm import Session
from sqlalchemy import or_
from schemas.user import UserCreate, UserPublic, UserUpdate
from typing import List
import models as model


async def get_all_users(db: Session, skip:int=0, limit:int=3_500) -> List[UserPublic]:
    user_list = db.query(model.User).offset(skip).limit(limit).all()
    public_users = []
    for i in user_list:
        public_users.append(i.toPublic())
    return public_users

async def get_user_by_id(db: Session, user_id: int, public: bool = False):
    user = db.query(model.User).filter_by(id=user_id).first()
    if not user:
        return None
    return user.toPublic() if public else user

async def get_user_by_username(db: Session, username: str, public: bool = False):
    user = db.query(model.User).filter_by(username=username).first()
    if not user:
        return None
    return user.toPublic() if public else user

def check_user_existence(db: Session, username: str, email_address: str = None) -> bool:
    if email_address:
        return db.query(model.User).filter(
            or_(model.User.username == username, model.User.email_address == email_address)
        ).scalar() is not None
    else:
        return db.query(model.User).filter(model.User.username == username).scalar() is not None

def create_user(db: Session, user_data: UserCreate) -> UserPublic:
    hashed_password = get_password_hash(user_data.password)
    new_user = model.User(
        username=user_data.username,
        email_address=user_data.email_address,
        password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return get_user_by_id(db=db, user_id=new_user.id, public=True)

def update_user(db: Session, user_id: int, user_data: UserUpdate) -> model.User | None:
    user = db.query(User).filter(model.User.id == user_id).first()
    if not user:
        return None

    if user_data.username is not None:
        user.username = user_data.username
    if user_data.email_address is not None:
        user.email_address = user_data.email_address
    if user_data.password_hash is not None:
        user.password_hash = get_password_hash(user_data.password_hash)

    db.commit()
    db.refresh(user)
    return get_user_by_id(db=db, user_id=user.id, public=True)

def count_user_text_tabs(db: Session, user_id: int) -> int:
    user = db.query(model.User).filter(model.User.id == user_id).first()
    if not user:
        return 0
    return len(user.text_tabs)