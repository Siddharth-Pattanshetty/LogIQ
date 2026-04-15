RULES = {
    "ERROR": {
        "patterns": [
            r"exception",
            r"failed",
            r"error",
            r"denied",
            r"segmentation fault",
            r"nullpointer"
        ],
        "weight": 3
    },
    "WARNING": {
        "patterns": [
            r"warn",
            r"retry",
            r"slow",
            r"timeout",
            r"deprecated"
        ],
        "weight": 2
    },
    "INFO": {
        "patterns": [
            r"info",
            r"start",
            r"starting",
            r"started",
            r"running",
            r"progress",
            r"launch",
            r"connected",
            r"listening"
        ],
        "weight": 1
    }
}