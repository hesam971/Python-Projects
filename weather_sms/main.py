import requests
import os
from .rest import Client

my_api = os.environ.get("my_api")

weather_params = {
    "lat": 51.455643,
    "lon": 7.011555,
    "appid": my_api,
}

account_sid = "AC65b7a97f9aa3788ca9039e8ef8c96fb8"
auth_token = "6960b5c53ffbd508cecc121e5d1c2a1b"


is_rainy = False

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=43.214050&lon=27.914734&appid=235691c7af2170ecf87e746a7d7504c5")
for i in range(0, len(response.json()['list'])):
    if int(response.json()['list'][i]["weather"][0]["id"]) < 700:
        is_rainy = True

if is_rainy:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Today is rainy",
        from_='+16402237067',
        to='+4917664982537'
    )
    print(message.status)
    print(message.sid)