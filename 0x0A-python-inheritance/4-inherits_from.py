#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class.
    """
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
