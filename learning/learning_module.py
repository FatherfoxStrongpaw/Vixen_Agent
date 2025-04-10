import json
import os

# Define the path to the learning storage folder
LEARNING_FOLDER = "learning/"

# Ensure the learning folder exists
if not os.path.exists(LEARNING_FOLDER):
    os.makedirs(LEARNING_FOLDER)

class LearningModule:
    def __init__(self):
        self.user_preferences = {}

    def load_user_preferences(self, user_id):
        """
        Load the user's preferences from the stored file.

        Args:
            user_id (str): The unique ID for the user.

        Returns:
            dict: The user's preferences or an empty dictionary if no file exists.
        """
        file_path = os.path.join(LEARNING_FOLDER, f"{user_id}_preferences.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                self.user_preferences = json.load(f)
        else:
            self.user_preferences = {}

    def save_user_preferences(self, user_id):
        """
        Save the user's preferences to a JSON file.

        Args:
            user_id (str): The unique ID for the user.
        """
        file_path = os.path.join(LEARNING_FOLDER, f"{user_id}_preferences.json")
        with open(file_path, "w") as f:
            json.dump(self.user_preferences, f, indent=4)

    def update_preferences(self, feedback_type):
        """
        Update the user's preferences based on the feedback type.

        Args:
            feedback_type (str): Type of feedback (positive, negative, or neutral).
        """
        if feedback_type == "positive":
            self.user_preferences['tone'] = 'cheerful'
        elif feedback_type == "negative":
            self.user_preferences['tone'] = 'empathetic'
        else:
            self.user_preferences['tone'] = 'neutral'

    def learn_from_feedback(self, feedback):
        """
        Learn from the feedback and adjust preferences accordingly.

        Args:
            feedback (str): Feedback string from the user.
        """
        if feedback.lower() in ["good", "excellent", "great"]:
            self.update_preferences("positive")
        elif feedback.lower() in ["bad", "poor", "disappointing"]:
            self.update_preferences("negative")
        else:
            self.update_preferences("neutral")
        
        # Save updated preferences after processing feedback
        self.save_user_preferences('user1')
