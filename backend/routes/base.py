from fastapi import APIRouter
from routes import products, stripe

main_router = APIRouter()

main_router.include_router(products.router)
main_router.include_router(stripe.router)