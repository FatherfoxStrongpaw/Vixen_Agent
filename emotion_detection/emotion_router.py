"""
emotion_router.py

Coordinates emotional subsystems for Vixen Agent.
Handles:
- Ticking the emotional state engine
- Analyzing user sentiment
- Adjusting output tone

This file should be imported and called from the agent loop.
"""

from emotion_detection.emotional_state import EmotionalState
from emotion_detection.emotion_analysis import analyze_sentiment
from emotion_detection.tone_adjustment import adjust_tone

class EmotionRouter:
    def __init__(self):
        self.state = EmotionalState()

    def tick(self):
        """Decay emotional state over time."""
        self.state.tick()

    def process_input(self, user_input):
        """Analyze sentiment and optionally trigger emotional response."""
        sentiment = analyze_sentiment(user_input)
        if sentiment == "positive":
            self.state.trigger("user_affection")
        elif sentiment == "negative":
            self.state.trigger("conflict")
        return sentiment

    def finalize_response(self, response_text, user_input):
        """Adjust final response based on detected sentiment."""
        return adjust_tone(response_text, user_input)

    def emotional_snapshot(self):
        return self.state.snapshot()

    def get_bias(self):
        return self.state.get_bias()


if __name__ == "__main__":
    router = EmotionRouter()
    user_input = input("User says: ")
    router.tick()
    router.process_input(user_input)
    bot_response = "Let me see what I can do for you."
    final = router.finalize_response(bot_response, user_input)
    print("Final response:", final)
    print("Current emotional state:", router.emotional_snapshot())
