from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from spotify_auth import get_spotify_client
from mood_analysis import analyze_mood
from playlist_creator import create_playlist, create_fein_playlist

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/create-playlist', methods=['POST'])
def create_mood_playlist():
    try:
        data = request.json
        user_text = data.get('mood', '')
        
        if not user_text:
            return jsonify({'message': 'Please provide a mood description'}), 400
        
        # Authenticate and get Spotify client
        sp = get_spotify_client()
        user_id = sp.current_user()['id']
        
        # Check for FE!N case
        if user_text.upper() in ["FE!N", "FEIN"]:
            playlist = create_fein_playlist(sp, user_id)
            return jsonify({
                'message': "Created a playlist with Travis Scott's song 'FE!N'!",
                'playlistUrl': playlist['external_urls']['spotify']
            })
        else:
            # Regular mood-based playlist
            mood = analyze_mood(user_text)
            playlist = create_playlist(sp, mood, user_id)
            
            return jsonify({
                'message': f"Created '{mood.capitalize()} Vibes Playlist' based on your mood!",
                'mood': mood,
                'playlistUrl': playlist['external_urls']['spotify']
            })
            
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
