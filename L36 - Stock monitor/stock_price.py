import requests
import os
from twilio.rest import Client

AVE_KEY = "c68cf5014a9b2d05de563e2a50b2af2e"
AlphaV_Endpoint = "https://www.alphavantage.co/query"

NEWS_KEY = "c68cf5014a9b2d05de563e2a50b2af2e"
NEWS_EP = "https://newsapi.org/v2/everything"

account_sid = "c68cf5014a9b2d05de563e2a50b2af2e"
auth_token = "c68cf5014a9b2d05de563e2a50b2af2e"
# auth_token = os.environ.get("SOME-AUTH_TOKEN")

STOCK_SYMBOL = "TTM"
COMPANY = "Tata Motors"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_SYMBOL,
    "apikey": AVE_KEY
}

connection = requests.get(AlphaV_Endpoint, params=parameters)
connection.raise_for_status()
stock_data = connection.json()['Time Series (Daily)']

yesterday_close = list(stock_data.items())[0][1]['4. close']
day_b4_yesterday_close = list(stock_data.items())[1][1]['4. close']

up_down = None
pc_change = round(float(yesterday_close) - float(day_b4_yesterday_close) * 100 / float(day_b4_yesterday_close), 2)

if pc_change > 5:
    up_down = "🔺"
elif pc_change < 5:
    up_down = "🔻"


if pc_change > 5 or pc_change < -5:
    date_str = list(stock_data.items())[0][0]

    news_parameters = {
        "q": COMPANY,
        # "from": date_str,
        "apiKey": NEWS_KEY
    }

    news_data = requests.get(NEWS_EP, params=news_parameters)
    news_data.raise_for_status()
    news = news_data.json()["articles"]
    key_news = news[:3]
    # print(key_news)

    news_list = [f"stock = {STOCK_SYMBOL} {up_down} {pc_change} \n Headline: {article['title']} \n Brief: {article['description']}" for article in key_news]
    # print(news_list)

    client = Client(account_sid, auth_token)
    for article in news_list:
        message = client.messages.create(from_='+18623226278', body=article, to="+919789000254")
    print(message.status)
