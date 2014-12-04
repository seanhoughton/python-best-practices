from collections import namedtuple

# Use a namedtuple for slightly stronger typing
User = namedtuple('User', ['is_superadmin', 'is_siteadmin', 'is_staff'])


def complex_boolean_logic(user):
    '''Multiple "or" comparisons'''
    return user.is_superadmin or user.is_siteadmin or user.is_staff


def simple_boolean_logic(user):
    '''Use a set operation to simplify'''
    return any([user.is_superadmin, user.is_siteadmin, user.is_staff])  # could also use "all()"


if __name__ == "__main__":
    user = User(is_superadmin=False, is_staff=True, is_siteadmin=False)
    for x in range(0, 100000):
        complex_boolean_logic(user)
    for x in range(0, 100000):
        simple_boolean_logic(user)
