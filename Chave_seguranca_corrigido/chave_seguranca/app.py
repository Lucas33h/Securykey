from fastapi import FastAPI
from routes import users, credentials
from database import Base, engine

app = FastAPI(title="Chave de Segurança")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(credentials.router)
