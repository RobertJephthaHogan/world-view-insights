from fastapi import Body, APIRouter, HTTPException
from app.database.user_operations import UserOperations
from app.services.authentication import AuthenticationService
from app.models.User import UpdateUserModel, User, UserData, UserSignIn
from app.models.Response import Response
from passlib.context import CryptContext
from beanie import PydanticObjectId



hash_helper = CryptContext(schemes=["bcrypt"])

class UserService:
    
    async def add_user(user: User = Body(...)):
        user_exists = await User.find_one(User.email == user.email)
        if user_exists:
            raise HTTPException(
                status_code=409,
                detail="User with email supplied already exists"
            )
        user.password = hash_helper.encrypt(user.password)
        new_user = await UserOperations.add_user(user)
        print('new_user', new_user)
        return new_user
    
    async def login_user(user_credentials: UserSignIn = Body(...)):
        user_exists = await User.find_one(User.email == user_credentials.username)
        if user_exists:
            password = hash_helper.verify(
                user_credentials.password, user_exists.password)
            if password:
                jwt_resp = AuthenticationService.JWTHandler().sign_jwt(user_credentials.username)
                resp_dto = {
                    "data" : user_exists,
                    "access_token" : list(jwt_resp.values())[0],
                }
                return resp_dto
            raise HTTPException(
                status_code=403,
                detail="Incorrect email or password"
            )
        raise HTTPException(
            status_code=403,
            detail="Incorrect email or password"
        )
    
    async def get_user(id: PydanticObjectId):
        user = await UserOperations.retrieve_user(id)
        if user:
            return {
                "status_code": 200,
                "response_type": "success",
                "description": "User data retrieved successfully",
                "data": user
            }
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "User doesn't exist",
            "data": {}
        }
    
    async def update_user(id: PydanticObjectId, updated_user: UpdateUserModel = Body(...)):
        new_entry = await UserOperations.update_user(id, updated_user)
        user_exists  = await User.get(str(id)) # Obj id error on return fix
        if new_entry:
            return {
                "status_code": 200,
                "response_type": "success",
                "description": "User with ID: {} updated".format(id),
                "data": user_exists
            }
        return {
            "status_code": 500,
            "response_type": "error",
            "description": "Internal Server Error While Updating User.",
            "data": False
        }
    
    async def delete_user(id: PydanticObjectId):
        user = await UserOperations.delete_user(id)
        if user:
            return {
                "status_code": 200,
                "response_type": "success",
                "description": "User data deleted successfully.",
                "data": user
            }
        else:
            return {
            "status_code": 500,
            "response_type": "error",
            "description": "Error deleting user",
        }
    
    