import requests
from datetime import datetime

TOKEN = 'EVERABRRTEGAEFVGE'
USER_NAME = "FVERAVEE"


pixela_ep = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": 'yes',
    "notMinor": 'yes'
}

# response = requests.post(url=pixela_ep, json=user_params)
# print(response.text)


graph_ep = f"{pixela_ep}/{USER_NAME}/graphs"

graph_config = {
    "id": "tracker2022",
    "name": "Cardio Tracker",
    "unit": "km",
    "type": 'float',
    "color": 'sora'
}

header = {
    "X-USER-TOKEN": "EWCEWSCEWFCAEWSCE"
}

# response2 = requests.post(url=graph_ep, json=graph_config, headers=header)

today = datetime(day=5, month=3, year=2022)

data_ep = f"{graph_ep}/tracker2022"
data_config = {
    "date": today.strftime('%Y%m%d'),
    "quantity": "10",
}

# print(today.strftime('%Y%m%d'),)

# data_point = requests.post(url=data_ep, json=data_config, headers=header)
# print(data_point.text)

updater_ep = f"{data_ep}/{today.strftime('%Y%m%d')}"

update = {
    "quantity": '13'
}

# data_changer = requests.put(url=updater_ep ,json=update, headers=header)
# print(data_changer.text)


delete_pixel = requests.delete(url=updater_ep,headers=header)
print(delete_pixel.text)