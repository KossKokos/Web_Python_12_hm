from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas.users import UserModel


async def create_user(body: UserModel, db: Session) -> User:
	user = User(**body.dict())
	db.add(user)
	db.commit()
	db.refresh(user)
	return user


async def get_user_by_email(email: str, db: Session) -> User | None:
	return db.query(User).filter(User.email==email).first()


async def update_token(user: User, refresh_token, db: Session) -> None:
    user.refresh_token = refresh_token
    db.commit()
    db.refresh(user)