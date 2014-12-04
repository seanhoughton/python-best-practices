import random


def is_even(num):
    return num % 2 == 0


def c_style_loop(numbers):
    '''Traditional loop that progressively adds to the filtered list'''
    evens = []
    for num in numbers:
        if is_even(num):
            evens.append(num)
    return evens


def pythonic_loop_1(numbers):
    '''Use a list comprehension to generate a filtered list'''
    return [num for num in numbers if is_even(num)]


def pythonic_loop_2(numbers):
    '''Use the built-in filter function to create a filtered list'''
    return filter(is_even, numbers)


if __name__ == "__main__":
    random.seed(1234)
    numbers = random.sample(range(0, 50000), 10000)
    for x in range(0, 100):
        c_style_loop(numbers)
    for x in range(0, 100):
        pythonic_loop_1(numbers)
    for x in range(0, 100):
        pythonic_loop_2(numbers)
