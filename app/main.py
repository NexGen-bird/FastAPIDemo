from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.auth import login_user, signup_user

app = FastAPI()

class UserCredentials(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(credentials: UserCredentials):
    result = login_user(credentials.email, credentials.password)
    if "error" in result:
        raise HTTPException(status_code=401, detail=result["error"])
    return {"message": "Login successful", "data": result}

# @app.post("/signup")
# def signup(credentials: UserCredentials):
#     result = signup_user(credentials.email, credentials.password)
#     if "error" in result:
#         raise HTTPException(status_code=400, detail=result["error"])
#     return {"message": "Signup successful", "data": result}
