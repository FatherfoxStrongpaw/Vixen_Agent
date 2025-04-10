from emotion_detection.emotion_router import EmotionRouter

router = EmotionRouter()
print("Emotion router initialized successfully")

sentiment = router.process_input("I am very happy today!")
print(f"Detected sentiment: {sentiment}")

response = "I'll help you with that."
adjusted = router.finalize_response(response, "I am very happy today!")
print(f"Adjusted response: {adjusted}")

snapshot = router.emotional_snapshot()
print(f"Emotional snapshot: {snapshot}")
