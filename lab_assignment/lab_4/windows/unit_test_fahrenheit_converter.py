# -*- coding: utf8 -*-

import unittest

import fahrenheit_converter as fc

from unittest.mock import patch
from io import StringIO


class TestExamGrder(unittest.TestCase):
    def test_input_celsius_value(self):
        with patch('builtins.input', side_effect=['32.2']):
            result = fc.input_celsius_value()
            self.assertEqual(32.2, result)

        with patch('builtins.input', side_effect=['y']):
            with self.assertRaises(ValueError):
                result = fc.input_celsius_value()
                self.assertEqual(32.2, result)

        with patch('builtins.input', side_effect=['30']):
            result = fc.input_celsius_value()
            self.assertEqual(30.0, result)

    def test_convert_celsius_fahrenheit(self):
        celsius_value = 32.2
        result = fc.convert_celsius_fahrenheit(celsius_value)
        fah = ((9 / 5) * celsius_value) + 32
        self.assertEqual(fah, result)

        celsius_value = 15.2
        result = fc.convert_celsius_fahrenheit(celsius_value)
        fah = ((9 / 5) * celsius_value) + 32
        self.assertEqual(fah, result)

        celsius_value = 64.2
        result = fc.convert_celsius_fahrenheit(celsius_value)
        fah = ((9 / 5) * celsius_value) + 32
        self.assertEqual(fah, result)

    def test_print_fahrenheit_value(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            fc.print_fahrenheit_value(10, 10.5)
            self.assertIn('섭씨온도', fakeOutput.getvalue().strip())
            self.assertIn('화씨온도', fakeOutput.getvalue().strip())
            self.assertIn('10', fakeOutput.getvalue().strip())
            self.assertIn('10.5', fakeOutput.getvalue().strip())

    def test_main(self):
        with patch('builtins.input', side_effect=['32.2']):
            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                fc.main()
                fah = ((9 / 5) * 32.2) + 32
                self.assertIn('섭씨온도', fakeOutput.getvalue().strip())
                self.assertIn('화씨온도', fakeOutput.getvalue().strip())
                self.assertIn(str(32.2), fakeOutput.getvalue().strip())
                self.assertIn(str(fah), fakeOutput.getvalue().strip())

        with patch('builtins.input', side_effect=['56.2']):
            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                fc.main()
                fah = ((9 / 5) * 56.2) + 32
                self.assertIn('섭씨온도', fakeOutput.getvalue().strip())
                self.assertIn('화씨온도', fakeOutput.getvalue().strip())
                self.assertIn(str(56.2), fakeOutput.getvalue().strip())
                self.assertIn(str(fah), fakeOutput.getvalue().strip())
