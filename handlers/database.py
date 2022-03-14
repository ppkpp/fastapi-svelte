from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configs.setting import Settings
settings = Settings()

engine = create_engine(settings._DATABASE_URL, connect_args={
                       "check_same_thread": False})
#engine = create_engine(settings._DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
