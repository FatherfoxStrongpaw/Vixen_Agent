import json
import os
import config

class Memory:
    """Handles Vixen's memory system (saving & recalling user data)."""

    def __init__(self, memory_file=config.MEMORY_FILE):
        self.memory_file = memory_file
        self.data = {
            "user": {},      # Stores user preferences
            "tasks": [],     # Tracks completed tasks
            "context": []    # Stores past conversations
        }
        self.load_memory()

    def load_memory(self):
        """Loads memory from file, or starts fresh if none exists."""
        try:
            with open(self.memory_file, "r") as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    raise ValueError("Memory file structure is invalid. Resetting...")
                self.data = data  # ✅ Now updates `self.data`
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            self.data = {"user": {}, "tasks": [], "context": []}  # Default structure
            self.save_memory()  # Ensure a new file is created if missing

    def save_memory(self):
        """Saves current memory state to file."""
        try:
            with open(self.memory_file, "w", encoding="utf-8") as file:
                json.dump(self.data, file, indent=4)
            print("[DEBUG] Memory saved successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to save memory: {e}")

    # 📝 USER PREFERENCES MANAGEMENT
    def remember_user(self, key, value):
        """Stores user preferences like favorite movies, name, etc."""
        self.data["user"][key] = value
        self.save_memory()
        return f"Got it! I'll remember that {key} is {value}."

    def recall_user(self, key):
        """Retrieves a stored user preference."""
        return self.data["user"].get(key, "I don't remember that yet.")

    # 📝 TASK TRACKING
    def track_task(self, task_name):
        """Stores completed task history."""
        self.data["tasks"].append(task_name)
        self.save_memory()

    def list_tasks(self):
        """Retrieves stored task history."""
        return self.data["tasks"] if self.data["tasks"] else "No task history available."

    # 📝 CONVERSATION CONTEXT MANAGEMENT
    def store_context(self, message):
        """Stores recent conversation context (ensuring proper format & avoiding duplicates)."""
        if "context" not in self.data:
            self.data["context"] = []  # Initialize if missing

        # ✅ Debug print before storing
        print(f"[DEBUG] Attempting to store: {message}")

        # ✅ Prevent duplicate consecutive entries
        if self.data["context"] and self.data["context"][-1]["content"] == message:
            print("[DEBUG] Skipped duplicate entry.")  # ✅ Debugging line
            return  # Skip if the last stored entry is identical

        self.data["context"].append({"role": "user", "content": message})

        if len(self.data["context"]) > 10:  # Keep last 10 messages max
            self.data["context"].pop(0)

        self.save_memory()
        print("[DEBUG] Context stored successfully.")


    def get_context(self, last_n=5):
        """Retrieves recent conversation context."""
        return self.data["context"][-last_n:] if self.data["context"] else []

    def add_entry(self, role, content):
        """Stores conversation history for reasoning and recall."""
        if "context" not in self.data:
            self.data["context"] = []  # Ensure context exists

        self.data["context"].append({"role": role, "content": content})

        if len(self.data["context"]) > 10:  # Keep last 10 messages max
            self.data["context"].pop(0)

        self.save_memory()  # ✅ Properly indented

    def clear_memory(self):
        """Resets memory to factory default."""
        self.data = {"user": {}, "tasks": [], "context": []}
        self.save_memory()
