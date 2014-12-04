
def default_arrays_are_bad(bad=[], good=None):
    if not good:
        good = []


def is_compares_identity_not_value(param):
    if param is "pooled constant":  # This may or may not work
        pass
    if param == "pooled constant":  # This will always work
        pass

