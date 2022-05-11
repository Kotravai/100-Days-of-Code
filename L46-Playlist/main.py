import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

BB_HOT_URL = "https://www.billboard.com/charts/hot-100/"
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'
# SPOT_CLIENT = os.environ["SPO_CLIENT"]
# SPOT_SECRET = os.environ["SPO_SECRET"]
SPOT_UID = "oh4diudoked1nc2mkfa2n8luhu"

SPOT_CLIENT = "b476cec14e0bh47eda50b8c3a4121db9e"
SPOT_SECRET = "4c314d2bf5fah4f278f2c05c0cbc89172"

""" Billboard Stuffs"""

# date = input("What date would you like to go to? Type the date in YYYY-MM-DD format. ")

date = "2022-03-15"
url = f"{BB_HOT_URL}{date}"

response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, "html.parser")
class_name = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
title_set = soup.find_all(name="h3", id="title-of-a-story", class_=class_name)
artist_set = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")

all_titles = []
all_artists = []
for a in title_set:
    word = a.text
    word = str(word).replace("\n", "")
    word = str(word).strip("\t")
    all_titles.append(word)

for a in artist_set:
    word = a.text
    word = str(word).replace("\n", "")
    word = str(word).strip("\t")
    all_artists.append(word)

""" Spotify stuffs"""

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOT_CLIENT,
    client_secret=SPOT_SECRET,
    redirect_uri="https://example.com",
    scope=scope))
# user_id = sp.current_user()["access_token"]

headers = {
  'Content-Type': 'application/json',
  'Authorization': "BQDQ2d_zpDLTHQqcBWictJCTRBS_FEWdghHUmVMCLLtbKByBE9SxEda7RBxw0b8oF_W7dCNlq9zob"
}


all_uris =[]
for i in range(len(all_titles)):
    search_q = {
            "track": all_titles[i],
            "artist": all_artists[i],
        }
    spot_response = requests.get(url='https://api.spotify.com/v1/search', params=search_q, auth=headers)
    data = spot_response.json()
    print(data)
    song_uri = data['uri']
    # song_uri = sp.search(q= "artist:" + "Adele" + "track:" + "Oh My God", type='track' )
    print(song_uri)
    all_uris.append(song_uri)


# search_q = {
#     "track": "Oh My God",
#     "artist": "Adele",
# }
#
# header={
#
# }
# spot_response = requests.get(url='https://api.spotify.com/v1', params=search_q, auth=spotify )
# print(spot_response.json())