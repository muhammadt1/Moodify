# src/main.py
import sys
import os

# Add the project root directory (SPOT) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from spotify_auth import get_spotify_client
from mood_analysis import analyze_mood
from playlist_creator import create_playlist, create_fein_playlist

def main():
    # Authenticate and get Spotify client
    sp = get_spotify_client()
    user_id = sp.current_user()['id']
    
    # Get mood input from the user
    user_text = input("Describe your mood: ")
    
    # Checks case for cameo entry.
    if user_text.upper() in ["FE!N", "FEIN"]:
        print("Creating a playlist with Travis Scott's song 'FEIN'...")
        create_fein_playlist(sp, user_id)
    else:
        # Regular mood-based playlist
        mood = analyze_mood(user_text)
        create_playlist(sp, mood, user_id)

if __name__ == '__main__':
    main()
