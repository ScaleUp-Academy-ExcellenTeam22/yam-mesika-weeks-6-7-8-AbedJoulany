from collections.abc import Iterable

"""
   The code will return a dictionary while:
   The keys are the values returned from the function passed as the first parameter.
   The value to a particular key is a list of all the organs for which the value appearing in the key is repeated.
"""


def group_by(func : callable , iterable : Iterable) -> dict:
    """
    The function will return a dictionary while:
    The keys are the values returned from the function passed as the first parameter.
    The value to a particular key is a list of all the organs for which the value appearing in the key is repeated.
    :param func: function to run on the values
    :param iterable: iterable to get the values from
    :return: dictionary
    """
    my_dict = {}
    for iter in iterable:
        my_dict.setdefault (func (iter), []).append (iter)
    return my_dict


if __name__ == '__main__':
    print (group_by (len, ["hi", "bye", "yo", "try"]))
