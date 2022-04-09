#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

dm = DataManager()
fs = FlightSearch()
fd = FlightData()
sheet_data = dm.sheetdata()

# print(sheet_data)

for city in sheet_data:
    # if city['iataCode'] == '':
    #     city['iataCode'] = fs.iata_finder(city['city'])
    city['iataCode'] = fs.iata_finder(city['city'])
    dm.iataupdater()
    min_price = fd.searcher(city['iataCode'])
    if min_price == None:
        continue
    if int(min_price) <= int(city['lowestPrice']):
        print(f"Price drop alert for {city['city']}. Today's lowest price is {min_price}")

# dm.iataupdater()
#
# fs = FlightSearch()
# new_sheet_data = fs.iata_finder()
# print(new_sheet_data)
