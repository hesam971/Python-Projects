import requests
import os
from .rest import Client

my_api = os.environ.get("my_api")

weather_params = {
    "lat": 51.455643,
    "lon": 7.011555,
    "appid": my_api,
}

account_sid = ""
auth_token = ""


is_rainy = False

response = requests.get("")
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