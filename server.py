from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.logger import logger
import logging
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os.path as op
import datetime

def create_app():
    app = FastAPI()
    origins = ["http://localhost:8000","localhost:8000","http://localhost:8080","localhost:8080"]
    app.add_middleware(CORSMiddleware,
                       allow_origins=origins,
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"])
                       
    from handlers.database import SessionLocal, engine
    import models.model as app_model
    app_model.Base.metadata.create_all(bind=engine)
    from modules.dependency import is_auth
    from handlers import todo
    app.include_router(todo.router, dependencies=[Depends(is_auth)])
    logging.basicConfig(
        format='Server:{levelname:7} {message}', style='{', level=logging.DEBUG)
    
    app.mount("/public", StaticFiles(directory="client/public"), name="public")
    app.mount("/build", StaticFiles(directory="client/public/build"), name="build")
    #app.mount("/assets", StaticFiles(directory="client/public/assets"), name="assets")

    @app.get('/{full_path:path}')
    def getSPA():
        with open('client/public/index.html', 'r') as file_index:
            html_content = file_index.read()
        return HTMLResponse(html_content, status_code=200)

    return app

app = create_app()

