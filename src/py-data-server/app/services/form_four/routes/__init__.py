import json
from fastapi import APIRouter, Body
from beanie import PydanticObjectId
from app.models.Response import Response
from app.models.FormFour import FormFour, UpdateFormFourModel
from app.services.form_four import FormFourService

router = APIRouter()



class FormFourController:
    
        
    @router.post("/new", response_description="Form Four added into the database", response_model=Response)
    async def add_form_four(form_four: FormFour = Body(...)):
        new_form_four = await FormFourService.add_form_four(form_four)
        
        if new_form_four :
        
            return {
                "status_code": 200,
                "response_type": "success",
                "description": "Form Four Entry Created Successfully",
                "data": new_form_four
            }
        else :
            return {
                "status_code": 500,
                "response_type": "error",
                "description": "Error Creating Form Four Entry",
                "data": new_form_four
            }
        
    @router.get("/get_paginated_form_fours/{page}/{page_size}", response_description="Form Fours retrieved", response_model=Response)
    async def get_scheduled_services(page_size, page):
        
        scheduled_services = await FormFourService.get_paginated_form_fours(int(page_size), int(page))
        
        if scheduled_services:
            return {
                "status_code": 200,
                "response_type": "success",
                "description": "Scheduled Services retrieved successfully",
                "data": scheduled_services
            }
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "No Scheduled Services exist",
        }