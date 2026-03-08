import random

def choose_fix(knowledge, phase=None):

    if "phases" in knowledge and phase in knowledge["phases"]:
        fixes = knowledge["phases"][phase]["fixes"]
    else:
        return ["Say the corner phase: entry, mid or exit."]

    return random.sample(fixes, min(2, len(fixes)))