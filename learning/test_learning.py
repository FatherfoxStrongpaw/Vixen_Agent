# Test learning module functionality
from learning.learning_module import LearningModule

# Initialize learning module and load user preferences
learning = LearningModule()
learning.load_user_preferences("user1")

# Simulate user feedback and learn from it
feedback = "good"  # Positive feedback example
learning.learn_from_feedback(feedback)

# Check if preferences have been updated
print(learning.user_preferences)  # Expected: {'tone': 'cheerful'}
