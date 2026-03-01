input_str = input("Введите числа через пробел: ")
step = int(input("Введите степень: "))


elements = input_str.split()

results = []

for item in elements:
    if item.startswith('-') and item[1:].isdigit():
        num = int(item)
        results.append(num ** step)
    elif item.isdigit():
        num = int(item)
        results.append(num ** step)
    else:
        results.append(item * step)

print("Вывод:", *results)
