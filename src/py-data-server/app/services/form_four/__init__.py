from fastapi import APIRouter, Body
from app.models.FormFour import FormFour, UpdateFormFourModel
from app.database.form_four_operations import FormFourOperations
from app.services.data_fetcher_service import DataFetcherService as DFS





class FormFourService:
    
    
    
    async def add_form_four(form_four: FormFour = Body(...)):
        new_form_four = await FormFourOperations.add_form_four(form_four)

        return new_form_four

        
    async def get_paginated_form_fours(page_size: int, page: int):
        form_fours = await FormFourOperations.retrieve_form_fours_paginated(page_size, page)
        
        return form_fours
    
    
    def extract_form_four_field(self, tag, default="", transform=lambda x: x.replace('\n', '')):
        """Helper function to extract text from a BeautifulSoup tag safely."""
        try:
            return transform(tag.text)
        except AttributeError:
            return default
    
    
    def fix_string_zero_value(self, value):
        
        try:
            value = float(value)
        except ValueError:
            return "0"
        
        if value == '':
            return "0"
        return value
    
    
    async def parse_form_four(self, soup, filing):
        # Initialize dictionaries for non-derivative and derivative data
        non_derivative_table_dict = {"nonDerivativeTransactions": {}, "nonDerivativeHoldings": {}}
        derivative_table_dict = {"derivativeTransactions": {}, "derivativeHoldings": {}}
        
        # Function to process individual transactions or holdings
        def process_entries(entries, entry_fields, entry_type):
            entry_dict = {}
            for counter, entry in enumerate(entries, 1):
                fields = {field: self.extract_form_four_field(entry.find(field)) for field in entry_fields}
                # Special handling for fields requiring transformation
                transaction_shares = entry.find('transactionShares')
                transaction_shares = self.fix_string_zero_value(self.extract_form_four_field(transaction_shares, default="0"))
                
                transaction_price_per_share = entry.find('transactionPricePerShare')
                transaction_price_per_share = self.fix_string_zero_value(self.extract_form_four_field(transaction_price_per_share, default="0"))
                
                fields['transactionSize'] = float(transaction_shares) * float(transaction_price_per_share)
                entry_dict[f"{entry_type}_{counter}"] = fields

            return entry_dict
        
        # Processing Non-Derivative Table
        non_derivative_table = soup.find('nonDerivativeTable')
        if non_derivative_table:
            non_derivative_transactions = non_derivative_table.find_all('nonDerivativeTransaction')
            non_derivative_table_dict["nonDerivativeTransactions"] = process_entries(
                                                                non_derivative_transactions, 
                                                                ['securityTitle', 'transactionDate', 'deemedExecutionDate', 'transactionFormType', 'transactionCode', 'equitySwapInvolved', 'transactionShares', 'transactionPricePerShare', 'transactionAcquiredDisposedCode', 'sharesOwnedFollowingTransaction', 'directOrIndirectOwnership'],
                                                                'nonDerivativeTransaction'
                                                                )

            non_derivative_holdings = non_derivative_table.find_all('nonDerivativeHolding')
            non_derivative_table_dict["nonDerivativeHoldings"] = process_entries(
                                                                non_derivative_holdings, 
                                                                ['securityTitle', 'sharesOwnedFollowingTransaction', 'directOrIndirectOwnership', 'natureOfOwnership'],
                                                                'nonDerivativeHolding'
                                                                )

        # Processing Derivative Table
        derivative_table = soup.find('derivativeTable')
        if derivative_table:
            derivative_transactions = derivative_table.find_all('derivativeTransaction')
            derivative_table_dict["derivativeTransactions"] = process_entries(
                                                            derivative_transactions, 
                                                            ['securityTitle', 'conversionOrExercisePrice', 'transactionDate', 'deemedExecutionDate', 'transactionFormType', 'transactionCode', 'equitySwapsInvolved', 'transactionTimeliness', 'transactionShares', 'transactionPricePerShare', 'transactionAcquiredDisposedCode', 'exerciseDate', 'expirationDate', 'underlyingSecurityTitle', 'underlyingSecurityShares', 'sharesOwnedFollowingTransaction', 'directOrIndirectOwnership'],
                                                            'derivativeTransaction'
                                                            )

            derivative_holdings = derivative_table.find_all('derivativeHolding')
            derivative_table_dict["derivativeHoldings"] = process_entries(
                                                        derivative_holdings, 
                                                        ['securityTitle', 'conversionOrExercisePrice', 'exerciseDate', 'expirationDate', 'underlyingSecurityTitle', 'underlyingSecurityShares', 'sharesOwnedFollowingTransaction', 'valueOwnedFollowingTransaction', 'directOrIndirectOwnership'],
                                                        'derivativeHolding'
                                                        )

        # Construct DTO
        form_four_dto = {
            "cikAccessionId": filing,
            "schemaVersion": self.extract_form_four_field(soup.find('schemaVersion'), default=""),
            "documentType": self.extract_form_four_field(soup.find('documentType'), default=""),
            "periodOfReport": self.extract_form_four_field(soup.find('periodOfReport'), default=""),
            "notSubjectToSection16": self.extract_form_four_field(soup.find('notSubjectToSection16'), transform=lambda x: x.lower() == 'true', default=False),
            "issuerName": self.extract_form_four_field(soup.find('issuer').find('issuerName')),
            "issuerCik": self.extract_form_four_field(soup.find('issuer').find('issuerCik')),
            "issuerTradingSymbol": self.extract_form_four_field(soup.find('issuer').find('issuerTradingSymbol')),
            "issuerStockQuote": str(DFS.getStockQuote(self.extract_form_four_field(soup.find('issuer').find('issuerTradingSymbol')))),
            "issuerMarketCap": str(DFS.getMarketCap(self.extract_form_four_field(soup.find('issuer').find('issuerTradingSymbol')))),
            "rptOwnerCik" : self.extract_form_four_field(soup.find('rptOwnerCik'), default=""),
            "rptOwnerName" : self.extract_form_four_field(soup.find('rptOwnerName'), default=""),
            "isDirector" : self.extract_form_four_field(soup.find('isDirector'), default=""),
            "isOfficer" : self.extract_form_four_field(soup.find('isOfficer'), default=""),
            "isTenPercentOwner" : self.extract_form_four_field(soup.find('isTenPercentOwner'), default=""),
            "isOther" : self.extract_form_four_field(soup.find('isOther'), default=""),
            "officerTitle" : self.extract_form_four_field(soup.find('officerTitle'), default=""),
            "otherTitle" : self.extract_form_four_field(soup.find('otherTitle'), default=""),
            "nonDerivativeTable": non_derivative_table_dict,
            "derivativeTable": derivative_table_dict,
        }
        
        return form_four_dto