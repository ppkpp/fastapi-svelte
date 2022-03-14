
from sqlalchemy import ARRAY,Boolean, Column, ForeignKey, Integer, String, DateTime,Table
from sqlalchemy.orm import relationship

from handlers.database import Base
import datetime


class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    is_done = Column(Boolean, unique=False, default=False)
    createdate = Column(DateTime, default=datetime.datetime.now)
