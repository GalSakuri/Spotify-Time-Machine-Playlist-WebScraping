import os
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# Load Spotify API credentials from environment variables
Client_ID = os.environ["Client_ID"]
Client_SECRET = os.environ["Client_SECRET"]
Redirect_URI = os.environ["Redirect_URI"]

# Prompt user for the target Billboard chart date
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Billboard request
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=billboard_url, headers=header)

# Parse the Billboard page HTML and extract song titles
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Authenticate with Spotify using OAuth and cache token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri=Redirect_URI,
    client_id=Client_ID,
    client_secret=Client_SECRET,
    cache_path="token.text",
))

# Spotify user ID of the authenticated user
user_id = sp.current_user()["id"]

year = date.split("-")[0]
song_uris = []

# For each Billboard song title, search Spotify and collect its URI
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a new private Spotify playlist for the specified date
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100", public=False)

print(playlist)

# Add the collected track URIs to the newly created playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
