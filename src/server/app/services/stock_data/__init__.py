



from app.services.fmp import FmpService


class StockDataService:
    
    
    async def get_stock_page_data(ticker):
        
        company_data = await FmpService.CompanyData.get_company_outlook(ticker)
        
        return company_data.json()
    
    
