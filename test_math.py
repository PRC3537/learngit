import smath
import pytest


def test_add():
    assert smath.add(1, 2) == 3


def test_add1():
    assert smath.add(1, 2) != 90


def test_func():
    assert smath.func(3) == 4


def test_func1():
    assert smath.func(3) != 5

