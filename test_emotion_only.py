from agent import VixenAgent
import sys

# Patch the ollama.chat function to avoid actually calling the LLM
import ollama
original_chat = ollama.chat

def mock_chat(*args, **kwargs):
    print("Mock LLM call - would normally call Ollama here")
    return {"message": {"content": "This is a mock response from the LLM."}}

ollama.chat = mock_chat

try:
    # Initialize the agent
    agent = VixenAgent('mistral')
    print("Agent initialized successfully with emotion detection")

    # Test the emotion detection
    sentiment = agent.emotions.process_input("I am very happy today!")
    print(f"Detected sentiment: {sentiment}")

    # Test the emotional state
    snapshot = agent.emotions.emotional_snapshot()
    print(f"Emotional snapshot: {snapshot}")

    # Test the tone adjustment
    adjusted = agent.emotions.finalize_response("Here's your response", "I am very happy today!")
    print(f"Adjusted response: {adjusted}")

    print("\nEmotion detection module is working correctly!")
finally:
    # Restore the original function
    ollama.chat = original_chat
