from fastapi import APIRouter, HTTPException, status
from config.db import db
from uuid import uuid4

router = APIRouter(
    prefix = '/api/products',
    tags = ['Products']
)

collection = db.products

from pydantic import BaseModel
class Product(BaseModel):
    name: str
    type: str
    price: float
    description: str
    thumbnail: str

# CREATE
@router.post("/")
async def create_product(product: Product):
    product = {
        "_id": str(uuid4()),
        "name": product.name,
        "type": product.type,
        "price": product.price,
        "description": product.description,
        "thumbnail": product.thumbnail
    }
    collection.insert_one(product)
    

# READ
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_products():
    products = await collection.find().to_list(None)
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Not Found")
    return products

@router.get("/{item_id}")
async def get_product_by_id(item_id):
    product = await collection.find_one({"_id": item_id})
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Not Found")
    return product

# UPDATE
@router.put("/{item_id}")
async def update_product_by_id(item_id, new_product: Product):
    product = {
        "name": new_product.name,
        "type": new_product.type,
        "price": new_product.price,
        "description": new_product.description,
        "thumnail": new_product.thumbnail
    }
    result = await collection.update_one({"_id": item_id}, {"$set": product})
    if not result.modified_count:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"Product with ID: {item_id} was not updated")
    return {"detail": "Updated Successfully"}

# DELETE
@router.delete("/{item_id}")
async def delete_product_by_id(item_id):
    result = await collection.delete_one({"_id": item_id})
    if not result.deleted_count:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"Product with ID: {item_id} was not deleted")
    return {"detail": "Deleted Successfully"}