import config  # Configuration settings
import ollama  # Ollama LLM integration
from memory import Memory  # Handles agent memory
from reasoning import ReasoningEngine  # Structured reasoning engine
from tools import Toolset  # Utility functions for file management, execution, etc.
from tasks import TaskManager  # Task scheduling and management


class VixenAgent:
    def __init__(self, model):
        self.model = model
        self.memory = Memory() if config.MEMORY_ENABLED else None
        self.reasoning = ReasoningEngine()
        self.tools = Toolset()
        self.tasks = TaskManager()
        self.past_context = self.memory.get_context(10) if self.memory else []

        self.tasks.start()  # Start background task processing

    def respond(self, prompt):
        """Processes user commands and applies memory functions."""
        
        # ✅ Memory Commands
        if prompt.startswith("remember "):
            parts = prompt.replace("remember ", "").split(":")
            if len(parts) < 2:
                return "Error: Use 'remember key: value'."
            key, value = parts[0].strip(), parts[1].strip()
            return self.memory.remember_user(key, value)

        if prompt.startswith("recall "):
            key = prompt.replace("recall ", "").strip()
            return self.memory.recall_user(key)

        if prompt == "last conversation":
            return self.memory.recall_context()

        if prompt.startswith("track task "):
            task_name = prompt.replace("track task ", "").strip()
            return self.memory.track_task(task_name)

        if prompt == "list tracked tasks":
            return self.memory.list_tasks()

        # ✅ Task & File Commands
        if prompt.startswith("read file "):
            filepath = prompt.replace("read file ", "").strip()
            return self.tools.read_file(filepath)

        if prompt.startswith("write file "):
            return self.tools.write_file(prompt)

        if prompt.startswith("list files"):
            return self.tools.list_files()
        
        if prompt.startswith("add task "):
            parts = prompt.replace("add task ", "").split(":")
            if len(parts) < 2:
                return "Error: Use 'add task task_name: interval_in_seconds'."
            name, interval = parts
            try:
                interval = int(interval.strip())

                # Assign specific functions to task names
                if name.strip() == "auto_save":
                    return self.tasks.add_task(name.strip(), interval, self.tasks.auto_save_memory)
                if name.strip() == "monitor_system":
                    return self.tasks.add_task(name.strip(), interval, self.tasks.monitor_system)
                if name.strip() == "self_check":
                    return self.tasks.add_task(name.strip(), interval, self.tasks.self_check)

                return f"Error: Task '{name.strip()}' not recognized."
            except ValueError:
                return "Error: Interval must be a number."

        if prompt.startswith("remove task "):
            return self.tasks.remove_task(prompt.replace("remove task ", "").strip())

        if prompt == "list tasks":
            tasks = self.tasks.list_tasks()
            return "Active tasks:\n" + "\n".join(tasks) if tasks else "No active tasks."

        if prompt.startswith("execute "):
            command = prompt.replace("execute ", "").strip()
            return self.tools.execute_command(command)

        # ✅ Conversation Storage
        self.memory.store_context(prompt)

        # Default reasoning and response
        system_message = {
            "role": "system",
            "content": f"You are {config.AGENT_NAME}, an AI that is {config.AGENT_PERSONA}. "
                       f"You respond with a {config.AGENT_TONE} tone and use {config.THINKING_STYLE}. "
                       "You do not just answer, you analyze, consider context, and provide structured reasoning before responding."
        }

        reasoning_analysis = self.reasoning.structured_reasoning(prompt, self.past_context)

        messages = [system_message] + self.past_context + [
            {"role": "user", "content": f"{reasoning_analysis}\n\n{prompt}"}
        ]

        try:
            response = ollama.chat(model=self.model, messages=messages)
            reply = response['message']['content']

            if self.memory:
                self.memory.add_entry("user", prompt)
                self.memory.add_entry("assistant", reply)
                self.past_context = self.memory.get_context(10)

            return reply

        except Exception as e:
            if config.DEBUG_MODE:
                print(f"Error: {e}")
            return "Something went wrong processing your request."
