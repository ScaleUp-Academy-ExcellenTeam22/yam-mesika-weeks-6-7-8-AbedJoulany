from collections.abc import Iterable

"""
   The code will return a dictionary while:
   The keys are the values returned from the function passed as the first parameter.
   The value to a particular key is a list of all the organs for which the value appearing in the key is repeated.
"""


def group_by(function_to_call : callable , iter : Iterable) -> dict:
    """
    The function will return a dictionary while:
    The keys are the values returned from the function passed as the first parameter.
    The value to a particular key is a list of all the organs for which the value appearing in the key is repeated.
    :param function_to_call: function to run on the values
    :param iter: iterable to get the values from
    :return: dictionary
    """
    my_dict = {}
    for iter in iter:
        my_dict.setdefault (function_to_call (iter), []).append (iter)
    return my_dict


if __name__ == '__main__':
    print (group_by (len, ["hi", "bye", "yo", "try"]))
