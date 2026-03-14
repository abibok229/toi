import math

# список квадратов первых 10 натуральных чисел
squares = [i**2 for i in range(1, 11)]
print("1.", squares)

# словарь дней недели
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day_dict = {day: index+1 for index, day in enumerate(days)}
print("2.", day_dict)

# множество тегов библиотек в нижнем регистре
tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags_set = {tag.lower() for tag in tags}
print("3.", tags_set)

# список четных чисел
numbers = [1, 3, 4, 87, 98, 15, 7, 4]
evens = [x for x in numbers if x % 2 == 0]
print("4.", evens)

# словарь факториалов
factorials = {n: math.factorial(n) for n in range(1, 6)}
print("5.", factorials)
