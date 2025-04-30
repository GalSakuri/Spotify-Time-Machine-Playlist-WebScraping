# Spotify Nostalgia Playlist Generator

Scrapes the Billboard Hot-100 chart for a user-specified date, searches Spotify for each track, creates a private Spotify playlist, and adds the found tracks.

---

## Features

- Fetches the top 100 songs from Billboard for any date (YYYY-MM-DD).  
- Searches Spotify for each song, matching by title and year.  
- Creates a private Spotify playlist named `YYYY-MM-DD Billboard 100`.  
- Adds all successfully found tracks to your new playlist.  

---

## Requirements

- Python 3.8+  
- A Spotify developer account with a registered app (Client ID & Secret).  
- A Billboard Hot-100 scraping (this version uses BeautifulSoup & requests).  

---

## Installation

1. **Clone this repo**  
   ```bash
   git clone https://github.com/your-username/spotify-nostalgia.git
   cd spotify-nostalgia

	2.	Create & activate a virtual environment

python3 -m venv venv
source venv/bin/activate


	3.	Install dependencies

pip install -r requirements.txt

Your requirements.txt should include at least:

spotipy
python-dotenv
beautifulsoup4
requests



⸻

Configuration
	1.	Copy the sample env file and fill in your Spotify credentials:

cp .env.example .env


	2.	Edit .env to set:

SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback

⸻

Usage

Run the script:

python main.py

	•	You’ll be prompted:

Which year do you want to travel to? Type the date in this format YYYY-MM-DD:


	•	Enter a date (e.g. 2020-10-10).
	•	The script will:
	1.	Scrape Billboard for that date’s Hot-100.
	2.	Search Spotify and build a list of track URIs.
	3.	Create a private playlist on your account.
	4.	Add the found tracks to it.
	•	At the end you’ll see your new playlist’s metadata, including the Spotify URL.

⸻

How It Works
	1.	Environment & OAuth
Loads your Spotify credentials from .env and authenticates via spotipy, caching the token locally.
	2.	Scraping Billboard
Fetches the HTML of the Billboard chart page and parses out the <h3> elements that contain song titles.
	3.	Searching Spotify
For each title, performs sp.search(q="track:{title} year:{YYYY}", limit=1) to find the best match.
	4.	Creating & Populating Playlist
Creates a private playlist named after the date and adds all successfully found URIs.

⸻

Troubleshooting
	•	No songs found
	•	The CSS selector may have changed. Inspect the Billboard page and adjust the soup.select(...) string.
	•	403 Forbidden from Billboard
	•	Billboard may block scrapers. You can switch to the GitHub-hosted JSON endpoint or use Selenium.
	•	Spotify errors
	•	Ensure your redirect URI in the Spotify Developer Dashboard matches SPOTIPY_REDIRECT_URI.
	•	Check that your token cache (token.json) is writable.

⸻

License

This project is released under the MIT License. See LICENSE for details.
