'''
Partials let you "pre-fill-out" values and give you a
function you can call without that value.
'''

from functools import partial

def __get_p4_path(p4_connection, filename):
    result = p4_connection.run(['where', filename])[0]['path']


def procedural_version(p4_connection, files):
    result = []
    for filename in files:
        result.append(__get_p4_path(p4_connection, filename))
    return result


def functional_version(p4_connection, files):
    get_path = partial(__get_p4_path, p4_connection)
    return apply(get_path, files)

