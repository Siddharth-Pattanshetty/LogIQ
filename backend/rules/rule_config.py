# Rule configuration for the rule-based classification engine.
#
# Weight rationale:
#   ERROR   (5) — Highest weight because misclassifying errors is the costliest mistake.
#                  False negatives (missed errors) can lead to undetected outages.
#   WARNING (3) — Moderate weight. Warnings are important but less urgent than errors.
#   INFO    (1) — Lowest weight. Info logs are the default/baseline category.
#
# All patterns use \b word boundaries to prevent substring matches
# (e.g., "error" won't match "terrorize").

RULES = {
    "ERROR": {
        "patterns": [
            r"\bexception\b",
            r"\bfailed\b",
            r"\berror\b",
            r"\bdenied\b",
            r"\bsegmentation fault\b",
            r"\bnullpointer\b",
            r"\bcrash\b",
            r"\bfatal\b",
            r"\babort\b",
            r"\bunable to\b",
            r"\bcannot\b",
            r"\bfailure\b"
        ],
    "weight": 5
    },
    "WARNING": {
        "patterns": [
            r"\bwarn\b",
            r"\bretry\b",
            r"\bslow\b",
            r"\btimeout\b",
            r"\bdeprecated\b",
            r"\bdelay\b",
            r"\blatency\b",
            r"\bhigh usage\b",
            r"\bmemory pressure\b",
            r"\bthrottle\b"
        ],
    "weight": 3
    },
    "INFO": {
        "patterns": [
            r"\bstart\b",
            r"\brunning\b",
            r"\bprogress\b",
            r"\bconnected\b"
        ],
    "weight": 1
    }
}