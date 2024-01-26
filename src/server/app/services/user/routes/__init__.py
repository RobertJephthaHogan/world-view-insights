from fastapi import Body, APIRouter, HTTPException
from passlib.context import CryptContext
from beanie import PydanticObjectId
from app.services.authentication import AuthenticationService
from app.models.User import UpdateUserModel, User, UserData, UserSignIn
from app.models.Response import Response
from app.database.user_operations import UserOperations
from app.services.user import UserService


router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])

class UserRouter:

    @router.post("/login")
    async def user_login(user_credentials: UserSignIn = Body(...)):
        data = await UserService.login_user(user_credentials)
        return data


    @router.post("/new", response_model=UserData)
    async def user_signup(user: User = Body(...)):
        new_user = await UserService.add_user(user)
        return new_user


    @router.get("/{id}", response_description="User data retrieved", response_model=Response)
    async def get_user(id: PydanticObjectId):
        data = await UserService.get_user(id)
        return data


    @router.put("/{id}", response_model=Response)
    async def update_user(id: PydanticObjectId, updated_user: UpdateUserModel = Body(...)):
        data = await UserService.update_user(id, updated_user)
        return data


    @router.delete("/{id}", response_description="User data deleted")
    async def get_user(id: PydanticObjectId):
        data = await UserService.delete_user(id)
        return data
