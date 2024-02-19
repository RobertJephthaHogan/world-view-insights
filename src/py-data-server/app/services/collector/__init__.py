from app.services.edgar import EdgarService
from app.models.FormFour import FormFour
from app.database.form_four_operations import FormFourOperations
from app.services.edgar.form_four_parser import parseFormFour
from bson import ObjectId



class CollectorService:
    
    
    async def collect_form_fours():
        
        finalDTO = {}
        newFilingsList = []
        alreadyInDB = 0
        newFilings = 0
        recentFilings = await EdgarService.getRecentFilings("4", "", "")
        
        print('recentFilings', recentFilings)
        
        for filing in recentFilings:
            
            print('filing', filing)
            
            # check if the filing exists in the database, if it exists, do nothing
            filing_exists = await FormFourOperations.retrieve_form_four_by_accession_id(filing)
            
            if (len(filing_exists)):
                # do not collect the existing filing
                pass
            
            if not (len(filing_exists)):
                # if the filing does not already exist, create the entry
                print('Collecting New Form Four Filing...')
                
                newFiling = filing
                soup, filing = await EdgarService.getFiling(newFiling)
                formFourDTO = parseFormFour(soup, filing)
                formFourDTO['id'] = str(ObjectId())

                # print('newFiling', newFiling)
                # print('soup', soup)
                # print('filing', filing)
                print('formFourDTO', formFourDTO)
                
                form_four_obj = FormFour(**formFourDTO)
                await FormFourOperations.add_form_four(form_four_obj)
                
                
                pass
                
            print('filing_exists?', filing_exists)
        
        pass