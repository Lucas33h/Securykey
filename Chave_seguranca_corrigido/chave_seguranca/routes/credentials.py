from fastapi import APIRouter

router = APIRouter()

@router.get("/credentials")
def list_credentials():
    return [
        {"site": "github.com", "usuario": "arthur", "senha": "***"}
    ]
