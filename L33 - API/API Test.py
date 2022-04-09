import requests
#
response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()
# data = response.text
print(data['iss_position'])


#------------------Sunrise & Sunset----------#


# my_lat= 12.7266590
# my_lng= -77.8479456
#
# parameters = {
#     "lat": my_lat,
#     "lng": my_lng,
#     "formatted": 0
# }
#
# # sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#
# # Adding parameteers into URL
# sun_response = requests.get('https://api.sunrise-sunset.org/json?lat=12.7266590&lng=-77.8479456&formatted=0')
# sun_response.raise_for_status()
#
# data = sun_response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(':')[0]
# sunset = data["results"]["sunset"].split("T")[1].split(':')[0]
#
# # sunrise.split("T")[1].split(':')
# # sunset.split("T")