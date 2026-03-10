def multiply_list(elements: list, factor: int = 2) -> list:
    result = []
    for item in elements:
        if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
            result.append(int(item) * factor)
        else:
            result.append(item * factor)
    return result

input_str = input("Введите список чисел через пробел: ")
factor_input = input("Введите множитель (по умолчанию 2): ")

elements = input_str.split()

if factor_input == "":
    factor = 2
else:
    factor = int(factor_input)

result_func = multiply_list(elements, factor)
result_lambda = list(map(lambda x: (int(x) if (x.isdigit() or (x.startswith('-') and x[1:].isdigit())) else x) * factor, elements))

print(f"Результат (функция): {result_func}")
print(f"Результат (лямбда-функция): {result_lambda}")