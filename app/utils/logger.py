import json
from datetime import datetime

def log_detection(result: dict):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "detection": result
    }
    with open("data/detections.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
