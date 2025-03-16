# src/main.py
import sys
import os

# Add the project root directory (SPOT) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from spotify_auth import get_spotify_client
from mood_analysis import analyze_mood
from playlist_creator import create_playlist

def main():
    # Authenticate and get Spotify client
    sp = get_spotify_client()
    user_id = sp.current_user()['id']
    
    # Get mood input from the user
    user_text = input("Describe your mood: ")
    mood = analyze_mood(user_text)
    
    # Create a playlist based on the mood
    create_playlist(sp, mood, user_id)

if __name__ == '__main__':
    main()
