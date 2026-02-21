name = input("Ваше имя: ")
surname = input("Фамилия: ")
age = input("Возраст: ")

print("Реализация через format:")
print("Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(name, surname, age))

print("Реализация через f-string:")
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет")
