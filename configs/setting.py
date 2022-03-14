from typing import List
from pydantic import BaseSettings


class Settings(BaseSettings):
    #_dbuser = "pkuser"
    #_dbpass = "pkpass"
    #_dbhost = "192.168.1.28"
    #_dbport = "5432"
    #_DATABASE_URL = f"postgresql://{_dbuser}:{_dbpass }@{_dbhost}:{_dbport}/dhnbapp"
    _DATABASE_URL = 'sqlite:///data.db'
    _host = "0.0.0.0"
    _port = 8000
    _isdebug = True
    _isreload = False
    SECRET_KEY: str = "pk!@#$#@!"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 600000000
    headers = {"charset": "utf-8", "Content-Type": "application/json"}

