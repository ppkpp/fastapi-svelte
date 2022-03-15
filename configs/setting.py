from typing import List
from pydantic import BaseSettings


class Settings(BaseSettings):
    _dbuser = "postgres"
    _dbpass = "pkpass"
    _dbhost = "172.17.0.2"
    _dbport = "5432"
    _DATABASE_URL = f"postgresql://{_dbuser}:{_dbpass }@{_dbhost}:{_dbport}/pkapp"
    #_DATABASE_URL = 'sqlite:///data.db'
    _host = "0.0.0.0"
    _port = 8000
    _isdebug = True
    _isreload = False
    SECRET_KEY: str = "pk!@#$#@!"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 600000000
    headers = {"charset": "utf-8", "Content-Type": "application/json"}

    MESSAGE_STREAM_DELAY = 1  # second
    MESSAGE_STREAM_RETRY_TIMEOUT = 15000 

