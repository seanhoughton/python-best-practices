import random

def test_and_set(data, key):
    if key in data:
        value = data[key]
    else:
        value = ''
    return value


def try_except(data, key):
    try:
        return data[key]
    except KeyError:
        return ''


def default_value(data, key):
    return data.get(key, '')


if __name__ == "__main__":
    data = {'foo': 10, 'bar': 20, 'jar': 30}
    keys = data.keys() + ['missing']
    for x in range(0, 100000):
        test_and_set(data, random.choice(keys))
    for x in range(0, 100000):
        try_except(data, random.choice(keys))
    for x in range(0, 100000):
        default_value(data, random.choice(keys))
