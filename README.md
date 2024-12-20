# Moodify - Spotify Playlist Creator Based on Mood

This project automates the creation of a Spotify playlist based on the user's mood, determined through analysis of text input. It uses Python, the Spotify Web API, and TextBlob for sentiment analysis.

## Features

- **Mood Detection**: Analyze user text input to detect their mood (happy, sad, or neutral) using sentiment analysis.
- **Spotify Playlist Creation**: Automatically create a playlist on Spotify with songs based on the user's mood.
- **Spotify API Integration**: Uses Spotify Web API to authenticate users, fetch song recommendations, and create playlists.

## Technologies Used

- **Spotify API**: done through the `spotipy` library
- **TextBlob**: for sentiment analysis
- **requests** for making HTTP requests

## Demonstration
![Project Demo](./assets/projectDemoGif1.gif)


## Prerequisites

Before you can run the project, you will need:

1. **Python** installed.
2. A **Spotify Developer Account** to access the Spotify API.
3. The following Python libraries installed:
   - `spotipy`
   - `textblob`
   - `requests`

You can install them using the following command:

```bash
pip install spotipy textblob requests
