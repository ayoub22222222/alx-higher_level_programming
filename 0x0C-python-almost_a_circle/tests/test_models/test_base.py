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
    scenario including success and flr ones
    """
    def test_random_input(self):
        pass

    def test_empty_base(self):
        empty1 = Base()
        empty2 = Base()
        empty3 = Base()
        self.assertEqual(print(empty1.id), 1)
        self.assertEqual(print(empty2.id), 2)
        self.assertEqual(print(empty3.id), 3)

    def test_basic_int_input(self):
        """this methode test tree
        random integer"""
        basic1 = Base(14)
        basic2 = Base(15)
        basic3 = Base(111)
        self.assertEqual(print(basic1.id), 14)
        self.assertEqual(print(basic2.id), 15)
        self.assertEqual(print(basic3.id), 111)

    def test_basic_str_input(self):
        """test string input"""
        pass

    def test_large_number(self):
        """test large number"""
        large = Base(100000000000000)
        self.assertEqual(print(large.id), 100000000000000),
    
    def test_bolean_value(self):
        """test bolean value"""
        bol1 = Base(True)
        bol2 = Base(False)
        self.assertFalse(print(bol2.id), False)
        self.assertTrue(print(bol1.id), True)

    def test_None_value(self):
        """test None input"""
        n = Base(None)
        self.asserIsNone(print(n.id), "expected to be None")
        
    def test_list_input(self):
        """test list input"""
        lst = Base([1, 2, 3])
        self.assertEqual(print(lst.id), [1, 2, 3])
    
    def test_dict_value(self):
        """test dictionnairies input"""
        dct = Base({"value_one": 1, "value_two": 2})
        self.assertEqual(print(dct.id), {"value_one": 1, "value_two": 2})

    def test_tuple_input(self):
        """test tuple input"""
        self.assertEqual(Base((1, 2, 3), (1, 2, 3))
    

    def test_syntax_error(self):
        """test syntax error"""
        syn = Base($)
        with self.assertRaises(SyntaxError):
            print(Base($).id)

if __name__ == "__main__":
    unittest.main()
