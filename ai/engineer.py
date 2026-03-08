import ollama

class RaceEngineer:

    def __init__(self):
        self.model = "llama3"

        self.system_prompt = """
You are a professional race engineer speaking over race radio.

Rules:
- Give very short answers.
- Maximum 2 setup changes.
- Do not explain anything.
- Only say what to changes
- Use short radio style sentences.

Example responses:
"Reduce rear anti-roll bar by 1 click."
"Increase rear wing by 1 click."
"Lower rear tire pressure by 0.2."

Never give long explanations.
"""

    def analyze_problem(self, problem, setup):

        prompt = f"""
Driver problem:
{problem}

Current setup:
{setup}
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"]