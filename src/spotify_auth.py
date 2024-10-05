# src/spotify_auth.py
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config.credentials import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

def get_spotify_client():
    # Scope for playlist creation and user access
    scope = "playlist-modify-public user-read-recently-played"
    
    # Create Spotify API client with OAuth
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                                   redirect_uri=SPOTIPY_REDIRECT_URI,
                                                   scope=scope))
    return sp
