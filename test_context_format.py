from agent import VixenAgent

# Initialize the agent
agent = VixenAgent('mistral')
print("Agent initialized successfully")

# Check the format of past_context
print("Past context format:")
for item in agent.past_context:
    print(f"  {item}")
