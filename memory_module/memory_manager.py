import json
import os

# Define the path to the memory storage folder
MEMORY_FOLDER = "memory/"

# Ensure the memory folder exists
if not os.path.exists(MEMORY_FOLDER):
    os.makedirs(MEMORY_FOLDER)

def save_user_context(user_id, context):
    """
    Save the user's context into a JSON file.
    
    Args:
        user_id (str): The unique ID for the user.
        context (dict): The context data to be saved.
    """
    file_path = os.path.join(MEMORY_FOLDER, f"{user_id}_context.json")
    with open(file_path, "w") as f:
        json.dump(context, f, indent=4)

def load_user_context(user_id):
    """
    Load the user's context from a JSON file.
    
    Args:
        user_id (str): The unique ID for the user.
        
    Returns:
        dict: The loaded context data, or an empty dictionary if not found.
    """
    file_path = os.path.join(MEMORY_FOLDER, f"{user_id}_context.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        return {}  # Return an empty dictionary if no context is found
