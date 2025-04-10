# Test creativity engine functionality
from creativity.creativity_engine import CreativityEngine

# Initialize creativity engine
creativity = CreativityEngine()

# Generate a random idea
random_idea = creativity.generate_random_idea()
print(f"Random Idea: {random_idea}")

# Combine two ideas
idea1 = "Design a new type of transportation"
idea2 = "Invent a futuristic gadget"
combined_idea = creativity.combine_ideas(idea1, idea2)
print(f"Combined Idea: {combined_idea}")
