# class NotificationManager:
#     # This class is responsible for sending notifications with the deal flight details.
#     pass
#

import requests

USER = "https://api.sheety.co/7c108f5d52343ccd8abd98615a1f6df9/flightDeals/users"

print("Welcome to Flight Clubbing!\nWe find the best flight deals amd mail you.")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
mail_check = True

while mail_check:
    mail_1 = input("Enter your mail id: ")
    mail_2 = input("Re-Enter your mail id: ")

    if mail_1 == mail_2:
        email = mail_1
        params = {"user": {
            "firstName": str(first_name),
            "lastName": str(last_name),
            "email": str(email)
        }}

        data = requests.post(url=USER, json=params)
        print("You're in the club.")
        mail_check = False


# response = requests.get(url=USER)
# cola = response.json()
# print(cola)
