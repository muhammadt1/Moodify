# src/mood_analysis.py
from textblob import TextBlob

def analyze_mood(text):
    # Perform sentiment analysis
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Classify mood based on polarity
    if polarity > 0.1:
        return 'happy'
    elif polarity < -0.1:
        return 'sad'
    else:
        return 'neutral'
