# src/playlist_creator.py
def create_playlist(sp, mood, user_id):
    # Mood-based playlist parameters
    if mood == 'happy':
        target_valence = 0.8
        genre = 'pop'
    elif mood == 'sad':
        target_valence = 0.2
        genre = 'acoustic'
    else:
        target_valence = 0.5
        genre = 'chill'

    # Get track recommendations from Spotify API
    recommendations = sp.recommendations(seed_genres=[genre], limit=20, target_valence=target_valence)
    track_uris = [track['uri'] for track in recommendations['tracks']]

    # Create a playlist and add recommended tracks
    playlist = sp.user_playlist_create(user_id, f'{mood.capitalize()} Vibes Playlist', public=True)
    sp.playlist_add_items(playlist['id'], track_uris)

    print(f"Created '{mood.capitalize()} Vibes Playlist' with {len(track_uris)} tracks.")
