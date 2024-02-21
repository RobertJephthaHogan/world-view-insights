from fastapi import APIRouter, Body
from app.models.FormFour import FormFour, UpdateFormFourModel
from app.database.form_four_operations import FormFourOperations





class FormFourService:
    
    
    
    async def add_form_four(form_four: FormFour = Body(...)):
        new_form_four = await FormFourOperations.add_form_four(form_four)

        return new_form_four

        
    async def get_paginated_form_fours(page_size: int, page: int):
        form_fours = await FormFourOperations.retrieve_form_fours_paginated(page_size, page)
        
        return form_fours