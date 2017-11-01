# -*- coding: utf8 -*-

import unittest

import basic_operations as bo


class TestBasicOperations(unittest.TestCase):
    def test_str_to_int(self):
        self.assertEqual(10, bo.str_to_int("10"))
        self.assertEqual(15, bo.str_to_int("15"))
        self.assertEqual(40, bo.str_to_int("40"))
        self.assertEqual(155, bo.str_to_int("155"))

    def test_str_to_float(self):
        self.assertEqual(10.0, bo.str_to_float("10"))
        self.assertEqual(15.4, bo.str_to_float("15.4"))
        self.assertEqual(40.0, bo.str_to_float("40"))
        self.assertEqual(-132.28, bo.str_to_float("-132.28"))

    def test_number_to_str(self):
        self.assertEqual("10", bo.number_to_str(10))
        self.assertEqual("15.4", bo.number_to_str(15.4))
        self.assertEqual("40", bo.number_to_str(40))
        self.assertEqual("-132.3", bo.number_to_str(-132.3))

    def test_add_string_number(self):
        self.assertEqual("Seoul10", bo.add_string_number("Seoul", 10))
        self.assertEqual("Seoul15.4", bo.add_string_number("Seoul", 15.4))
        self.assertEqual("Seoul40", bo.add_string_number("Seoul", 40))
        self.assertEqual("Seoul-132.3", bo.add_string_number("Seoul", -132.3))

    def test_add_string_string(self):
        self.assertEqual(
            "Seoul Korea", bo.add_string_string("Seoul", " Korea"))
        self.assertEqual(
            "Hello World", bo.add_string_string("Hello", " World"))

    def test_associative_law_add(self):
        self.assertEqual(
            ((10 + 50) - 30), bo.associative_law_add(10, 50, -30))
        self.assertEqual(
            ((10 + -50) + 100), bo.associative_law_add(10, -50, 100))

    def test_associative_law_mutiple(self):
        self.assertEqual(
            ((10 * -5) * - 30), bo.associative_law_mutiple(10, -5, -30))
        self.assertEqual(
            ((-10 * -5) * - 30), bo.associative_law_mutiple(-10, -5, -30))
        self.assertEqual(
            ((-10 * -5) * 30), bo.associative_law_mutiple(-10, -5, 30))

    def test_distributive_law(self):
        self.assertEqual(
            (10 * (-5 + - 30)), bo.distributive_law(10, -5, -30))
        self.assertEqual(
            (3 * (4 + 5)), bo.distributive_law(3, 4, 5))
        self.assertEqual(
            (-10 * (-5 + -5)), bo.distributive_law(-10, -5, -5))

    def test_exponent(self):
        self.assertEqual(
            (10 ** 5), bo.exponent(10, 5))
        self.assertEqual(
            (10), bo.exponent(10, 1))
        self.assertEqual(
            (10.2 ** 5), bo.exponent(10.2, 5))
