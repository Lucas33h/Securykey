from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal
from models import User
from auth import hash_password, verify_password, create_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(email: str, password: str, db=Depends(get_db)):
    if db.query(User).filter_by(email=email).first():
        raise HTTPException(400, "Email já cadastrado")

    user = User(email=email, password_hash=hash_password(password))
    db.add(user)
    db.commit()
    return {"message": "Usuário criado com sucesso"}

@router.post("/login")
def login(email: str, password: str, db=Depends(get_db)):
    user = db.query(User).filter_by(email=email).first()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(401, "Credenciais inválidas")

    token = create_token(user.id)
    return {"token": token}
