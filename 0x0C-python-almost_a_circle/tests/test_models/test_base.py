#!/usr/bin/python3
"""this file is conatain all
the tests that will be performed to test
our code to make sure that all the output
work as expected
"""
from models.base import Base
import unittest


class TestBaseClass(unittest.TestCase):
    """this class iherante from the unittest class and
    use the TestCase methode to test different type of
    scenario
    """
    def test_is_equal(self):
        x1 = Base()
        x2 = Base()
        x3 = Base()
        x4 = Base(12)
        x5 = Base()
        self.assertEqual(x1, 1)
        pass

    pass
