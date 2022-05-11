from bs4 import BeautifulSoup
import requests
import smtplib

# url = "https://www.amazon.in/Samsung-Storage-sAMOLED-Replacement-SM-M215GLBDINS/dp/B098NGDNMT?ref_=ast_sto_dp"
url = "https://www.amazon.in/dp/B09V44MF6K?th=1"

my_email = "mmymail@yahoo.com"
pwd = "safewcwasdvwe"

head = {
    # "Request Line": "GET / HTTP/1.1",
    # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    # "Accept-Encoding":"gzip, deflate",
    "Accept-Language": "en-us",
    # "Connection":"keep-alive",
    # "Host":"myhttpheader.com",
    # "Upgrade-Insecure-Requests": '2',
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
}


response = requests.get(url, headers=head)
data = response.text
print(data)

bs = BeautifulSoup(data, "lxml")
price_data = bs.find(name="span", class_="a-offscreen")
value = str(price_data.text)
price3 = value[1:]
price2 = price3[:6]
price = price2[:2]+price2[3:]
print(price)

# print(price_data.text)

if int(price) < 50000:
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Price drop alert!!\n\n It is time to buy!. The current price is {price}")