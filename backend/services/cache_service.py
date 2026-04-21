cache={}

def get_cache(log:str):
    return cache.get(log)

def set_cache(log:str,result:dir):
    cache[log]=result