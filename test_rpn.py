#!/usr/bin/env python3

# Alexandra Brown
# alexbro
# eecs398 w17 week 10

import unittest
import rpn


class TestBasics(unittest.TestCase):

    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_subtract(self):
        result = rpn.calculate('5 3 -')
        self.assertEqual(2, result)

    def test_multiply(self):
        result = rpn.calculate('2 3 *')
        self.assertEqual(6, result)

    def test_divide(self):
        result = rpn.calculate('10 5 /')
        self.assertEqual(2, result)

    def test_power(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)
