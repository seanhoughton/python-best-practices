'''
PEP8 style helps let everyone know what to expect immediately
'''

PUBLIC_MODULE_VALUE = 100.0      # This ALLCAPS value can be read (and written to!) by outside code

__PRIVATE_MODULE_VALUE = 200.0   # This ALLCAPS value's name is mangled and is invisible to outside
                                 # code and classes defined in *this* module

def public_function():
    pass


def __private_function():
    pass


class MyDemoClass(object):
    def __private_member_function(self):
        '''This function is only visible to other member functions'''
        pass

    def public_member_function(self):
        '''This function is visible to everyone'''
        pass


