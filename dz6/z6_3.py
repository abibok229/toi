import unittest
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):
    def test_zero(self):
        """Факториал 0 должен быть равен 1."""
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        """Факториал 1 должен быть равен 1."""
        self.assertEqual(factorial(1), 1)

    def test_small_positive(self):
        """Проверка для небольших положительных чисел."""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative(self):
        """Факториал отрицательного числа вызывает ValueError."""
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_overflow(self):
        """Слишком большое число вызывает переполнение и ValueError."""
        with self.assertRaises(ValueError):
            factorial(1000)

    def test_large_within_limit(self):
        """Проверка для числа, чей факториал умещается в sys.maxsize."""
        result = factorial(20)
        self.assertIsInstance(result, int)

if __name__ == '__main__':
    unittest.main()
