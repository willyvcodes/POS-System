from fastapi import APIRouter
from routes import products

main_router = APIRouter()

main_router.include_router(products.router)