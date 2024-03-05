from fastapi import APIRouter, Body
import json
import re
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
    
    
    async def get_purchases_and_sales(page_size: int, page: int):
        form_fours = await FormFourOperations.retrieve_form_fours_by_tx_type_paginated(page_size, page, ['P', 'S'])
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
        
        
        # Go through the nonDerivative transactions first and determine if the tx type is a purchase or sale
        non_derivative_transactions = non_derivative_table['nonDerivativeTransactions']
        codes_match, tx_code, securities_match, security_title = self.check_if_tx_codes_match(non_derivative_transactions)
        
        
        if codes_match and securities_match and tx_code == 'P':
            return tx_code, security_title 
        
        # Go through the nonDerivative transactions and determine if the tx type is a sale
        if codes_match and securities_match and tx_code == 'S':
            return tx_code, security_title 

        # TODO: Determine if the tx type is options being exercised
        
        
        # then Go through the derivative transactions and determine if the tx type is a purchase or sale (handle this later)
        
        return "undefined", "undefined"
    
    
    def calculate_weighted_average_price(self, transactions):
        total_value = 0
        total_shares = 0
        
        for key, transaction in transactions.items():
            shares = float(transaction['transactionShares'])
            
            # Prevent ValueError when transaction['transactionPricePerShare'] is not able to be converted
            try:
                price_per_share = float(transaction['transactionPricePerShare'])
            except ValueError:
                price_per_share = 0.0
            
            total_value += shares * price_per_share
            total_shares += shares
        
        if total_shares == 0:
            return 0  # To avoid division by zero
        weighted_average_price = total_value / total_shares
        return weighted_average_price
    
    
    def sum_shares_by_security_title(self, holdings, security_title):
        total_shares = 0
        # Iterate through each of the holdings (nonDerivativeHoldings here may change later)
        for holding in holdings['nonDerivativeHoldings'].values():
            # Check if the securityTitle matches the one provided
            if holding['securityTitle'] == security_title:
                # Add the sharesOwnedFollowingTransaction to the total, converting to int
                total_shares += int(holding['sharesOwnedFollowingTransaction'])
        return total_shares
    
    
    def calculate_total_transaction_size(self, transactions):
        total_transaction_size = 0
        
        for key, transaction in transactions.items():
            shares = float(transaction['transactionShares'])
            # Prevent ValueError when transaction['transactionPricePerShare'] is not able to be converted
            try:
                price_per_share = float(transaction['transactionPricePerShare'])
            except ValueError:
                price_per_share = 0.0
            
            total_transaction_size += shares * price_per_share
        
        return total_transaction_size
    
    
    def get_aggregate_tx_data(self, derivative_table, non_derivative_table):
        """determines the avg tx price, tx size, and total shares"""
        
        # Go through the nonDerivative transactions first and determine if the tx type is a purchase or sale
        non_derivative_transactions = non_derivative_table['nonDerivativeTransactions']
        codes_match, tx_code, securities_match, security_title = self.check_if_tx_codes_match(non_derivative_transactions)

        # if the codes match and the securities match, determine the avg tx price, tx size, and total shares
        if codes_match and securities_match:
            total_transaction_shares = sum(float(transaction["transactionShares"]) for transaction in non_derivative_transactions.values())
            wavg_price_per_share = self.calculate_weighted_average_price(non_derivative_transactions)
            total_transaction_size = self.calculate_total_transaction_size(non_derivative_transactions)
            return total_transaction_shares, wavg_price_per_share, total_transaction_size

        return 0, 0, 0
    
    async def parse_form_four(self, soup, filing):
        
        # TODO: HANDLE CONVERSION + BUY/SELL TRANSACTIONS
        
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
            "relationship": "",
            "link": '',
            "totalTransactionShares": '',
            "transactionPrice": '',
            "totalTransactionSize": '',
            "sharesRemainingAfterTransaction": '',
            "transactionType": '',
            "securityTitle": '',
            "nonDerivativeTable": non_derivative_table_dict,
            "derivativeTable": derivative_table_dict,
        }
        
        
        # Add the filing link to the dto
        cik = (filing.split('-'))[0]
        accessionUnformatted = (filing.split('-'))[1]

        # Define a regex pattern to match the <FILENAME> tag and capture its contents
        # This pattern assumes the tag is followed by any character except for a new line, up to the '.xml'
        pattern = r'<FILENAME>([^<]+\.xml)'
        
        # Find all occurrences of the pattern (There will only be 1)
        filenames = re.findall(pattern, soup.prettify())
        file_name = filenames[0]
        # Use regular expression to replace all white spaces and new lines
        file_name = re.sub(r'\s+', '', file_name)
        filing_url = f'https://www.sec.gov/Archives/edgar/data/{cik}/{accessionUnformatted}/xslF345X05/{file_name}'
        form_four_dto['link'] = filing_url
        
        
        # Add Filers Relationship Title to the dto
        officerTitle = self.extract_form_four_field(soup.find('officerTitle'), default="")
        otherTitle = self.extract_form_four_field(soup.find('otherTitle'), default="")
        relationshipTitle = officerTitle if officerTitle else otherTitle
        form_four_dto['relationship'] = relationshipTitle
        

        
        # Determine the transaction type and security title
        transaction_type, security_title = self.determine_transaction_type(form_four_dto['derivativeTable'], form_four_dto['nonDerivativeTable'])
        
        form_four_dto['transactionType'] = transaction_type
        form_four_dto['securityTitle'] = security_title
        
        # Add number of shares remaining after the transaction
        shares_remaining = self.sum_shares_by_security_title(non_derivative_table_dict, security_title)
        form_four_dto['sharesRemainingAfterTransaction'] = shares_remaining
        
        # TODO: Add Relationship Field
        
        if transaction_type == "P" or "S":
            
            """
                If transaction is a purchase or sale, Add total transaction size field, # Shares total, average tx price
            """
            
            total_transaction_shares, wavg_price_per_share, total_transaction_size = self.get_aggregate_tx_data(form_four_dto['derivativeTable'], form_four_dto['nonDerivativeTable'])
            form_four_dto['totalTransactionShares'] = total_transaction_shares
            form_four_dto['transactionPrice'] = wavg_price_per_share
            form_four_dto['totalTransactionSize'] = total_transaction_size
        
        
        
        print(json.dumps(form_four_dto, indent=4))

        
        return form_four_dto