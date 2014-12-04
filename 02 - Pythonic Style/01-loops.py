
def c_style_index():
    '''Manually track the index with a variable'''
    langs = ["Python", "go", "lua"]
    index = 0
    length = len(langs)
    while index < length:
        #print(index, langs[index])
        index += 1


def pythonic_index():
    '''Use enumerate() to generate an index for each iteration'''
    langs = ["Python", "go", "lua"]
    for index, value in enumerate(langs):
        #print(index, value)
        pass


if __name__ == "__main__":
    for x in range(0, 100000):
        c_style_index()
    for x in range(0, 100000):
        pythonic_index()
