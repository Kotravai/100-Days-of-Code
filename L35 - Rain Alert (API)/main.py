import os

import requests
from twilio.rest import Client


account_sid = "someaccountSID"
auth_token = os.environ.get("SOME-AUTH_TOKEN")

OWM_Enpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    'appid': "4r3e34qf4qf4qq5g3q",
    'lat': -22.273069004034,
    'lon': 166.45335162083,
    'exclude': "current,minutely,daily"
}

response = requests.get(OWM_Enpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data)

# weather_id = []
# for i in range(12):
#     id = weather_data["hourly"][i]["weather"][0]["id"]
#     weather_id.append(id)

will_rain = False
weather_id = [(weather_data["hourly"][i]["weather"][0]["id"]) for i in range(12)]
for condition_code in weather_id:
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_='+SOMENUMBER', body="It's gonna rain today. Have an umbrella",
                                     to="+MYMOBILE")
    print(message.status)



    # 'lat': 23.4124706482,
    # 'lon': 104.8669851793,