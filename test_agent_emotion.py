from agent import VixenAgent

# Initialize the agent
agent = VixenAgent('mistral')
print("Agent initialized successfully with emotion detection")

# Test the emotion detection
sentiment = agent.emotions.process_input("I am very happy today!")
print(f"Detected sentiment: {sentiment}")

# Test the response generation
response = agent.respond("I am very happy today!")
print(f"Agent response: {response}")

# Get the emotional snapshot
snapshot = agent.emotions.emotional_snapshot()
print(f"Emotional snapshot: {snapshot}")
