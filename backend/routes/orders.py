from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from datetime import datetime

from config.db import db
collection = db.orders

router = APIRouter(
    prefix = '/api/orders',
    tags = ['Orders']
)

@router.get('/')
async def get_orders():
    orders = await collection.find().to_list(None)
    if not orders:
        raise HTTPException(status_code=404, detail="No Orders Found")
    return orders

@router.post('/', status_code=201)
async def add_order(products: List[dict]):
    order = {
        "_id": str(uuid4()),
        "products": products,
        "date_created": str(datetime.now())
    }
    try:
        await collection.insert_one(order)
        return {"detail": "Product Updated Successfully"}
    except Exception as e:
        raise HTTPException(status_code=500)
