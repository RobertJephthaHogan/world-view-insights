from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId


from app.models.FormFour import FormFour, UpdateFormFourModel


form_four_collection = FormFour

class FormFourOperations:

    async def add_form_four(new_form_four: FormFour) -> FormFour:
        new_form_four.id = str(ObjectId())
        form_four = await new_form_four.create()
        return form_four


    async def retrieve_all_form_fours() -> List[FormFour]:
        form_fours = await form_four_collection.all().to_list()
        return form_fours


    async def retrieve_form_four(id: FormFour) -> FormFour:
        form_four = await form_four_collection.get(str(id))
        if form_four:
            return form_four
        
    
    async def retrieve_form_four_by_accession_id(accession_id) -> List[FormFour]:
        form_four = await form_four_collection.find(FormFour.cikAccessionId == accession_id).to_list()
        return form_four
    
    
    async def retrieve_form_fours_paginated(page_size: int, page: int) -> List[FormFour]:
        # Calculate the number of documents to skip
        skip = (page - 1) * page_size
        # Query the database with skip and limit for pagination
        form_fours = await FormFour.find().sort("-_id").skip(skip).limit(page_size).to_list()
        return form_fours
        

    async def delete_form_four(id: PydanticObjectId) -> bool:
        try:
            form_four = await form_four_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if form_four:
            await form_four.delete()
            return True


    async def update_form_four_data(id: PydanticObjectId, data: dict) -> Union[bool, FormFour]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        form_four = await form_four_collection.get(str(id))
        if form_four:
            await form_four.update(update_query)
            return form_four
        return False

