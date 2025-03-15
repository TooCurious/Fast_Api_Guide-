import uvicorn

from fastapi import FastAPI
from app.routes.users import router as users_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["Users"])

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8066, reload=True, workers=3)