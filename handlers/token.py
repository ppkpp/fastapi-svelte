from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/login/token")
async def read_tokens(token: str = Depends(oauth2_scheme)):
    return {"token": token}
