first_input = input("Введите первый список: ")
second_input = input("Введите второй список: ")

first_list = [int(x) for x in first_input.split()]
second_list = [int(x) for x in second_input.split()]

common_elements = set(first_list) & set(second_list)

print("Общие элементы:", *common_elements)
