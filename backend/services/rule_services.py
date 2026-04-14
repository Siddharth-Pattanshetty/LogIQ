import re

def rule_predict(log):
    log=log.lower()

    #Error patterns
    if ("error" in log or 
        "exception" in log or 
        "failed" in log or 
        "fatal" in log or 
        "unable" in log or 
        "denied" in log):
        return {
            "label": "ERROR",
            "confidence": 0.9,
            "source": "rule"
        }

    # Warning patterns
    elif ("warn" in log or 
        "deprecated" in log or 
        "slow" in log or 
        "retry" in log):
        return {
            "label": "WARNING",
            "confidence": 0.8,
            "source": "rule"
        }

     # INFO
    elif "info" in log:
        return {
            "label": "INFO",
            "confidence": 0.7,
            "source": "rule"
        }

    return {
        "label": "INFO",
        "confidence": 0.5,
        "source": "rule"
    }