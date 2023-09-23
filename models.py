from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from datetime import datetime

Base = declarative_base()


class Board(Base):
    __tablename__ = 'board'
    id: int = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name: str = sqlalchemy.Column(sqlalchemy.String(64))
    created_time: datetime = sqlalchemy.Column(sqlalchemy.DATETIME)