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
def test_sequence_length():
    assert 16 == len(fibo(16))


# test that fibonacci sequence is correct
def test_sequence():
    assert [0, 1, 1, 2, 3, 5] == fibo(6)
    assert [0] == fibo(1)
    assert [0, 1] == fibo(1.6)
