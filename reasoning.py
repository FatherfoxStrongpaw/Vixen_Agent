import config

class ReasoningEngine:
    """Handles logical processing and structured reasoning for Vixen."""

    def __init__(self):
        self.debug = config.DEBUG_MODE

    def analyze_question(self, prompt):
        """Breaks down a complex question into parts."""
        question_words = ["what", "why", "how", "who", "when", "where"]
        if any(word in prompt.lower() for word in question_words):
            return "This is a question. I will analyze it step by step."
        return "This seems like a statement. I'll process it accordingly."

    def check_for_contradictions(self, new_entry, memory):
        """Scans memory for contradictions in stored knowledge."""
        
        if not isinstance(memory, list):  # Ensure memory is a valid list
            print("[ERROR] Memory format invalid in contradiction check.")
            return "Error: Memory format is incorrect."
        
        contradictions = []
        
        for entry in memory:
            if isinstance(entry, dict) and "role" in entry and "content" in entry:
                if entry["role"] == "assistant" and isinstance(entry["content"], str):
                    if new_entry.lower() in entry["content"].lower():
                        contradictions.append(entry["content"])

        if contradictions:
            return f"Possible contradiction detected: {contradictions[-1]}"
        return "No contradictions found."

    def break_down_problem(self, prompt):
        """Breaks complex queries into smaller reasoning steps."""
        steps = []
        if "because" in prompt.lower() or "why" in prompt.lower():
            steps.append("Step 1: Identify the core subject of the question.")
            steps.append("Step 2: Determine relevant background knowledge.")
            steps.append("Step 3: Connect the reasoning logically.")
        elif "how" in prompt.lower():
            steps.append("Step 1: Define the process involved.")
            steps.append("Step 2: Identify the sequence of actions.")
            steps.append("Step 3: Explain step-by-step execution.")
        else:
            steps.append("Step 1: Analyze user intent.")
            steps.append("Step 2: Compare with prior knowledge.")
            steps.append("Step 3: Generate a structured response.")
        
        return "\n".join(steps)

    def structured_reasoning(self, prompt, memory):
        """Applies multi-step reasoning before generating a response."""
        analysis = self.analyze_question(prompt)
        contradiction_check = self.check_for_contradictions(prompt, memory)
        breakdown = self.break_down_problem(prompt)

        if self.debug:
            print(f"Reasoning Debug:\n- Analysis: {analysis}\n- Contradiction Check: {contradiction_check}\n- Breakdown:\n{breakdown}")

        return f"{analysis}\n{contradiction_check}\n{breakdown}"
