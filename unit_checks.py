import unittest
from Pr1_Biriuk import calculate


class TestCalculator(unittest.TestCase):
    """
    Клас для тестування калькулятора
    Наслідується від unittest.TestCase
    """

    def test_addition(self):
        """Тест перевірки додавання"""
        self.assertEqual(calculate("2+3"), 5)

    def test_subtraction(self):
        """Тест перевірки віднімання"""
        self.assertEqual(calculate("10-5"), 5)

    def test_multiplication(self):
        """Тест перевірки множення"""
        self.assertEqual(calculate("3*4"), 12)

    def test_division(self):
        """Тест перевірки ділення"""
        self.assertEqual(calculate("8/2"), 4)

    def test_division_by_zero(self):
        """Тест перевірки ділення на нуль"""
        with self.assertRaises(ZeroDivisionError):
            calculate("5/0")

    def test_invalid_expression(self):
        """Тест перевірки некоректного виразу"""
        with self.assertRaises(ValueError):
            calculate("2+*3")


if __name__ == "__main__":
    unittest.main()