from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.logger import logger
from typing import List, Dict
from .database import get_db
from sqlalchemy.orm import Session
from models.schema import TodoSchema,CreateTodoSchema,UpdateTodoSchema
from models.model import Todo
router = APIRouter()


@router.get("/todos",response_model=List[TodoSchema])
async def get_todo(db: Session=Depends(get_db)):
    predict_logs =  db.query(Todo).all()
    return predict_logs

@router.post('/todos')
async def add_todo(todo: CreateTodoSchema,db: Session = Depends(get_db)):
    db_todo = Todo(title=todo.title,is_done=todo.is_done)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.put("/todos/{id}", response_model=CreateTodoSchema)
async def update_todo(id: int,todo: UpdateTodoSchema, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).get(id)
    if not db_todo:
        raise HTTPException(status_code=404, detail=" ID not found.")
    #db_todo.title = todo.name
    db_todo.is_done = todo.is_done
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.delete("/todos/{id}")
async def delete_course(id: int,db: Session = Depends(get_db)):
    db.query(Todo).filter_by(id=id).delete()
    db.commit()
    return  {"message": "deleted succesfully"}