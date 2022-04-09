##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import os, random
import smtplib

my_email = "somemails@sahoo.com"
pwd = "hahahlasodif"
now = dt.datetime.now()
day = now.day
month = now.month

bday_list = pandas.read_csv("birthdays.csv").to_dict(orient='records')
for i in range(len(bday_list)):
    if bday_list[i]['day'] == day and bday_list[i]['month'] == month:
        letter = random.choice(os.listdir("letter_templates/"))

        with open(f"letter_templates/{letter}", 'r') as msg:
            content = msg.read()
            contents = content.replace("[NAME]", bday_list[i]['name'])
            with open("birthday_wish.txt", 'r+') as wishes:
                wishes.truncate(0)
                wishes.write(contents)

        if 'gmail' in bday_list[i]['email']:
            mail_smtp = 'smtp.gmail.com'
        elif 'yahoo' in bday_list[i]['email']:
            mail_smtp = 'smtp.mail.yahoo.com'

        with smtplib.SMTP(mail_smtp, port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=pwd)
            with open("birthday_wish.txt", 'r+') as wishes:
                connection.sendmail(from_addr=my_email, to_addrs=bday_list[i]['email'], msg=f"Subject: Happy Birthday\n\n{wishes.read()}")

