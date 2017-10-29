import unittest

import arithmetic_function


class TestArithmeticFunction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(8, arithmetic_function.addition(3, 5))
        self.assertEqual(65, arithmetic_function.addition(60, 5))
        self.assertEqual(43, arithmetic_function.addition(20, 23))
        self.assertEqual(-23, arithmetic_function.addition(0, -23))

    def test_minus(self):
        self.assertEqual(-2, arithmetic_function.minus(3, 5))
        self.assertEqual(55, arithmetic_function.minus(60, 5))
        self.assertEqual(-3, arithmetic_function.minus(20, 23))
        self.assertEqual(23, arithmetic_function.minus(0, -23))

    def test_multiplication(self):
        self.assertEqual(50, arithmetic_function.multiplication(10, 5))
        self.assertEqual(0, arithmetic_function.multiplication(0, -23))
        self.assertEqual(144, arithmetic_function.multiplication(12, 12))

    def test_division(self):
        self.assertEqual(float(2), arithmetic_function.division(10, 5))
        self.assertEqual(10/6.0, arithmetic_function.division(10, 6))
        self.assertEqual(12/float(12), arithmetic_function.division(12, 12))
