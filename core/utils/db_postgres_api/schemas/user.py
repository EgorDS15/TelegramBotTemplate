import sqlalchemy as sql
from sqlalchemy import Column, String

from core.utils.db_postgres_api.db_telegram import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    # id = Column(BigInteger, primary_key=True)
    user_id = Column(String(30))
    name = Column(String(200), unique=False, nullable=True)
    query = Column(sql.Text)

    query: sql.select
