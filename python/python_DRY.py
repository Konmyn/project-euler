#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


class CalcTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 842
        self.b = 439

    def tearDown(self):
        pass

    def test_add(self):
        self.assertTrue(add(self.a, self.b), self.a + self.b)

    def test_sub(self):
        self.assertTrue(subtract(self.a, self.b), self.a - self.b)

    def test_mul(self):
        self.assertTrue(multiply(self.a, self.b), self.a * self.b)

    def test_div(self):
        self.assertTrue(divide(self.a, self.b), self.a / self.b)

if __name__ == "__main__":
    unittest.main()
