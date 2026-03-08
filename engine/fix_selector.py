import ollama


MODEL = "phi3"


def choose_fix_with_ai(driver_text, fixes):

    prompt = f"""
Driver problem:
{driver_text}

Available setup adjustments:
{fixes}

Choose the best fix.

Return only the sentence.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.2}
    )

    return response["message"]["content"]