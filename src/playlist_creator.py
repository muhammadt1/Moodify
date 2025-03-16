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

    print(f"Created {mood.capitalize()} Vibes Playlist with {len(track_uris)} tracks.")


def create_fein_playlist(sp, user_id):
    """
    Create a playlist with Travis Scott's song FEIN
    """
    # Use the specific track URI for Travis Scott's FEIN
    track_uri = "spotify:track:42VsgItocQwOQC3XWZ8JNA"
    
    try:
        # Verify the track exists by getting its information
        track_info = sp.track(track_uri)
        track_name = track_info['name']
        artist_name = track_info['artists'][0]['name']
        
        playlist = sp.user_playlist_create(user_id, f"{artist_name} - {track_name} Playlist", public=True)
        sp.playlist_add_items(playlist['id'], [track_uri])
        
        print(f"Created {artist_name} - {track_name} Playlist ")
    except Exception as e:
        print(f"Error accessing the specified track: {e}")
        print("Creating a Travis Scott playlist instead.")
        
        results = sp.search(q="artist:travis scott", type="track", limit=10)
        track_uris = [track['uri'] for track in results['tracks']['items']]
        
        playlist = sp.user_playlist_create(user_id, "Travis Scott Playlist", public=True)
        sp.playlist_add_items(playlist['id'], track_uris)
        
        print(f"Created Travis Scott Playlist with {len(track_uris)} tracks.")
