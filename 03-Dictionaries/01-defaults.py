
def test_and_set(data):
    if 'foo' in data:
        value = data['foo']
    else:
        value = ''
    return value


def default_value(data):
    return data.get('foo', '')


if __name__ == "__main__":
    data = {'foo': 10, 'bar': 20, 'jar': 30}
    for x in range(0, 100000):
        test_and_set(data)
    for x in range(0, 100000):
        default_value(data)
