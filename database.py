import platform
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Importe todos os seus modelos para que o Base.metadata os reconheça
import models as model

DB_URL = 'postgresql://admin:admin@localhost/littletomy01'

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    model.Base.metadata.create_all(bind=engine)
    print("Tabelas criadas")

# Exemplo de como você chamaria isso em um ponto de entrada:
if __name__ == "__main__":
    create_tables()