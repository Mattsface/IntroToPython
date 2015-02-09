#!/usr/bin/env python


import unittest
from make_bricks import make_bricks

class MyTests(unittest.TestCase):
    def test_make_bricks_one(self):
        test_vals = (3, 1, 8)
        expected = True
        actual = make_bricks(*test_vals)
        self.assertEquals(expected, actual)

    def test_make_bricks_two(self):
        test_vals = (3, 1, 9)
        expected = False
        actual = make_bricks(*test_vals)
        self.assertEquals(expected, actual)

    def test_make_bricks_three(self):
        test_vals = (3, 2, 10)
        expected = True
        actual = make_bricks(*test_vals)
        self.assertEquals(expected, actual)

    def test_make_bricks_four(self):
        test_vals = (3, 2, 9)
        expected = False
        actual = make_bricks(*test_vals)
        self.assertEqual(expected, actual)

    def test_make_bricks_five(self):
        test_vals = (1, 4, 12)
        expected = False
        actual = make_bricks(*test_vals)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()