from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from uuid import uuid4
from random import randint

from config.db import db
collection = db.products

router = APIRouter(
    prefix = '/api/products',
    tags = ['Products']
)

class ShowProduct(BaseModel):
    name: str
    type: str
    price: float
    description: str
    thumbnail: str
    upc: str

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

@router.post("/", status_code=201)
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
    try: 
        await collection.insert_one(product)
        return {"detail": "Product Created Successfully"}
    except Exception as e:
        raise HTTPException(status_code=500) from e
    
@router.get("/")
async def get_all_products():
    products = await collection.find().to_list(None)
    if not products:
        raise HTTPException(status_code=404, detail="No Products Found")
    return products

@router.get("/{item_id}", response_model=ShowProduct)
async def get_product_by_id(item_id):
    product = await collection.find_one({"_id": item_id})
    if not product:
        raise HTTPException(status_code=404, detail="No Product Found")
    return product

@router.get("/generate_upc/")
async def generate_new_upc():
    upc_size = 13
    return str(random_with_N_digits(upc_size))

@router.put("/{item_id}", status_code=201)
async def update_product_by_id(item_id, new_product: ShowProduct):
    product = {
        "name": new_product.name,
        "type": new_product.type,
        "price": new_product.price,
        "description": new_product.description,
        "thumbnail": new_product.thumbnail,
        "upc": new_product.upc
    }
    result = await collection.update_one({"_id": item_id}, {"$set": product})
    if not result.modified_count:
        raise HTTPException(status_code=404, detail=f"Product with ID: {item_id} was not updated")
    return {"detail": "Product Updated Successfully"}

@router.delete("/{item_id}", status_code=202)
async def delete_product_by_id(item_id):
    result = await collection.delete_one({"_id": item_id})
    if not result.deleted_count:
        raise HTTPException(status_code=204, detail=f"Product with ID: {item_id} was not deleted")
    return {"detail": "Product Deleted Successfully"}