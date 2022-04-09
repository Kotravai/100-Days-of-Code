import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_ep = "https://api.sheety.co/7c108f5d52343ccd8abd98615a1f6df9/flightDeals/prices"
        self.sheet_data = {}

    def sheetdata(self):
        response = requests.get(url=self.sheety_ep)
        data = response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data

    def iataupdater(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{self.sheety_ep}/{city['id']}", json=new_data)
            # print(response.text)

