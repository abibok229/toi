def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание двух чисел."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b

def divide(a: float, b: float) -> float:
    """Деление двух чисел. Проверка деления на ноль."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b

def power(a: float, b: float) -> float:
    """Возведение числа a в степень b."""
    return a ** b

def factorial(n: int) -> int:
    """Вычисление факториала целого неотрицательного числа."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал определён только для целых неотрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def modulo(a: float, b: float) -> float:
    """Остаток от деления a на b. Проверка деления на ноль."""
    if b == 0:
        raise ZeroDivisionError("Остаток от деления на ноль невозможен")
    return a % b

def average(numbers: list[float]) -> float:
    """Среднее арифметическое списка чисел."""
    if not numbers:
        raise ValueError("Список чисел пуст")
    return sum(numbers) / len(numbers)

def print_menu():
    print("\nДоступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал")
    print("7. Остаток от деления")
    print("8. Среднее арифметическое")
    print("---")
    print("Для выхода введите 'exit'")

def main():
    while True:
        print_menu()
        choice = input("Операция: ").strip()
        if choice.lower() == "exit":
            print("Выход из калькулятора.")
            break
        try:
            if choice == "1":
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                result = add(a, b)
            elif choice == "2":
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                result = subtract(a, b)
            elif choice == "3":
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                result = multiply(a, b)
            elif choice == "4":
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                result = divide(a, b)
            elif choice == "5":
                a = float(input("Введите число: "))
                b = float(input("Введите степень: "))
                result = power(a, b)
            elif choice == "6":
                n = int(input("Введите целое неотрицательное число: "))
                result = factorial(n)
            elif choice == "7":
                a = float(input("Введите делимое: "))
                b = float(input("Введите делитель: "))
                result = modulo(a, b)
            elif choice == "8":
                nums_str = input("Введите список чисел через пробел: ")
                parts = nums_str.split()
                nums = [float(x) for x in parts]
                result = average(nums)
            else:
                print("Неверный выбор. Попробуйте снова.")
                continue
            print(f">>> {result}")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()