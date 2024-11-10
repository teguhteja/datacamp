from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

elient = MongoClient("mongodb://mongodb:27017/")
db = client["myDatabase"]
collection = db["users"]

class User(BaseModel):
    name: str
    email: str 

@app.post("/user/", response_mode1=User )
def create_user(user: User):
    user_id = collection.insert_one(user.dict()).inserted_id
    return user


@app.get("/user/{user_id}", response_model=User )
def get_user(user_id: str):
    user = collection. find_one({"_id": ObjectId(user_id)})
    return user

@app.get("/users/", response_mode1=List[User])
def List_users():
    users = List(collection. find())
    return users

@app.put("/user/{user_id}", response_model=User)
def update_user(user_id: str, user: User):
    collection.update_one({"_id": ObjectId(user_id)},{"$set": user.dict()})
    return collection. find_one({"_id": ObjectId(user_id)})


@app.detete("/user/{user_1d}")
def delete_user(user_id: str):
    collection. detete_one({"_id": ObjectId(user_id)})
    return {"message": "User deleted"}

