LLM_CALL_LIMIT=5
llm_calls=0

def can_call_llm():
    global llm_calls
    return llm_calls<LLM_CALL_LIMIT

def increment_llm_calls():
    global llm_calls
    llm_calls += 1