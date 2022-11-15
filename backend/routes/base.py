from fastapi import APIRouter
from routes import products, stripe, orders, users

main_router = APIRouter()

main_router.include_router(products.router)
main_router.include_router(stripe.router)
main_router.include_router(orders.router)
main_router.include_router(users.router)