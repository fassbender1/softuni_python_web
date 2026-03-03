import time
from functools import wraps


def measure_execution(view_func):

    @wraps(view_func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = view_func(*args, **kwargs)
        end_time = time.time()
        print("The time it took was:", end_time - start_time, "seconds")
        return result

    return wrapper