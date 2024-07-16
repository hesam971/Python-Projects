from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import pprint

CLIENT_ID = "a351ef36d88e49f1a02fb95dba64f5b8"
CLIENT_SECRET = "6f0163702c6d41819877e526601b2586"
REDIRECT_UNI = "http://example.com"

# response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
#
# beautiful_soup = BeautifulSoup(response.text, "html.parser")
# movie_links = beautiful_soup.findAll(name="h3", class_="title")
#
#
# with open("newfile.txt", "w") as new_file:
#     for movie in movie_links[::-1]:
#         new_file.write(f"{movie.getText()}\n")

my_answer = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{my_answer}/")
year = my_answer.split("-")[0]
billboard_page = response.text
beautiful_soup = BeautifulSoup(billboard_page, "html.parser")
the_best_songs = beautiful_soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                    scope="playlist-modify-private",
                                                    redirect_uri="http://example.com", show_dialog=True,
                                                    cache_path="token.txt"))


user_id = spotify.current_user()["id"]
song_uris = []

for best in the_best_songs:
    result = spotify.search(q=f"track:{best.getText().strip()} year:{year}", type="track", limit=1, market="US")
    # print(result) #Prints the result
    try:
    # Handling exception where the song cannot be found. It is skipped in this case.
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"{best} doesn't exist in Spotify. Skipped.")
    else:
        song_uris.append(uri)


#-----------------Creating new private playlist in Spotify--------------------------#
playlist = spotify.user_playlist_create(user=user_id, name=f"{my_answer} Billboard 100", public=False, description="Musical Time Machine")["id"]
#print(playlist)

#---------------- Adding the songs to the playlist----------------------------#
#spotify.playlist_add_items(playlist_id=playlist, items=song_uris)
spotify.user_playlist_add_tracks(user=user_id, playlist_id=playlist, tracks=song_uris)


# print("Billboard Hot 100")
# song_uris = []
# for best in the_best_songs[1]:
#     if len(sys.argv) > 1:
#         search_str = sys.argv[1]
#     else:
#         print(best.getText().strip())
#         search_str = f"{best.getText().strip()}"
#         result = spotify.search(search_str)
#         pprint.pprint(result['tracks']['items'][0]['album']['artists'][0]['name'])
#         pprint.pprint(result['tracks']['items'][0]['album']['artists'][0]['external_urls']['spotify'])
#         song_uris.append(result['tracks']['items'][0]['album']['artists'][0]['name'])
#
# # Creating a new private playlist in Spotify
# playlist = spotify.user_playlist_create(user=user_id, name=f"{my_answer} Billboard 100", public=False)
# print(playlist["id"])
# print(song_uris)
# # Adding songs found into the new playlist
# spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


