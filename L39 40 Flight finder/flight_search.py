import requests
from data_manager import DataManager

FLIGHT_IATA_EP = "https://tequila-api.kiwi.com/locations/query"
FLIGHT_SEARCH_EP = "https://tequila-api.kiwi.com/v2/search"
AffilID = "sdfsver gcsvefsts"
kiwi_key = "k-sevfs hvdasvrbgs"
SOURCE = 'LHR'


class FlightSearch:

    def __init__(self):
        self.flights = None
        self.header = {
            "apikey": kiwi_key
        }

    def iata_finder(self, city):
        response = requests.get(FLIGHT_IATA_EP, headers=self.header, params={'term': city, 'location_types': 'airport'})
        data = response.json()['locations']
        code = data[0]['code']
        return code


    # This class is responsible for talking to the Flight Search API.


