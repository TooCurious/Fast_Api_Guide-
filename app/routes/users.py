from fastapi import APIRouter, Depends
from ..models.models import User

router = APIRouter()


@router.post("/user")
def create_user(user: User):
    if int(user.age) >= 18:
        is_adult = True
    else:
        is_adult = False

    # Возвращаем данные пользователя с дополнительным полем 'is_adult'
    return {
        "data": user.dict(),
        "is_adult": is_adult
    }