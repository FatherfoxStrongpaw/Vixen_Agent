"""
emotion_analysis.py

Performs sentiment analysis on user input to detect emotional tone.
Primary use: guiding tone adjustment and triggering emotional modulation.

Uses TextBlob if available, with fallback to rule-based heuristics.
"""

try:
    from textblob import TextBlob
    use_textblob = True
except ImportError:
    use_textblob = False


def analyze_sentiment(text):
    """
    Analyze sentiment of a given text.
    Returns: one of ['positive', 'neutral', 'negative']
    """
    if use_textblob:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            return "positive"
        elif polarity < -0.1:
            return "negative"
        else:
            return "neutral"
    else:
        # Fallback heuristic: very basic word presence detection
        text = text.lower()
        positive_words = ["thank you", "awesome", "love", "great", "good"]
        negative_words = ["hate", "stupid", "angry", "useless", "bad"]
        score = 0
        for word in positive_words:
            if word in text:
                score += 1
        for word in negative_words:
            if word in text:
                score -= 1

        if score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
            return "neutral"


if __name__ == "__main__":
    sample_text = input("Enter a test phrase: ")
    print("Detected sentiment:", analyze_sentiment(sample_text))