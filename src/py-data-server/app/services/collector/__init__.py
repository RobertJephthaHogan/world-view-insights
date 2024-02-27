from app.services.edgar import EdgarService
from app.models.FormFour import FormFour
from app.database.form_four_operations import FormFourOperations
from app.services.form_four.form_four_parser import parseFormFour
from app.services.form_four import FormFourService
from bson import ObjectId
import json



class CollectorService:
    
    
    async def collect_form_fours():
        
        finalDTO = {}
        newFilingsList = []
        alreadyInDB = 0
        newFilings = 0
        recentFilings = await EdgarService.getRecentFilings("4", "", "")
                
        for filing in recentFilings:
                        
            # check if the filing exists in the database, 
            filing_exists = await FormFourOperations.retrieve_form_four_by_accession_id(filing)
            
            # if the filing already exists, do nothing
            if (len(filing_exists)):
                pass
            
            # if the filing does not already exist, create the entry
            if not (len(filing_exists)):
                                
                newFiling = filing
                soup, filing = await EdgarService.getFiling(newFiling)
                
                formFourDTO = parseFormFour(soup, filing)
                print('formFourDTO', formFourDTO)
                
                print('filing', filing)
                
                new_f4_Dto = await FormFourService().parse_form_four(soup, filing)
                #print('NEW PARSED DTO CHECK', new_f4_Dto)
                print(json.dumps(new_f4_Dto, indent=4))

                
                formFourDTO['id'] = str(ObjectId())
                #new_f4_Dto['id'] = str(ObjectId())
                
                form_four_obj = FormFour(**formFourDTO)
                # form_four_obj = FormFour(**new_f4_Dto)
                await FormFourOperations.add_form_four(form_four_obj)
                
                
                
                
        
        