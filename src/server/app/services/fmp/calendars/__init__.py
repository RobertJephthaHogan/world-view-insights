import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class Calendars:

    # Get Earnings Calendar
    def getEarningsCalendar():
        url = f'https://financialmodelingprep.com/api/v3/earning_calendar?apikey={fmp_key}'
        return requests.get(url)

    # Get Earnings Calendar Confirmed
    def getEarningsCalendarConfirmed():
        url = f'https://financialmodelingprep.com/api/v4/earning-calendar-confirmed?apikey={fmp_key}'
        return requests.get(url)

    # Get IPO Calendar
    def getIPOCalendar():
        url = f'https://financialmodelingprep.com/api/v3/ipo_calendar?apikey={fmp_key}'
        return requests.get(url)

    # Get IPO Calendar Confirmed
    def getIPOCalendarConfirmed():
        url = f'https://financialmodelingprep.com/api/v3/ipo-calendar-confirmed?apikey={fmp_key}'
        return requests.get(url)

    # Get Stock Split Calendar
    def getStockSplitCalendar():
        url = f'https://financialmodelingprep.com/api/v3/stock_split_calendar?apikey={fmp_key}'
        return requests.get(url)

    # Get Dividend Calendar
    def getDividendCalendar():
        url = f'https://financialmodelingprep.com/api/v3/stock_dividend_calendar?apikey={fmp_key}'
        return requests.get(url)

    # Get Economic Calendar
    def getEconomicCalendar():
        url = f'https://financialmodelingprep.com/api/v3/economic_calendar?apikey={fmp_key}'
        return requests.get(url)