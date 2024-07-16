# import requests
#
# headers = {
#     "apikey": "cnWkfvgHSdpTkd9Wkyia7BfkhT14mLgn"
# }
#
# sheety_response = requests.get("https://api.sheety.co/fdca502fdefcff932197c95c799bdec5/flightDeals/prices")
# for i in range(0, len(sheety_response.json()["prices"])):
#     info = {
#         "term": f"{sheety_response.json()['prices'][i]['city']}"
#     }
#     flight_itac = requests.get("https://api.tequila.kiwi.com/locations/query", headers=headers, params=info)
#     #print(f"city: {sheety_response.json()['prices'][i]['city']}, IATA:{flight_itac.json()['locations'][0]['code']} ")
#
#     body = {
#         "price": {
#             "city": f"{sheety_response.json()['prices'][i]['city']}",
#             "iataCode": f"{flight_itac.json()['locations'][0]['code']}",
#         }
#     }
#
#     put_requests = requests.put(f"https://api.sheety.co/fdca502fdefcff932197c95c799bdec5/flightDeals/prices/{i+2}",
#                                 json=body)
#     print(put_requests.text)
#
#     flight_params = {
#         "fly_from": f"{flight_itac.json()['locations'][0]['code']}",
#         "fly_to": "MIA",
#         "dateFrom": "03/12/2022",
#         "dateTo": "03/12/2022",
#         # extanded from angelas code
#         "nights_in_dst_from": 7,
#         "nights_in_dst_to": 28,
#         "flight_type": "round",
#         "one_for_city": 1,
#         "max_stopovers": 0,
#         "curr": "GBP"
#     }
#
#     flight_response = requests.get("https://api.tequila.kiwi.com/v2/search", params=flight_params, headers=headers)
#
#     for j in range(0, len(flight_response.json()['data'])):
#         if flight_response.json()['data'][j]['price'] < sheety_response.json()['prices'][i]['lowestPrice']:
#             print(f"Low prince alert! Only {flight_response.json()['data'][j]['price']} to fly from "
#                   f"{flight_response.json()['data'][j]['cityFrom']}-{flight_response.json()['data'][j]['flyFrom']} to"
#                   f" {flight_response.json()['data'][j]['cityTo']}-{flight_response.json()['data'][j]['flyTo']}, from "
#                   f"{flight_response.json()['data'][j]['local_departure'].split('T')[0]} to "
#                   f"{flight_response.json()['data'][j]['local_arrival'].split('T')[0]}")
#
#
#
#


import requests
from bs4 import BeautifulSoup

URL = "https://www.avenzamaps.com/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="a")
print(all_movies)

# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]
#
# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")


'''
FAQ: Empire's website has changed!

When this lesson was created, I used this URL for the project: 
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

However, Empire has since changed their website. You can see this when you inspect the movie title elements. 
You'll see that the h3 with the class "title" is no longer there. 
To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.

'''