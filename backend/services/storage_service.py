import json
import os
FILE_PATH="logs/predictions.json"

def save_prediction(data):
    os.makedirs("logs",exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH,"w") as f:
            json.dump([],f)
        
    with open(FILE_PATH, "r+") as f:
        existing = json.load(f)
        existing.append(data)
        f.seek(0)
        json.dump(existing, f, indent=2)