# Test memory module functionality
from memory.memory_manager import save_user_context, load_user_context

# Simulate user context (use a sample user ID for testing)
user_id = "user1"
context = {
    "name": "John Doe",
    "preferences": {
        "tone": "cheerful"
    }
}

# Save the context
save_user_context(user_id, context)

# Load the context and print it
loaded_context = load_user_context(user_id)
print(loaded_context)
