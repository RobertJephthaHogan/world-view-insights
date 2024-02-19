from app.services.edgar import EdgarService




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
            # if it does not exist 
        
        pass