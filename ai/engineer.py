import ollama

class PracticeEngineer:

    def __init__(self):
        self.model = "phi3"

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

    def choose_adjustment(self, driver_text: str, candidates: list[str]) -> str:

        prompt = f"""
Driver problem:
{driver_text}

Available setup adjustments:
{candidates}

Choose the best fix.
Return only the sentence.
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ],
            options={"temperature": 0.2},
        )

        return response["message"]["content"]

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
    

class RaceEngineer:

    def __init__(self):
        self.model = "phi3"

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

    def respond_race(self, driver_text: str) -> str:
        prompt = f"""
Driver message:
{driver_text}

You are in a race session. Respond on the radio.
Return only one short sentence.
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ],
            options={"temperature": 0.2},
        )

        return response["message"]["content"]

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
