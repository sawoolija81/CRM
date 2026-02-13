from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_user():
    return [{"id": 1, "name": "Alex"},{"id": 2, "name": "Bodya"}]