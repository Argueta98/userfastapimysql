from fastapi import APIRouter
from schema.user_schema import UserSchema

user = APIRouter()

@user.get("/")
def root():
    return {"message": "Hi, i am fastapi a router"}

@user.post("/api/user")
def create_user(data_user: UserSchema):
    print(data_user)