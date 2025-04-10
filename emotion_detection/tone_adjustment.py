"""
tone_adjustment.py

Adjusts Vixen's output tone based on user sentiment.
Relies on emotion_analysis.py for sentiment classification.

Can be expanded to integrate with personality matrix or emotional state.
"""

from emotion_detection.emotion_analysis import analyze_sentiment


def adjust_tone(response_text, user_input):
    """
    Adjusts the tone of response_text based on user_input sentiment.
    This is a placeholder implementation with basic tone shifting.
    """
    sentiment = analyze_sentiment(user_input)

    if sentiment == "positive":
        return f"😊 {response_text}"
    elif sentiment == "negative":
        return f"😔 {response_text}"
    else:
        return response_text


if __name__ == "__main__":
    user_input = input("User says: ")
    response = "I'm here to help you."
    print("Adjusted response:", adjust_tone(response, user_input))