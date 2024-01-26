import sqlalchemy as sql
from sqlalchemy import Column, BigInteger, String

from core.utils.db_postgres_api.db_telegram import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(200), primary_key=True)
    update_name = Column(sql.DateTime, primary_key=True)

    query: sql.select
