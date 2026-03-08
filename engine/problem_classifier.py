import ollama
import json


MODEL = "phi3"


SYSTEM = """
You are a race engineer assistant.

Your job is to classify the driver's handling problem.

Return ONLY JSON in this format:

{
 "issue": "oversteer | understeer",
 "phase": "entry | mid | exit"
}

Examples:

Driver: rear sliding on throttle
Output: {"issue":"oversteer","phase":"exit"}

Driver: car pushes on turn in
Output: {"issue":"understeer","phase":"entry"}

Driver: front not rotating mid corner
Output: {"issue":"understeer","phase":"mid"}
"""


def classify_problem(text):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": text}
        ],
        options={"temperature": 0}
    )

    content = response["message"]["content"]

    return json.loads(content)