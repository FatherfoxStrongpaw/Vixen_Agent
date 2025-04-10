import random

class CreativityEngine:
    def __init__(self):
        self.ideas_bank = [
            "Create a new game idea",
            "Invent a futuristic gadget",
            "Write a poem",
            "Design a new type of transportation",
            "Build a robot assistant",
            "Come up with a plot for a science fiction movie"
        ]

    def generate_random_idea(self):
        """
        Generate a random idea from the ideas bank.
        
        Returns:
            str: A random creative idea.
        """
        return random.choice(self.ideas_bank)

    def combine_ideas(self, idea1, idea2):
        """
        Combine two ideas into a unique new concept.
        
        Args:
            idea1 (str): The first idea.
            idea2 (str): The second idea.
        
        Returns:
            str: A combined idea.
        """
        return f"Combine '{idea1}' with '{idea2}' to create something new and exciting!"
