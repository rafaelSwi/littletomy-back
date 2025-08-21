from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from database import engine
from database import Base
from database import create_tables

from routing.check import check_router
from routing.user import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "Teste de API"}
    
app.include_router(check_router, prefix="/api/check", tags=["api", "check"])
app.include_router(user_router, prefix="/api/user", tags=["api", "user"])

create_tables()