from time import time
def timer(fn):
    def inner(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"{fn.__name__} executed in {end - start}s")
        return result
    return inner