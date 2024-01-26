import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class FmpFinancialStatements:


    def __init__(self, ticker):
        self.ticker = ticker

    #########################################
    ### Standardized Financial Statements ###
    #########################################

    # Standardized Income Statements
    def get_annual_income_statements(self):
        url = f'https://financialmodelingprep.com/api/v3/income-statement/{self.ticker}?limit=120&apikey={fmp_key}'
        return requests.get(url)


    def get_quarterly_income_statements(self):
        url = f'https://financialmodelingprep.com/api/v3/income-statement/{self.ticker}?period=quarter&limit=400&apikey={fmp_key}'
        return requests.get(url)
        

    # Standardized Balance Sheets
    def get_annual_balance_sheets(self):
        url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{self.ticker}?limit=120&apikey={fmp_key}'
        return requests.get(url)
        

    def get_quarterly_balance_sheets(self):
        url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{self.ticker}?period=quarter&limit=400&apikey={fmp_key}'
        return requests.get(url)
        

    # Standardized Cash-Flow Statements
    def get_annual_cashflow_statements(self):
        url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{self.ticker}?limit=120&apikey={fmp_key}'
        return requests.get(url)


    def get_quarterly_cashflow_statements(self):
        url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{self.ticker}?period=quarter&limit=400&apikey={fmp_key}'
        return requests.get(url)



    ########################################
    ### Financial Statements As Reported ###
    ########################################

    # Income Statements As Reported 
    def get_annual_income_statements_as_reported(self):
        url = f'https://financialmodelingprep.com/api/v3/income-statement-as-reported/{self.ticker}?limit=120&apikey={fmp_key}'
        return requests.get(url)


    def get_quarterly_income_statements_as_reported(self):
        url = f'https://financialmodelingprep.com/api/v3/income-statement-as-reported/{self.ticker}?period=quarter&limit=400&apikey={fmp_key}'
        return requests.get(url)


    #  Balance Sheets As Reported 
    def get_annual_balance_sheets_as_reported(self):
        url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement-as-reported/{self.ticker}?limit=120&apikey={fmp_key}'
        return requests.get(url)


    def get_quarterly_balance_sheets_as_reported(self):
        url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement-as-reported/{self.ticker}?period=quarter&limit=400&apikey={fmp_key}'
        return requests.get(url)
        

    #  Cash-Flow Statements As Reported 
    def get_annual_cashflow_statements_as_reported(self):
        url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement-as-reported/{self.ticker}?limit=120&apikey={fmp_key}'
        return requests.get(url)


    def get_quarterly_cashflow_statements_as_reported(self):
        url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement-as-reported/{self.ticker}?period=quarter&limit=400&apikey={fmp_key}'
        return requests.get(url)


    