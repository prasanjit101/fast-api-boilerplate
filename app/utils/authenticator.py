# this is a sample file which can be used to create the authenticator middleware

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from starlette.status import HTTP_401_UNAUTHORIZED
from starlette.requests import Request
from typing import Optional

app = FastAPI()
security = HTTPBearer()

# Example secret key, you should replace it with your own secret key
SECRET_KEY = "your-secret-key"

# Example list of authorized users, you should replace it with your own user database or storage
AUTHORIZED_USERS = {
    "user1": "password1",
    "user2": "password2"
}

# Custom authentication middleware
async def authenticate(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> Optional[str]:
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        
        if username not in AUTHORIZED_USERS:
            raise JWTError("Invalid token")
        
        # Authentication successful
        return username
    
    except JWTError:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Define your API routes
# @app.get("/")
# async def read_root(username: Optional[str] = Depends(authenticate)):
#     return {"message": f"Hello, {username}!"}
