import requests
import datetime as dt

now = dt.datetime.now()
today_date = now.strftime("%Y/%m/%d")
today_time = now.strftime("%H:%M:%S")

APP_ID = ""
API_KEY = ""

exercise_url = ""
sheety_url = ""


json_params = {
  "query": input("what was your today's activity? "),
}

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

sheety_headers = {
    "Authorization": "Bearer this_is_my_token"
}
#
#
response = requests.post(url=exercise_url, json=json_params, headers=HEADERS)

for i in range(0, len(response.json()['exercises'])):
    body = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": response.json()['exercises'][i]['user_input'],
            "duration": response.json()['exercises'][i]['duration_min'],
            "calories": response.json()['exercises'][i]['nf_calories'],
            "id": i
        }
    }
    sheety_response = requests.post(url=sheety_url, json=body, headers=sheety_headers)
    print(sheety_response.text)

# response = requests.get("https://api.sheety.co/fdca502fdefcff932197c95c799bdec5/workouts/workouts")
# print(response.text)