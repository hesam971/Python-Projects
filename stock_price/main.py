import requests
import datetime as dt
import math
from twilio.rest import Client
now = dt.datetime.now()
# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure
account_sid = 'AC65b7a97f9aa3788ca9039e8ef8c96fb8'
auth_token = '6960b5c53ffbd508cecc121e5d1c2a1b'
client = Client(account_sid, auth_token)
# get API info for stock price
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
key_api_stock = "XCF70Y8K36VZYM05"
stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": key_api_stock,
}
# get API info for news
key_api_news = "091d2c41f7504b9e8481e714cf4bda6b"
news_params = {
    "q": STOCK_NAME,
    "apiKey": key_api_news
}
# fetch info for yesterday in different hours for stock price
response = requests.get(f"https://newsapi.org/v2/everything", params=news_params)
r = requests.get(stock_url, params=stock_params)
data = r.json()['Time Series (60min)']
item_data = data.items()
# make a list for different hours for yesterday
yesterday_market = [i[1]['4. close'] for i in item_data if int(i[0].split(" ")[1].split(":")[0]) == now.hour - 3]
day_before_market = [i[1]['4. close'] for i in item_data if int(i[0].split(" ")[1].split(":")[0]) == now.hour - 5]
# make a if statement for getting massage when sock price increasing
if abs(math.ceil(float(yesterday_market[0]) - float(day_before_market[1]))) > 5:
    # make a list for news and get info related to tesla
    news_list_title = [response.json()['articles'][i]['title'] for i in range(0, 3)]
    news_list_description = [response.json()['articles'][i]['description'] for i in range(0, 3)]
    for i in range(0, 3):
        # send message for first 3 title and description
        message = client.messages.create(
            body=f"title: {news_list_title[i]}\n description:{news_list_description[i]}",
            from_='+16402237067',
            to='+4917664982537'
        )

        print(message.status)