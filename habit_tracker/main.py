import requests
import datetime as dt
TOKEN = "-my1370habit1991tracker"
USERNAME = "hesam971"
GRAPH_ID = "heso971"
GRAPH_NAME = "habit_tracker_for_bicycle"
# create user page in webpage
create_user = "https://pixe.la/v1/users"
user_info = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=create_user, json=user_info)
# print(response.text)

# create my own graph in webpage
headers = {
"X-USER-TOKEN": TOKEN
}
# to find webpage in internet https://pixe.la/v1/users/{username}/graphs/{id}
graph_user = f"https://pixe.la/v1/users/{USERNAME}/graphs"
user_graph_info = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}
# response = requests.post(url=graph_user, json=user_graph_info, headers=headers)
# print(response.text)

# post our habits to put it in table (post a pixel)
now = dt.datetime.now()
todays_data = now.strftime('%Y%m%d')
pixel_user = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
pixel_info = {
    "date": str(todays_data),
    "quantity": "6.1",
}
# response = requests.post(url=pixel_user, json=pixel_info, headers=headers)
# print(response.text)

# update our habits
# update_pixel_user = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
# update_pixel_info = {
#     "name": GRAPH_NAME,
#     "unit": "Km",
#     "color": "sora",
# }
# response = requests.put(url=update_pixel_user, json=update_pixel_info, headers=headers)
# print(response.text)


update_pixel_user = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{todays_data}"
update_pixel_info = {
    "date": str(todays_data),
    "quantity": "10",
}
# response = requests.put(url=update_pixel_user, json=update_pixel_info, headers=headers)
# print(response.text)

# delete pixel

delete_pixel_user = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{todays_data}"

response = requests.delete(url=delete_pixel_user, headers=headers)
print(response.text)