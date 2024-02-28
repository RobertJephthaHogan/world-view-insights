from fastapi import APIRouter, Body
import json
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
        """If transaction share or execution prices are blank, autofill with 0"""
        try:
            value = float(value)
        except ValueError:
            return "0"
        
        if value == '':
            return "0"
        return value
    
    
    def check_if_tx_codes_match(self, transactions):
        """
            Checks if the all of the filings transaction codes and security types are the same,
            if so it returns all_codes_match, tx_code, all_securities_match, and he security_title
        """
        transaction_codes = {trans["transactionCode"] for trans in transactions.values()}
        transaction_securities = {trans["securityTitle"] for trans in transactions.values()}
        all_codes_match = len(transaction_codes) == 1
        all_securities_match = len(transaction_securities) == 1
        tx_code = list(transactions.values())[0]["transactionCode"] if all_codes_match else False
        security_title = list(transactions.values())[0]["securityTitle"] if all_securities_match else False
        return all_codes_match, tx_code, all_securities_match, security_title
    
    
    def determine_transaction_type(self, derivative_table, non_derivative_table):
        """Determines the transaction type of the filing"""
        
        # print('derivative_table', json.dumps(derivative_table, indent=4))
        # print('non_derivative_table', json.dumps(non_derivative_table, indent=4))
        
        
        
        #TODO: Go through the nonDerivative transactions first and determine if the tx type is a purchase
        
        non_derivative_transactions = non_derivative_table['nonDerivativeTransactions']
        codes_match, tx_code, securities_match, security_title = self.check_if_tx_codes_match(non_derivative_transactions)
        print('codes_match', codes_match)
        print('tx_code', tx_code)
        print('securities_match', securities_match)
        print('security_title', security_title)
        
        
        if codes_match and securities_match and tx_code == 'P':
            # return transaction type and security type
            print('PURCHASE!!!!')
            return tx_code, security_title 
        
        #TODO: Go through the nonDerivative transactions first and determine if the tx type is a sale
        
        if codes_match and securities_match and tx_code == 'S':
            # return transaction type and security type
            print('SALE!!!!')
            return tx_code, security_title 

        # TODO: Determine if the tx type is options being exercised
        
        
        
        
        return "undefined", "undefined"
    
    
    async def parse_form_four(self, soup, filing):
        # Initialize dictionaries for non-derivative and derivative data
        non_derivative_table_dict = {"nonDerivativeTransactions": {}, "nonDerivativeHoldings": {}}
        derivative_table_dict = {"derivativeTransactions": {}, "derivativeHoldings": {}}
        
        # Function to process entries in the transactions or holdings tables
        def process_entries(entries, entry_fields, entry_type):
            entry_dict = {}
            for counter, entry in enumerate(entries, 1):
                
                # Extract the fields from the tables
                fields = {field: self.extract_form_four_field(entry.find(field)) for field in entry_fields}
                
                # Special handling for fields requiring transformation tp calc transaction size
                transaction_shares = entry.find('transactionShares')
                transaction_shares = self.fix_string_zero_value(self.extract_form_four_field(transaction_shares, default="0"))
                transaction_price_per_share = entry.find('transactionPricePerShare')
                transaction_price_per_share = self.fix_string_zero_value(self.extract_form_four_field(transaction_price_per_share, default="0"))
                fields['transactionSize'] = float(transaction_shares) * float(transaction_price_per_share)
                
                # set the entry key and value
                entry_dict[f"{entry_type}_{counter}"] = fields

            return entry_dict
        
        # Processing Non-Derivative Table
        non_derivative_table = soup.find('nonDerivativeTable')
        if non_derivative_table:
            non_derivative_transactions = non_derivative_table.find_all('nonDerivativeTransaction')
            non_derivative_table_dict["nonDerivativeTransactions"] = process_entries(
                                                                non_derivative_transactions, 
                                                                [
                                                                    # Non-derivative transaction fields
                                                                    'securityTitle', 
                                                                    'transactionDate', 
                                                                    'deemedExecutionDate', 
                                                                    'transactionFormType', 
                                                                    'transactionCode', 
                                                                    'equitySwapInvolved', 
                                                                    'transactionShares', 
                                                                    'transactionPricePerShare', 
                                                                    'transactionAcquiredDisposedCode', 
                                                                    'sharesOwnedFollowingTransaction', 
                                                                    'directOrIndirectOwnership'
                                                                ],
                                                                'nonDerivativeTransaction'
                                                                )

            non_derivative_holdings = non_derivative_table.find_all('nonDerivativeHolding')
            non_derivative_table_dict["nonDerivativeHoldings"] = process_entries(
                                                                non_derivative_holdings, 
                                                                [
                                                                    # Non-derivative holding fields
                                                                    'securityTitle', 
                                                                    'sharesOwnedFollowingTransaction', 
                                                                    'directOrIndirectOwnership', 
                                                                    'natureOfOwnership'
                                                                 ],
                                                                'nonDerivativeHolding'
                                                                )

        # Processing Derivative Table
        derivative_table = soup.find('derivativeTable')
        if derivative_table:
            derivative_transactions = derivative_table.find_all('derivativeTransaction')
            derivative_table_dict["derivativeTransactions"] = process_entries(
                                                            derivative_transactions, 
                                                            [
                                                                # derivative transaction fields
                                                                'securityTitle', 
                                                                'conversionOrExercisePrice', 
                                                                'transactionDate', 
                                                                'deemedExecutionDate', 
                                                                'transactionFormType', 
                                                                'transactionCode', 
                                                                'equitySwapsInvolved', 
                                                                'transactionTimeliness', 
                                                                'transactionShares', 
                                                                'transactionPricePerShare', 
                                                                'transactionAcquiredDisposedCode', 
                                                                'exerciseDate', 
                                                                'expirationDate', 
                                                                'underlyingSecurityTitle', 
                                                                'underlyingSecurityShares', 
                                                                'sharesOwnedFollowingTransaction', 
                                                                'directOrIndirectOwnership'
                                                            ],
                                                            'derivativeTransaction'
                                                            )

            derivative_holdings = derivative_table.find_all('derivativeHolding')
            derivative_table_dict["derivativeHoldings"] = process_entries(
                                                        derivative_holdings, 
                                                        [
                                                            # derivative holding fields
                                                            'securityTitle', 
                                                            'conversionOrExercisePrice', 
                                                            'exerciseDate', 
                                                            'expirationDate', 
                                                            'underlyingSecurityTitle', 
                                                            'underlyingSecurityShares', 
                                                            'sharesOwnedFollowingTransaction', 
                                                            'valueOwnedFollowingTransaction', 
                                                            'directOrIndirectOwnership'
                                                        ],
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
            "isDirector" : self.extract_form_four_field(soup.find('isDirector'), transform=lambda x: x.lower() == 'true', default=False),
            "isOfficer" : self.extract_form_four_field(soup.find('isOfficer'), transform=lambda x: x.lower() == 'true', default=False),
            "isTenPercentOwner" : self.extract_form_four_field(soup.find('isTenPercentOwner'), transform=lambda x: x.lower() == 'true', default=False),
            "isOther" : self.extract_form_four_field(soup.find('isOther'), transform=lambda x: x.lower() == 'true', default=False),
            "officerTitle" : self.extract_form_four_field(soup.find('officerTitle'), default=""),
            "otherTitle" : self.extract_form_four_field(soup.find('otherTitle'), default=""),
            "nonDerivativeTable": non_derivative_table_dict,
            "derivativeTable": derivative_table_dict,
        }
        
        # print(json.dumps(form_four_dto, indent=4))
        
        # Determine the transaction type and security title
        transaction_type, security_title = self.determine_transaction_type(form_four_dto['derivativeTable'], form_four_dto['nonDerivativeTable'])
        
        form_four_dto['transactionType'] = transaction_type
        form_four_dto['securityTitle'] = security_title
        
        
        return form_four_dto