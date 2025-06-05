import unittest

from src.calculator import suma, resta, multiplicación, division

class CalculatorTest(unittest.TestCase):
   
    def test_sum(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)

    def test_multiplicación(self):
        self.assertEqual(multiplicación(5, 5), 25)

    def test_division(self):
        self.assertEqual(division(10, 5), 2)