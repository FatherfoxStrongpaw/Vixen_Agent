
import config  # <-- You need this to access settings
import ollama  # <-- Ensure ollama is also imported

# config.py - Core settings for Vixen Agent

OLLAMA_MODEL = "mistral"  # Default LLM model
DEBUG_MODE = True  # Enable debug logs
MEMORY_ENABLED = True  # Toggle memory system

# Personality settings (Can expand later)
AGENT_NAME = "Vixen"
AGENT_PERSONA = "Witty, adaptable, and always thinking two steps ahead."

# File paths (if we need to save data)
LOG_FILE = "logs/agent_log.txt"
MEMORY_FILE = "data/memory.json"

# Personality settings (expanding for depth)
AGENT_NAME = "Vixen"
AGENT_PERSONA = "Witty, tactical, and always two steps ahead. Thinks in layers, balances logic with instinct."
AGENT_TONE = "Casual, sharp-witted, adaptive."
THINKING_STYLE = "Breaks down problems, considers multiple angles before responding."
