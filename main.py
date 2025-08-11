from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from database import engine
from database import Base

from routing.check import check_router

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
    
app.include_router(check_router, prefix="/check", tags=["check"])