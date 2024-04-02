from app.services.edgar import EdgarService



class EdgarUtils:

    def getTickerFromCIK(cik):
        shortCIK = cik.lstrip("0")
        context = EdgarService.getCikTickerMap()
        json = context.json()
        for i in range(len(json["data"])):
            if str(json["data"][i][0]) == str(shortCIK):
                ticker = json["data"][i][2]
                name = json["data"][i][1]
                tickerAndName = {name : ticker}
        return tickerAndName


    def getCIKfromTicker(ticker):
        context = EdgarService.getCikTickerMap()
        json = context.json()
        for i in range(len(json["data"])):
            if str(json["data"][i][2]) == str(ticker):
                cik = json["data"][i][0]
                name = json["data"][i][1]
                cikAndName = {name : cik}
        return cikAndName


    def makeTenDigitCIK(cik):
        all_10_digit_ciks = []
        if len(str(cik)) < 10:
            difference = 10 - int(len(str(cik)))
            if difference == 1:
                cik = "0" + str(cik)
                all_10_digit_ciks.append(cik)
            elif difference == 2:
                cik = "00" + str(cik)
                all_10_digit_ciks.append(cik)
            elif difference == 3:
                cik = "000" + str(cik)
                all_10_digit_ciks.append(cik)
            elif difference == 4:
                cik = "0000" + str(cik)
                all_10_digit_ciks.append(cik)
            elif difference == 5:
                cik = "00000" + str(cik)
                all_10_digit_ciks.append(cik)
            elif difference == 6:
                cik = "000000" + str(cik)
                all_10_digit_ciks.append(cik)
        else:
            pass

        return all_10_digit_ciks

    def makeSingleTenDigitCIK(cik):
        cik = list(cik.values())[0]
        if len(str(cik)) < 10:
            difference = 10 - int(len(str(cik)))
            if difference == 1:
                ten_digit_cik = "0" + str(cik)
            elif difference == 2:
                ten_digit_cik = "00" + str(cik)
            elif difference == 3:
                ten_digit_cik = "000" + str(cik)
            elif difference == 4:
                ten_digit_cik = "0000" + str(cik)
            elif difference == 5:
                ten_digit_cik = "00000" + str(cik)
            elif difference == 6:
                ten_digit_cik = "000000" + str(cik)
        else:
            pass

        return ten_digit_cik


