import ollama
import config
from agent import VixenAgent

def main():
    print(f"{config.AGENT_NAME} initialized with model: {config.OLLAMA_MODEL}")
    
    agent = VixenAgent(config.OLLAMA_MODEL)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Shutting down...")
            break

        response = agent.respond(user_input)
        print(f"{config.AGENT_NAME}: {response}")

if __name__ == "__main__":
    main()
