from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

from uuid import uuid4
from datetime import datetime

# for password hash validation
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash(password: str):
    return pwd_context.hash(password)

def verify(password, hashed_password):
    return pwd_context.verify(password, hashed_password)
# #################################################################

from config.db import db
collection = db.users
router = APIRouter(
    prefix = '/api/users',
    tags = ['Users']
)

class User(BaseModel):
    full_name: str
    username: str
    password: str

class LoginUser(BaseModel):
    username: str
    password: str

@router.post("/", status_code=201)
async def create_user(user: User):
    # hash the password
    hashed_password = hash(user.password)
    # by default the acccount is set not to admin level
    new_user = {
        "_id": str(uuid4()),
        "full_name": user.full_name,
        "username": user.username,
        "password": hashed_password,
        "date_created": str(datetime.now()),
        "is_admin": False
    }

    try: 
        await collection.insert_one(new_user)
        return {"detail": "User Created Successfully"}
    except Exception as e:
        raise HTTPException(status_code=500) from e
    
# @router.get("/")
# async def get_all_users():
#     users = await collection.find().to_list(None)
#     if not users:
#         raise HTTPException(status_code=404, detail="No Users Found")
#     return users

@router.get("/{username}", response_model=User)
async def get_user_by_username(username: str):
    user = await collection.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=404, detail="No User Found")
    return user

# @router.delete("/{user_id}", status_code=202)
# async def delete_user_by_id(user_id: str):
#     result = await collection.delete_one({"_id": user_id})
#     if not result.deleted_count:
#         raise HTTPException(status_code=204, detail=f"User with ID: {user_id} was not deleted")
#     return {"detail": "User Deleted Successfully"}

@router.post("/login")
async def login_user(user_info: LoginUser):
    user =  await get_user_by_username(user_info.username)
    verify_password = verify(user_info.password, user['password'])
    if not verify_password:
        raise HTTPException(status_code=401, detail="Password is incorrect")
    else:
        return user