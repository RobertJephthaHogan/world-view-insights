import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class Calendars:

    # Get Earnings Calendar
    def get_earnings_calendar():
        url = f'https://financialmodelingprep.com/api/v3/earning_calendar?apikey={fmp_key}'
        return requests.get(url)

    # Get Earnings Calendar Confirmed
    def get_earnings_calendar_confirmed():
        url = f'https://financialmodelingprep.com/api/v4/earning-calendar-confirmed?apikey={fmp_key}'
        return requests.get(url)

    # Get IPO Calendar
    def get_ipo_calendar():
        url = f'https://financialmodelingprep.com/api/v3/ipo_calendar?apikey={fmp_key}'
        return requests.get(url)

    # Get IPO Calendar Confirmed
    def get_ipo_calendar_confirmed():
        url = f'https://financialmodelingprep.com/api/v3/ipo-calendar-confirmed?apikey={fmp_key}'
        return requests.get(url)

    # Get Stock Split Calendar
    def get_stock_split_calendar():
        url = f'https://financialmodelingprep.com/api/v3/stock_split_calendar?apikey={fmp_key}'
        return requests.get(url)

    # Get Dividend Calendar
    def get_dividend_calendar():
        url = f'https://financialmodelingprep.com/api/v3/stock_dividend_calendar?apikey={fmp_key}'
        return requests.get(url)

    # Get Economic Calendar
    def get_economic_calendar():
        url = f'https://financialmodelingprep.com/api/v3/economic_calendar?apikey={fmp_key}'
        return requests.get(url)
