import requests
import datetime
import os

# os.environ["app_id"] = "9c957f3e"
# os.environ["app_key"] = "be5bf14783d0689f0b690c7a73238aab"
# os.environ["sheety_auth"] = "Some$ecretTok3n"
# os.environ["sheety_ep"] = "https://api.sheety.co/7c108f5d52343ccd8abd98615a1f6df9/myWorkouts/workouts"
nutritionix_ep = "https://trackapi.nutritionix.com/v2/natural/exercise"
# print(os.environ)
NUTRITION_APP_ID = os.environ.get("app_id")
# print(NUTRITION_APP_ID)
NUTRITION_APIKEY = os.environ.get("app_key")
# print(NUTRITION_APIKEY)
sheet = os.environ.get("sheety_auth")
SHEETY_KEY = f"Bearer {sheet}"
SHEETY_EP = os.environ.get("sheety_ep")

header = {
    "x-app-key": NUTRITION_APIKEY,
    "x-app-id": NUTRITION_APP_ID
}

nutritionix_params = {
    "query": input("Tell me what you did: "),
    "gender": "male",
    "age": 30,
    # "weight": 77,
    # "height": 182     # weight and height not working anymore
}

response = requests.post(url=nutritionix_ep, json=nutritionix_params, headers=header)
workout_data = response.json()
print(workout_data)
data = workout_data["exercises"][0]
# print(data)


exercise = data["name"]
duration = data["duration_min"]
calories = data["nf_calories"]

SHEETY_AUTH = {
    'Authorization': SHEETY_KEY
}

today = datetime.datetime.now()
date = today.strftime("%x")
time = today.strftime("%X")

data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

# sheet_data = requests.get(url=SHEETY_API)
# print(sheet_data.json())

data_entry = requests.post(url=SHEETY_EP, json=data, headers=SHEETY_AUTH)
print(data_entry.text)
