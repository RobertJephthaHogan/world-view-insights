



from app.services.fmp import FmpService


class StockDataService:
    
    
    async def get_stock_page_data(ticker):
        
        company_data = await FmpService.CompanyData.get_company_outlook(ticker)
        print('company_data', company_data.json())
        
        return company_data.json()
    
    
