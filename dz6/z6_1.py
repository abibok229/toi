def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, (int, float)):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)


# 1. Целые числа
assert average_num([1, 2, 3]) == 2.0

# 2. Числа с плавающей точкой
assert average_num([2.5, 3.5]) == 3.0

# 3. Смесь int и float
assert average_num([1, 2.5, 3]) == 2.17

# 4. Строковые представления чисел
assert average_num(["1", "2", "3"]) == 2.0

# 5. Некорректная строка – возврат "Bad request"
assert average_num([1, "abc", 3]) == "Bad request"

# 6. Отрицательные числа
assert average_num([-5, -10, -15]) == -10.0

# 7. Один элемент
assert average_num([7]) == 7.0

# 8. Float с большой точностью (округление)
assert average_num([1.234, 2.345]) == 1.79

print("Все тесты пройдены")
