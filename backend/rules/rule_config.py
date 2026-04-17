RULES = {
    "ERROR": {
        "patterns": [
            r"exception",
            r"failed",
            r"error",
            r"denied",
            r"segmentation fault",
            r"nullpointer",
            r"crash",
            r"fatal",
            r"abort",
            r"unable to",
            r"cannot",
            r"failure"
        ],
    "weight": 5   
    },
    "WARNING": {
        "patterns": [
            r"warn",
            r"retry",
            r"slow",
            r"timeout",
            r"deprecated",
            r"delay",
            r"latency",
            r"high usage",
            r"memory pressure",
            r"throttle"
        ],
    "weight": 3
    },  
    "INFO": {
        "patterns": [
            r"start",
            r"running",
            r"progress",
            r"connected"
        ],
    "weight": 1
    }
}