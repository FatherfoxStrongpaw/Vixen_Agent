class FeedbackProcessor:
    def __init__(self):
        self.feedback_history = []

    def process_feedback(self, feedback):
        """
        Process feedback from the user and store the history.
        
        Args:
            feedback (str): Feedback string indicating user satisfaction.
        
        Adjusts internal behavior based on positive or negative feedback.
        """
        self.feedback_history.append(feedback)
        
        if feedback.lower() in ["good", "excellent", "great"]:
            self.adjust_behavior("positive")
        elif feedback.lower() in ["bad", "poor", "disappointing"]:
            self.adjust_behavior("negative")
        else:
            self.adjust_behavior("neutral")
        
    def adjust_behavior(self, feedback_type):
        """
        Adjust the agent's behavior based on the type of feedback.
        
        Args:
            feedback_type (str): The feedback type, could be "positive", "negative", or "neutral".
        """
        if feedback_type == "positive":
            print("Behavior adjustment: Enhancing enthusiasm and engagement.")
            # Example: Increase energy or cheerfulness in responses.
        elif feedback_type == "negative":
            print("Behavior adjustment: Adjusting tone to be more empathetic.")
            # Example: Soften tone, be more understanding.
        else:
            print("Behavior adjustment: Keeping tone neutral.")
            # Example: Maintain a calm and steady tone.
