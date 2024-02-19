import json
from fastapi import APIRouter, Body
from beanie import PydanticObjectId
from app.models.Response import Response
from app.database.form_four_operations import FormFourOperations
from app.models.FormFour import FormFour, UpdateFormFourModel


router = APIRouter()



class FormFourController:
    
        
    @router.post("/new", response_description="Form Four added into the database", response_model=Response)
    async def add_form_four(form_four: FormFour = Body(...)):
        new_form_four = await FormFourOperations.add_form_four(form_four)
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Contact created successfully",
            "data": new_form_four
        }
