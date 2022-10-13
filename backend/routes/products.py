from fastapi import APIRouter, HTTPException, status
from config.db import db
from uuid import uuid4
from random import randint

router = APIRouter(
    prefix = '/api/products',
    tags = ['Products']
)

collection = db.products

from pydantic import BaseModel
class ShowProduct(BaseModel):
    name: str
    type: str
    price: float
    description: str
    thumbnail: str


# UTILITIES
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# CREATE
@router.post("/")
async def create_product(product: ShowProduct):
    product = {
        "_id": str(uuid4()),
        "name": product.name,
        "type": product.type,
        "price": product.price,
        "description": product.description,
        "thumbnail": product.thumbnail,
        "upc": str(random_with_N_digits(13))
    }
    collection.insert_one(product)
    return {"detail": "Created Successfully"}
    

# READ
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_products():
    products = await collection.find().to_list(None)
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Not Found")
    return products

@router.get("/{item_id}", response_model=ShowProduct, status_code=status.HTTP_200_OK)
async def get_product_by_id(item_id):
    product = await collection.find_one({"_id": item_id})
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Not Found")
    return product

@router.get("/generate_upc/{upc_size}")
async def generate_new_upc(upc_size: int):
    return str(random_with_N_digits(upc_size))

# UPDATE
@router.put("/{item_id}")
async def update_product_by_id(item_id, new_product: ShowProduct):
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