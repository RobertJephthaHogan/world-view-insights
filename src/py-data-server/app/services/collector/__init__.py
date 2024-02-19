from app.services.edgar import EdgarService
from app.database.form_four_operations import FormFourOperations



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
            print('filing_exists?', filing_exists)
            # if it does not exist 
        
        pass