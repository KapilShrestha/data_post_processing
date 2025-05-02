# app/api/routes/__init__.py

from fastapi import APIRouter
from .concat import router as concat_router
from .merge import router as merge_router
from .home import router as home_router

router = APIRouter() 

router.include_router(concat_router) 
router.include_router(merge_router)  
router.include_router(home_router)
