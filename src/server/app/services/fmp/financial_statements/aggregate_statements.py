from concurrent.futures.thread import ThreadPoolExecutor
from . import FmpFinancialStatements



class FmpAggregateFinancialStatements:

    async def getAllQuarterlyFinancialStatementsAsReported(ticker):
        
        list_of_full_statements = []
        client = FmpFinancialStatements(ticker)
        
        executor = ThreadPoolExecutor(max_workers=5)
        one = executor.submit(client.get_quarterly_income_statements_as_reported)
        two = executor.submit(client.get_quarterly_balance_sheets_as_reported)
        three = executor.submit(client.get_quarterly_cashflow_statements_as_reported)
        
        try:
            isrr = one.result().json() 
            bsrr = two.result().json() 
            cfsrr = three.result().json()
            lengths = [len(isrr), len(bsrr), len(cfsrr)]
            max_length = max(lengths)
        except Exception as e:
            print(e)
            
        titles_list = [isrr, bsrr, cfsrr]
        isrr_dates = []
        bsrr_dates = []
        cfrr_dates = []
        for i in range(len(titles_list)):
            for j in range(max_length):
                try:
                    if titles_list[i] == isrr:
                        isrr_dates.append(titles_list[i][j]['date'])
                    elif titles_list[i] == bsrr:
                        bsrr_dates.append(titles_list[i][j]['date'])
                    elif titles_list[i] == cfsrr:
                        cfrr_dates.append(titles_list[i][j]['date'])
                    else:
                        print("Houston we have a problem")
                except Exception as ex:
                    #print(ex)
                    pass
        dates_in_all_lists = [x for x in isrr_dates if x in bsrr_dates and x in cfrr_dates]
        for i in range(len(dates_in_all_lists)):
            current_set = []
            isrr_dict = {}
            bsrr_dict = {}
            cfsrr_dict = {}
            isrr_dict['income_statement'] = isrr[i]
            bsrr_dict['balance_sheet_statement'] = bsrr[i]
            cfsrr_dict['cash_flow_statement'] = cfsrr[i]
            current_set.append(isrr_dict)
            current_set.append(bsrr_dict)
            current_set.append(cfsrr_dict)
            for j in range(len(current_set)):
                current_dict = {}
                current_dict[dates_in_all_lists[i]] = current_set
                dict_of_full_statements = {
                    'income_statement':  current_set[0],
                    'balance_sheet':  current_set[1],
                    'cash_flow_statement': current_set[2] ,
                }
                list_of_full_statements.append(dict_of_full_statements)

        return list_of_full_statements


    async def getAllQuarterlyStandardizedFinancialStatements(ticker):

        list_of_full_statements = []
        client = FmpFinancialStatements(ticker)
        
        executor = ThreadPoolExecutor(max_workers=5)
        one = executor.submit(client.get_quarterly_income_statements)
        two = executor.submit(client.get_quarterly_balance_sheets)
        three = executor.submit(client.get_quarterly_cashflow_statements)
        try:
            isrr = one.result().json() 
            bsrr = two.result().json() 
            cfsrr = three.result().json()
            lengths = [len(isrr), len(bsrr), len(cfsrr)]
            max_length = max(lengths)
        except Exception as e:
            #print(e)
            pass
        titles_list = [isrr, bsrr, cfsrr]
        isrr_dates = []
        bsrr_dates = []
        cfrr_dates = []
        for i in range(len(titles_list)):
            for j in range(max_length):
                try:
                    if titles_list[i] == isrr:
                        isrr_dates.append(titles_list[i][j]['date'])
                    elif titles_list[i] == bsrr:
                        bsrr_dates.append(titles_list[i][j]['date'])
                    elif titles_list[i] == cfsrr:
                        cfrr_dates.append(titles_list[i][j]['date'])
                    else:
                        print("Houstan we have a problem")
                except Exception as ex:
                    #print(ex)
                    pass
        dates_in_all_lists = [x for x in isrr_dates if x in bsrr_dates and x in cfrr_dates]
        for i in range(len(dates_in_all_lists)):
            current_set = []
            isrr_dict = {}
            bsrr_dict = {}
            cfsrr_dict = {}
            all_statements = {}
            isrr_dict['income_statement'] = isrr[i]
            bsrr_dict['balance_sheet_statement'] = bsrr[i]
            cfsrr_dict['cash_flow_statement'] = cfsrr[i]
            current_set.append(isrr_dict)
            current_set.append(bsrr_dict)
            current_set.append(cfsrr_dict)
            all_statements.update(isrr[i])
            all_statements.update(bsrr[i])
            all_statements.update(cfsrr[i])

            for j in range(len(current_set)):
                current_dict = {}
                current_dict[dates_in_all_lists[i]] = current_set

                dict_of_full_statements = {
                    'income_statement':  current_set[0],
                    'balance_sheet':  current_set[1],
                    'cash_flow_statement': current_set[2] ,
                }
            list_of_full_statements.append(all_statements)
        
        return list_of_full_statements