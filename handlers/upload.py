import shutil
from typing import List
from fastapi import FastAPI, File, UploadFile, APIRouter
import os
import uuid
import aiofiles
import aiofiles.os as aios

router = APIRouter()

@router.post("/upload")
async def create_upload_file(uploaded_file: UploadFile = File(...)):    
    filename, file_extension = os.path.splitext(uploaded_file.filename)
    file_location = f"uploads/{uuid.uuid1()}{file_extension}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(uploaded_file.file, file_object)    
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}

