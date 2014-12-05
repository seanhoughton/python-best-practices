import random
from datetime import datetime


def time_it(func):
    def inner(*args, **kwargs):
        start_time = datetime.now()
        value = func(*args, **kwargs)
        end_time = datetime.now()
        seconds = (end_time-start_time).total_seconds()
        print("%r took %s seconds" % (func, seconds))
        return value
    return inner

@time_it
def slow_function(data):
    sorted_data = sorted(data)
    return reversed(sorted_data)


if __name__ == "__main__":
    data = random.sample(range(10000), 5000)
    for x in range(0, 10):
        slow_function(data)
