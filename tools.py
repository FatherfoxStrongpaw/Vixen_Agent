import os
import json
import config

class Toolset:
    """Handles file access, data retrieval, and external interactions for Vixen."""

    def __init__(self):
        self.debug = config.DEBUG_MODE

    def read_file(self, filepath):
        """Reads a file and returns its content."""
        if not os.path.exists(filepath):
            return f"Error: File '{filepath}' not found."
        
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            return f"Contents of {filepath}:\n{content}"
        except Exception as e:
            return f"Error reading file: {str(e)}"

    def write_file(self, input_text):
        """Parses input text, extracts filename and content, then writes to file."""
        parts = input_text.split(":", 1)  # Split into filename and content
        if len(parts) < 2:
            return "Error: Please specify file and content using 'write file filename: content'."

        filepath = parts[0].replace("write file ", "").strip()
        content = parts[1].strip()

        try:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(content)
            return f"Successfully wrote to {filepath}."
        except Exception as e:
            return f"Error writing file: {str(e)}"



    def list_files(self, directory="."):
        """Lists files in a directory."""
        try:
            files = os.listdir(directory)
            return f"Files in '{directory}':\n" + "\n".join(files)
        except Exception as e:
            return f"Error listing files: {str(e)}"

    def execute_command(self, command):
        """Executes a system command and returns output."""
        try:
            result = os.popen(command).read()
            return f"Command Output:\n{result}"
        except Exception as e:
            return f"Error executing command: {str(e)}"
