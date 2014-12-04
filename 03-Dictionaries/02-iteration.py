
def loop_over_keys(data):
    for key in data:
        value = data[key]


def loop_over_pair(data):
    for key, value in data.iteritems():
        pass


if __name__ == "__main__":
    data = {'key1': 'value1', 'key2': 'value2'}
    for x in range(0, 100000):
        loop_over_keys(data)
    for x in range(0, 100000):
        loop_over_pair(data)
