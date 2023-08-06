#!/usr/bin/env python3

from not_none_functions import return_not_none

# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False
# testing/test_not_none.py

 # testing/test_not_none.py

from not_none_functions import return_not_none

def test_return_not_none():
    result = return_not_none()
    assert result is not None, "Function should not return None"
    assert isinstance(result, str), "Function should return a string"
# testing/not_none_functions.py

def return_not_none():
    return "Hello, this is not None!"
