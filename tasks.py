import threading
import time
import json
import os
import psutil  # System monitoring (install with: pip install psutil)

TASK_FILE = "data/tasks.json"  # File to store tasks

class TaskManager:
    """Handles scheduled and background tasks for Vixen."""

    def __init__(self):
        self.tasks = []
        self.running = False
        self.load_tasks()  # Load saved tasks on startup

    ### 🔹 TASK PERSISTENCE 🔹 ###

    def save_tasks(self):
        """Saves task metadata to a file (without function references)."""
        try:
            task_data = [
                {"name": task["name"], "interval": task["interval"], "next_run": task["next_run"]}
                for task in self.tasks
            ]
            with open(TASK_FILE, "w") as f:
                json.dump(task_data, f)
            print("[DEBUG] Tasks saved successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to save tasks: {e}")



    def load_tasks(self):
        """Loads tasks from a file and restores their function references."""
        if os.path.exists(TASK_FILE):
            try:
                with open(TASK_FILE, "r") as f:
                    task_data = json.load(f)
                
                self.tasks = []
                for task in task_data:
                    # Restore the correct function based on task name
                    if task["name"] == "monitor_system":
                        action = self.monitor_system
                    elif task["name"] == "self_check":
                        action = self.self_check
                    elif task["name"] == "crash_recovery":
                        action = self.crash_recovery
                    elif task["name"] == "auto_save":
                        action = self.auto_save_memory
                    else:
                        print(f"[WARNING] Unknown task '{task['name']}' – skipping.")
                        continue  # Skip unknown tasks

                    # Reconstruct the task with the correct function
                    restored_task = {
                        "name": task["name"],
                        "interval": task["interval"],
                        "next_run": task["next_run"],
                        "action": action
                    }
                    self.tasks.append(restored_task)

                print("[DEBUG] Tasks loaded successfully.")
            except Exception as e:
                print(f"[ERROR] Failed to load tasks: {e}")



    ### 🔹 TASK MANAGEMENT 🔹 ###

    def add_task(self, name, interval, action):
        """Adds a repeating task that runs every 'interval' seconds."""
        task = {
            "name": name,
            "interval": interval,
            "action": action,
            "next_run": time.time() + interval
        }
        self.tasks.append(task)
        self.save_tasks()  # Save tasks automatically
        return f"Task '{name}' added, running every {interval} seconds."

    def remove_task(self, name):
        """Removes a task by name and updates the task file."""
        self.tasks = [task for task in self.tasks if task["name"] != name]
        self.save_tasks()  # Save tasks after removal
        return f"Task '{name}' removed."

    def list_tasks(self):
        """Lists all active tasks."""
        return [task["name"] for task in self.tasks]

    ### 🔹 TASK EXECUTION 🔹 ###

    def run_tasks(self):
        """Runs scheduled tasks in the background and restarts if needed."""
        self.running = True
        print("[DEBUG] Task manager is running...")

        while self.running:
            now = time.time()
            for task in self.tasks:
                if now >= task["next_run"]:
                    try:
                        print(f"[DEBUG] Running task: {task['name']}")
                        task["action"]()  # Run the actual task
                        print(f"[DEBUG] Task '{task['name']}' executed successfully.")
                    except Exception as e:
                        print(f"[ERROR] Task '{task['name']}' failed: {e}")
                        if task["name"] != "self_check":
                            print(f"[DEBUG] Restarting failed task: {task['name']}")
                            task["next_run"] = now + 5  # Restart in 5 seconds
                        else:
                            print("[ERROR] Critical failure in self-check. Manual intervention needed.")

                    task["next_run"] = now + task["interval"]
            time.sleep(1)  # Prevent CPU overload

    def start(self):
        """Starts the task manager in a background thread."""
        thread = threading.Thread(target=self.run_tasks, daemon=True)
        thread.start()
        return "Task manager started."

    def stop(self):
        """Stops all tasks."""
        self.running = False
        return "Task manager stopped."

    ### 🔹 USEFUL TASKS 🔹 ###

    def auto_save_memory(self):
        """Saves memory to a file every X minutes."""
        save_path = "data/memory_backup.json"
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(str(self.tasks))  # Replace with real memory data later
        print(f"[Task] Auto-saved memory to {save_path}")

    def monitor_system(self):
        """Checks system usage and logs warnings."""
        print("[DEBUG] monitor_system() was called.")  
        try:
            cpu_usage = psutil.cpu_percent()
            disk_usage = psutil.disk_usage("/").percent
            print(f"[DEBUG] CPU Usage: {cpu_usage}%")
            print(f"[DEBUG] Disk Usage: {disk_usage}%")
        except Exception as e:
            print(f"[ERROR] monitor_system() failed: {e}")

def self_check(self):
    """Ensures Vixen is running smoothly and restarts failed tasks."""
    print("[Task] Performing self-check...")

    # Track missing tasks
    missing_tasks = []
    
    for task in self.tasks:
        now = time.time()
        if now >= task["next_run"] + task["interval"] * 2:  # If it's overdue by 2 intervals
            print(f"[ERROR] Task '{task['name']}' appears to be missing or failed.")
            missing_tasks.append(task["name"])

    # Restart missing tasks
    for task_name in missing_tasks:
        self.restart_task(task_name)
    
    print("[DEBUG] Self-check complete.")

def restart_task(self, task_name):
    """Restarts a failed or missing task."""
    for task in self.tasks:
        if task["name"] == task_name:
            print(f"[DEBUG] Restarting task: {task_name}")
            task["next_run"] = time.time() + task["interval"]  # Schedule it again
            return
    print(f"[ERROR] Could not restart task '{task_name}' (task not found).")


    def crash_recovery(self):
        """Detects if the agent crashes and restarts it."""
        print("[DEBUG] Performing crash recovery check...")

        # Check if the task manager is still running
        if not self.running:
            print("[ERROR] Task manager is not running! Restarting...")
            self.start()

        print("[DEBUG] Crash recovery check complete.")

if __name__ == "__main__":
    tm = TaskManager()
    tm.monitor_system()  # Manually call the function
