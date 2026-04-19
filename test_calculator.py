import unittest
from calculator import (
    add, subtract, mul, div,
    logarithm, exp, square_root, hypotenuse
)
class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -3), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        import math
        self.assertAlmostEqual(logarithm(math.e, math.e), 1.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)
        self.assertAlmostEqual(mul(0.5, 0.4), 0.2)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5.0)
        self.assertAlmostEqual(div(4, 1), 0.25)
        self.assertAlmostEqual(div(-2, 6), -3.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, 0)
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)
        self.assertAlmostEqual(hypotenuse(0, 7), 7.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
        self.assertEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
