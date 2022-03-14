from datetime import datetime,date
from uuid import UUID
from typing import List, Optional,Any
from pydantic import BaseModel,validator
from sqlalchemy.orm import Query


class TodoSchema(BaseModel):
    id : int
    title : str
    is_done: Optional[bool] = False
    createdate : datetime
    class Config:
        orm_mode = True

class CreateTodoSchema(BaseModel):
    title : str
    is_done: Optional[bool] = False
    class Config:
        orm_mode = True

class UpdateTodoSchema(BaseModel):
    id : int
    is_done: Optional[bool] = False
    class Config:
        orm_mode = True