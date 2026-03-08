import json


def load_knowledge(issue):

    with open(f"knowledge/{issue}.json") as f:
        return json.load(f)