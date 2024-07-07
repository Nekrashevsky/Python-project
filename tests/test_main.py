import unittest
from calculator import evaluate_expression

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(evaluate_expression("2 + 2"), 4)
        self.assertEqual(evaluate_expression("10 + 5"), 15)
        self.assertEqual(evaluate_expression("0 + 0"), 0)

    def test_subtraction(self):
        self.assertEqual(evaluate_expression("5 - 3"), 2)
        self.assertEqual(evaluate_expression("10 - 10"), 0)
        self.assertEqual(evaluate_expression("0 - 5"), -5)

    def test_invalid_expression(self):
        self.assertIsInstance(evaluate_expression("2 +"), str)
        self.assertIsInstance(evaluate_expression("5 -"), str)
        self.assertIsInstance(evaluate_expression("invalid"), str)

if __name__ == "__main__":
    unittest.main()
