from server import app
from configs.setting import Settings
import uvicorn

settings = Settings()

if __name__ == "__main__":
    uvicorn.run("run:app", host=settings._host, port=settings._port,
                debug=settings._isdebug, reload=settings._isreload)
