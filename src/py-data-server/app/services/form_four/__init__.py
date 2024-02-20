from fastapi import APIRouter, Body
from app.models.FormFour import FormFour, UpdateFormFourModel
from app.database.form_four_operations import FormFourOperations





class FormFourService:
    
    
    
    async def add_form_four(form_four: FormFour = Body(...)):
        new_form_four = await FormFourOperations.add_form_four(form_four)
        print('new_form_four', new_form_four)

        
        return new_form_four

        