from fastapi import APIRouter

from app.routes.user import user_router
from app.routes.horoscope import horoscope_router

router = APIRouter(prefix="/api/v1")

router.include_router(user_router)
router.include_router(horoscope_router)
