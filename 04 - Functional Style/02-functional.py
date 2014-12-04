from itertools import pairwise


def manual_ascending_impl(seq):
    is_ascending = False
    prev = None
    for x in seq:
        if prev is not None and x <= prev:
            is_ascending = False
            break
        prev = x
    else:
        is_ascending = True
    return is_ascending


def functional_ascending_impl(seq):
    return all(l < r for l, r in pairwise(seq))
