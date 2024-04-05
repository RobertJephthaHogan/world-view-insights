from app.connection.session import session
import requests
from bs4 import BeautifulSoup
from app.config import Settings



form_types = ["10-K", "10-K/A", "10-KT", "10-KT/A", "10-Q", "10-Q/A", "10-QT", "10-12B", "10-QT/A", "10-12B/A", "10-12G", "10-12G/A", "8-K", "8-K/A", "8-K12B", "8-K12B/A", "8-K12G3", "8-K12G3/A", "8-K15D5", "8-K15D5/A", "20-F", "20-F/A", "20FR12B", "20FR12B/A", "20FR12G", "20FR12G/A", "4", "425", "424B5", "4/A", "424B2", "40-F", "40-F/A", "485APOS","485BPOS","40FR12B", "40FR12B/A", "40FR12G", "40FR12G/A", "6-K", "6-K/A", "SP&nbsp;15D2", "SP&nbsp;15D2/A", "S-1", "S-1/A", "S-1MEF", "S-3", "S-3/A", "S-3ASR", "S-3D", "S-3DPOS", "S-3MEF", "S-4", "S-4/A", "S-4EF", "S-4MEF", "S-4&nbsp;POS", "S-11", "S-11/A", "S-11MEF", "POS&nbsp;AM", "POS&nbsp;EX", "POSASR", "F-1", "F-1/A", "F-1MEF", "F-3", "F-3/A", "F-3ASR", "F-3D", "F-3DPOS", "F-3MEF", "F-4", "F-4/A", "F-4EF", "F-4MEF", "F-4&nbsp;POS", "F-10", "F-10/A", "F-10EF", "F-10POS"]
confirmed_forms = ["4"]



class EdgarService:
    
    # Each entity’s current filing history is available at the following URL:
    async def getEntityFilingHistory(tenDigitCIK):
        url = f'https://data.sec.gov/submissions/CIK{str(tenDigitCIK)}.json'
        header = {'Content-Type': 'application/json', 'User-Agent': Settings().USER_AGENT}
        r = session.get(url, headers=header)
        return r

    # Get Company Facts
    async def getCompanyFacts(tenDigitCIK):
        url = f'https://data.sec.gov/api/xbrl/companyfacts/CIK{str(tenDigitCIK)}.json'
        header = {'Content-Type': 'application/json', 'User-Agent': Settings().USER_AGENT}
        r = session.get(url, headers=header)
        return r

    # Get CIK to Ticker Map
    async def getCikTickerMap():
        url = "https://www.sec.gov/files/company_tickers_exchange.json"
        header = {'Content-Type': 'application/json', 'User-Agent': Settings().USER_AGENT}
        r = session.get(url, headers=header)
        return r

    async def getRssFeed(tenDigitCIK, formType):
        tenDigitCIK = "0000320193"
        formType = "10-Q"
        url = f'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={tenDigitCIK}&type={formType}%25&dateb=&owner=include&start=0&count=100&output=atom'
        header = {'Content-Type': 'application/json', 'User-Agent': Settings().USER_AGENT}
        r = session.get(url, headers=header)
        return r

    
    async def getFiling(filing):
        counter = 0
        cik = (filing.split('-'))[0]
        accessionUnformatted = (filing.split('-'))[1]
        accessionFormatted = f'{accessionUnformatted[:10]}-{accessionUnformatted[10:12]}-{accessionUnformatted[12:]}'
        url = f'https://www.sec.gov/Archives/edgar/data/{cik}/{accessionUnformatted}/{accessionFormatted}.txt'
        header = {'Content-Type': 'application/json', 'User-Agent': Settings().USER_AGENT}
        filingContent = requests.get(url, headers=header).text
        soup = BeautifulSoup(filingContent, "xml")

        return soup, filing


    async def getRecentFilings(formType, companyName, cik):
        url = f'https://www.sec.gov/cgi-bin/browse-edgar?company={companyName}&CIK={cik}&type={formType}&owner=include&count=100&action=getcurrent'
        header = {'Content-Type': 'application/json', 'User-Agent': Settings().USER_AGENT}
        anchor = []
        filings = []
        entry_form_types = []
        html_content = requests.get(url, headers=header).text
        # Parse the html content
        soup = BeautifulSoup(html_content, "html.parser")
        parent = soup.find_all("div")
        counter = 0
        for tag in parent:
            counter+= 1
            trTags = tag.find_all("tr")
            for tag in trTags:
                thisForm = []
                duplicate = []

                if str(tag.findChildren()[0].text) in confirmed_forms: # ensure form type is the type we are looking for
                    thisForm = tag.findChildren()[0].text
                    if (counter % 2) == 0:
                        entry_form_types.append(thisForm)
                    if (counter % 2) == 1:
                        duplicate.append(thisForm)
                    after = tag.findChildren()[1]
                    aTag = after.find_all("a")

                    anchor.append(str(aTag[0]).split('/')) 

                    for i in range(len(anchor)): # cleaning some html to grab form accession # and filing entity cik
                        thisList = []
                        for j in range(len(anchor[int(i)])):
                            thisList.append((anchor[int(i)])[int(j)])
                        for k in range(4):
                            thisList.pop(0)
                        for l in range(2):
                            thisList.pop(-1)
                        cik = thisList[0]
                        acc = thisList[1]
                        filing = cik + '-' + acc 
                        filings.append(filing)
                    entry_form_types.append(thisForm)
                else:
                    continue

        filingsSet = set(filings)
        keys = []
        final = []
        for i in range(len(filingsSet)):
            current = []
            current = list(filingsSet)[int(i)].split('-')
            keys.append(str(current[1]))
            dictionary = dict(zip(list(filingsSet), keys ))
            
        final.append(dictionary)
        final = final[0]

        return final


    