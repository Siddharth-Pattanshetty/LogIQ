import os
import re

def is_valid_log(line):
    line = line.strip()

    if not line:
        return False

    # ✅ Only accept lines starting with timestamp (REAL LOGS)
    # Example: 2015-10-17 15:37:56,547
    if re.match(r"\d{4}-\d{2}-\d{2}", line):
        return True

    return False


def load_logs(base_path):
    logs = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if is_valid_log(line):
                            logs.append(line.strip())
            except:
                continue

    return logs