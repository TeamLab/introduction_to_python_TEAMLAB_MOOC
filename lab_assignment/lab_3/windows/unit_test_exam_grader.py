# -*- coding: utf8 -*-

import unittest

import exam_grader as eg
from unittest.mock import patch


class TestExamGrder(unittest.TestCase):
    def test_get_number_of_subjects(self):
        with patch('builtins.input', side_effect=['10']):
            result = eg.get_number_of_subjects()
            self.assertEqual(10, result)

        with patch('builtins.input', side_effect=['y']):
            with self.assertRaises(ValueError):
                eg.get_number_of_subjects()

        with patch('builtins.input', side_effect=['3']):
            result = eg.get_number_of_subjects()
            self.assertEqual(3, result)

    def test_get_average_score(self):
        result = eg.get_average_score(500, 5)
        self.assertEqual(100.0, result)

        result = eg.get_average_score(355, 5)
        self.assertEqual(71.0, result)

        result = eg.get_average_score(100, 3)
        self.assertEqual(100 / 3, result)
