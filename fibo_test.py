import pytest

from fibo import *


# test the user's input is not a string
def test_string_input():
    assertTrue = checkString('fibo')


# check that float input is correctly identified
def test_float_input():
    assertTrue = checkFloat(5.3)


# test that a float input is rounded to nearest 10
def test_float_input_is_rounded():
    assert 5 == roundFloat(5.3)


# test that the fibonacci sequence is up to nth number
# test that fibonacci sequence is correct
