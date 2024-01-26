import datetime

from asyncpg import UniqueViolationError

from core.utils.db_postgres_api.db_telegram import db
from core.utils.db_postgres_api.schemas.user import User


async def add_user(user_id: int, name: str, update_name: datetime):
    try:
        user = User(user_id=user_id, name=name, update_name=update_name)
        await user.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def update_user_name(user_id, new_user_name: str):
    # user = await User.get(user_id)
    # или
    user = await select_user(user_id)
    return user.update(update_name=new_user_name).apply()


# async def select_user(user_id):
#     user = await User.query.where(User.user_id == user_id).gino.first()
#     return user
