import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 12.7266590  # Your latitude
MY_LONG = -77.8479456  # Your longitude

my_email = "somemail@xahoo.com"
pwd = "awcaefmaegenv"


def nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    k = iss_latitude - MY_LAT
    m = iss_longitude - MY_LONG

    if -5 <= k <= 5 and -5 <= m <= 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    my_hour = time_now.hour

    if sunrise <= my_hour >= sunset:
        return True
    else:
        return False


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(3600)   # To run the code every 3600 seconds.
    if nearby() and is_night():
        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=pwd)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: ISS is Nearby\n\n LOOK UP!! ")
