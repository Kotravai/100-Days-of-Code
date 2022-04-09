import requests
import datetime as dt

FLIGHT_IATA_EP = "https://tequila-api.kiwi.com/locations/query"
FLIGHT_SEARCH_EP = "https://tequila-api.kiwi.com/v2/search"
AffilID = "skdaweagflisghdstassdeafrch"
kiwi_key = "k-evargvger"
SOURCE = 'LHR'

class FlightData:
#     #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flights = None
        self.header = {
            "apikey": kiwi_key
        }


    def searcher(self, destination):
        price = []
        today = dt.date.today()
        start_date = today.strftime('%d/%m/%Y')
        end = today + dt.timedelta(days=180)
        end_date = end.strftime('%d/%m/%Y')
        parameters = {
            'fly_from': SOURCE,
            'fly_to': destination,
            'date_from': str(start_date),
            'date_to': str(end_date),
            'max_stopovers': 0,
            'curr': 'USD',
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round'
        }
        response = requests.get(FLIGHT_SEARCH_EP, headers=self.header, params=parameters)
        data = response.json()
        try:
            for i in range(len(data)):
                price.append(data['data'][i]['price'])
            return min(price)
        except IndexError:
            print(f"No flights exist to {destination} in the searched period")
            return None


# fd = FlightData()
# cola = fd.searcher('DPS')
# print(cola)
