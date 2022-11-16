import json

def read_json(file):
    with open(file) as f:
        data = json.load(f)
    return data