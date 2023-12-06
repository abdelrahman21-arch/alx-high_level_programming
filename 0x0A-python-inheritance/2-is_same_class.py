# 2-is_same_class.py
# sweilam
""" checks if the class is same or not """


def is_same_class(obj, a_class):
    """ check if an object is an instance of the given class.
    
    Args:
         obj (any): the object to check.
         a_class (type): The class to match obj type
    Returns:
           if obj match 1 otherwise 0.
    """
    if type(obj) == a_class):
        return True
    return False
