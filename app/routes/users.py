from fastapi import APIRouter, Depends
from app.models.models import User

router = APIRouter()


@router.post("/user")
def age_check(user: User):
    return {"name": user.name, "age": user.age, "is_adult": user.age >= 18}