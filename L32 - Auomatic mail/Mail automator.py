# import smtplib
#
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=pwd)
#     connection.sendmail(from_addr=my_email, to_addrs="xxxxxxxx@cmail.com", msg="Subject:Vanakkam\n\It's the age of SMILES")

import datetime as dt
import random
import smtplib


my_email = "somemail@yahoo.com"
pwd = "hahahdladsiv"
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with open("quotes.txt", 'r') as quote_file:
        quote_list = quote_file.readlines()
    message = random.choice(quote_list)

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=pwd)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Sunday Motivator\n\n {message}")






