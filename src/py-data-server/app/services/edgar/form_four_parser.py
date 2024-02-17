from app.services.data_fetcher_service import DataFetcherService as DFS



def parseFormFour(soup, filing):

    ###### Full Ownership Document Contents #####
    document = soup.find('ownershipDocument').contents

    # Form 4 Non-Derivative Table
    nonDerivativeTable = soup.find('nonDerivativeTable') 
    nonDerivativeTableDict = {}
    nonDerivativeTransactionDict = {}
    nonDerivativeHoldingDict = {}
    counter = 0
    
    # non-Derivative Transactions:
    if nonDerivativeTable != None:
        for ndt in nonDerivativeTable.find_all('nonDerivativeTransaction'):
            counter += 1

            # HANDLERS
            try:
                deemedExecutionDate = (ndt.find('deemedExecutionDate').text).replace('\n',"")
            except Exception:
                deemedExecutionDate = ""
            try:
                sharesOwnedFollowingTransaction = (ndt.find('sharesOwnedFollowingTransaction').text).replace('\n',"")
            except Exception:
                sharesOwnedFollowingTransaction = None
            try:
                equitySwapInvolved = (ndt.find('equitySwapInvolved').text).replace('\n',"")
            except Exception:
                equitySwapInvolved = ""
            try:
                transactionSize = float((ndt.find('transactionShares').text).replace('\n',"")) * float((ndt.find('transactionPricePerShare').text).replace('\n',""))
            except Exception:
                transactionSize = ""

                
            nonDerivativeTransactionEntry = {
                "securityTitle": (ndt.find('securityTitle').text).replace('\n',""),
                "transactionDate": (ndt.find('transactionDate').text).replace('\n',""),
                "deemedExecutionDate": deemedExecutionDate,
                "transactionFormType": (ndt.find('transactionFormType').text).replace('\n',""),
                "transactionCode": (ndt.find('transactionCode').text).replace('\n',""),
                "equitySwapInvolved": equitySwapInvolved,
                "transactionShares": (ndt.find('transactionShares').text).replace('\n',""),
                "transactionPricePerShare": (ndt.find('transactionPricePerShare').text).replace('\n',""),
                "transactionAcquiredDisposedCode": (ndt.find('transactionAcquiredDisposedCode').text).replace('\n',""),
                "sharesOwnedFollowingTransaction": sharesOwnedFollowingTransaction,
                "directOrIndirectOwnership": (ndt.find('directOrIndirectOwnership').text).replace('\n',""),
                "transactionSize": transactionSize,
            }
            nonDerivativeTransactionDict["transaction" + str(counter)] = nonDerivativeTransactionEntry
        nonDerivativeTableDict["nonDerivativeTransactions"] = nonDerivativeTransactionDict
    else:
        pass

    # non-Derivative Holdings
    counter = 0
    if nonDerivativeTable != None:
        for ndh in nonDerivativeTable.find_all('nonDerivativeHolding'):
            counter += 1

            # HANDLERS
            try:
                natureOfOwnership = (ndh.find('natureOfOwnership').text).replace('\n',"")
            except Exception:
                natureOfOwnership = ""
            try:
                sharesOwnedFollowingTransaction = (ndh.find('sharesOwnedFollowingTransaction').text).replace('\n',"")
            except Exception:
                sharesOwnedFollowingTransaction = ""

            nonDerivativeHoldingEntry = {
                "securityTitle": (ndh.find('securityTitle').text).replace('\n',""),
                "sharesOwnedFollowingTransaction": sharesOwnedFollowingTransaction,
                "directOrIndirectOwnership": (ndh.find('directOrIndirectOwnership').text).replace('\n',""),
                "natureOfOwnership": natureOfOwnership
            }
            nonDerivativeHoldingDict["nonDerivativeHolding" + str(counter)] = nonDerivativeHoldingEntry
        nonDerivativeTableDict["nonDerivativeHoldings"] = nonDerivativeHoldingDict
    else:
        pass

    # Form 4 Derivative Table
    derivativeTable = soup.find('derivativeTable') 
    derivativeTableDict = {}
    derivativeTransactionDict = {}
    derivativeHoldingDict = {}
    counter = 0

    # HANDLERS
    try:
        deemedExecutionDate = (dt.find('deemedExecutionDate').text).replace('\n',"")
    except Exception:
        deemedExecutionDate = ""
    try:
        equitySwapsInvolved = (dt.find('equitySwapsInvolved').text).replace('\n',"")
    except Exception:
        equitySwapsInvolved = ""
    try:
        transactionTimeliness = (dt.find('transactionTimeliness').text).replace('\n',"")
    except Exception:
        transactionTimeliness = ""
    try:
        transactionShares = (dt.find('transactionShares').text).replace('\n',"")
    except Exception:
        transactionShares = ""
    try:
        sharesOwnedFollowingTransaction = (dt.find('sharesOwnedFollowingTransaction').text).replace('\n',"")
    except Exception:
        sharesOwnedFollowingTransaction = ""
    try:
        underlyingSecurityShares = (dt.find('underlyingSecurityShares').text).replace('\n',"")
    except Exception:
        underlyingSecurityShares = ""
    


    # Derivative Transactions
    if derivativeTable != None:
        for dt in derivativeTable.find_all('derivativeTransaction'):
            derivativeTransactionEntry = {
                "securityTitle": (dt.find('securityTitle').text).replace('\n',""),
                "conversionOrExercisePrice": (dt.find('conversionOrExercisePrice').text).replace('\n',""),
                "transactionDate": (dt.find('transactionDate').text).replace('\n',""),
                "deemedExecutionDate": deemedExecutionDate,
                "transactionFormType": (dt.find('transactionFormType').text).replace('\n',""),
                "transactionCode": (dt.find('transactionCode').text).replace('\n',""),
                "equitySwapsInvolved": equitySwapsInvolved,
                "transactionTimeliness": transactionTimeliness,
                "transactionShares": transactionShares,
                "transactionPricePerShare": (dt.find('transactionPricePerShare').text).replace('\n',""),
                "transactionAcquiredDisposedCode": (dt.find('transactionAcquiredDisposedCode').text).replace('\n',""),
                "exerciseDate": (dt.find('exerciseDate').text).replace('\n',""),
                "expirationDate": (dt.find('expirationDate').text).replace('\n',""),
                "underlyingSecurityTitle": (dt.find('underlyingSecurityTitle').text).replace('\n',""),
                "underlyingSecurityShares": underlyingSecurityShares,
                "sharesOwnedFollowingTransaction": sharesOwnedFollowingTransaction,
                "directOrIndirectOwnership": (dt.find('directOrIndirectOwnership').text).replace('\n',""),
            }
            derivativeTransactionDict["derivativeTransaction" + str(counter)] = derivativeTransactionEntry
        derivativeTableDict["derivativeTransactions"] = derivativeTransactionDict
    else:
        pass

    # Derivative Holdings
    counter = 0

    try:
        underlyingSecurityShares = (dh.find('underlyingSecurityShares').text).replace('\n',"")
    except Exception:
        underlyingSecurityShares = ""
    try:
        sharesOwnedFollowingTransaction = (dh.find('sharesOwnedFollowingTransaction').text).replace('\n',"")
    except Exception:
        sharesOwnedFollowingTransaction = ""
    try:
        valueOwnedFollowingTransaction = (dh.find('valueOwnedFollowingTransaction').text).replace('\n',"")
    except Exception:
        valueOwnedFollowingTransaction = ""

    if derivativeTable != None:
        for dh in derivativeTable.find_all('derivativeHolding'):
            counter += 1
            derivativeHoldingEntry = {
                "securityTitle": (dh.find('securityTitle').text).replace('\n',""),
                "conversionOrExercisePrice": (dh.find('conversionOrExercisePrice').text).replace('\n',""),
                "exerciseDate": (dh.find('exerciseDate').text).replace('\n',""),
                "expirationDate": (dh.find('expirationDate').text).replace('\n',""),
                "underlyingSecurityTitle": (dh.find('underlyingSecurityTitle').text).replace('\n',""),
                "underlyingSecurityShares": underlyingSecurityShares,
                "sharesOwnedFollowingTransaction": sharesOwnedFollowingTransaction,
                "valueOwnedFollowingTransaction": valueOwnedFollowingTransaction,
                "directOrIndirectOwnership": (dh.find('directOrIndirectOwnership').text).replace('\n',"")
            }
            derivativeHoldingDict["derivativeHolding" + str(counter)] = derivativeHoldingEntry
        derivativeTableDict["derivativeHoldings"] = derivativeHoldingDict
    else:
        pass

    # HANDLERS
    try:
        otherTitle = (soup.find('reportingOwner')).find('otherText').text
    except Exception:
        otherTitle = ""
    try:
        notSubjectToSection16 = soup.find('notSubjectToSection16').contents
    except Exception:
        notSubjectToSection16 = ""
    try:
        isOfficer = (soup.find('reportingOwner')).find('isOfficer').text
    except Exception:
        isOfficer = ""
    try:
        isTenPercentOwner = (soup.find('reportingOwner')).find('isTenPercentOwner').text
    except Exception:
        isTenPercentOwner = ""
    try:
        isOther = (soup.find('reportingOwner')).find('isOther').text
    except Exception:
        isOther = ""
    try:
        isDirector = (soup.find('reportingOwner')).find('isDirector').text
    except Exception:
        isDirector = ""
    try:
        rptOwnerCik = (soup.find('reportingOwner')).find('rptOwnerCik').text
    except Exception:
        rptOwnerCik = ""
    try:
        officerTitle = (soup.find('reportingOwner')).find('officerTitle').text
    except Exception:
        officerTitle = ""
    try:
        issuerStockQuote = DFS.getStockQuote(str((soup.find('issuer')).find('issuerTradingSymbol').text))
    except Exception:
        issuerStockQuote = "Form Four Parse error -- No Price Available For This Symbol"
    try:
        issuerMarketCap = DFS.getMarketCap(str((soup.find('issuer')).find('issuerTradingSymbol').text))
    except Exception:
        issuerMarketCap = "Form Four Parse error -- No Market Cap Available For This Symbol"

    formFourDTO = {
        "_id": filing,
        "schemaVersion": soup.find('schemaVersion').contents,
        "documentType": soup.find('documentType').contents,
        "periodOfReport": soup.find('periodOfReport').contents,
        "notSubjectToSection16": notSubjectToSection16,
        "issuerName": (soup.find('issuer')).find('issuerName').text,
        "issuerCik": (soup.find('issuer')).find('issuerCik').text,
        "issuerTradingSymbol": (soup.find('issuer')).find('issuerTradingSymbol').text,
        "issuerStockQuote" : issuerStockQuote,
        "issuerMarketCap" : issuerMarketCap,
        "rptOwnerCik" : rptOwnerCik,
        "rptOwnerName": (soup.find('reportingOwner')).find('rptOwnerName').text,
        "isDirector": isDirector,
        "isOfficer": isOfficer,
        "isTenPercentOwner": isTenPercentOwner,
        "isOther": isOther,
        "officerTitle": officerTitle,
        "otherTitle": otherTitle,
        "nonDerivativeTable" : nonDerivativeTableDict,
        "derivativeTable": derivativeTableDict,
    }


    return formFourDTO