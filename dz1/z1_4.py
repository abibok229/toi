while True:
    s = input("Введите число: ").strip()
    if s == "exit":
        print("Выход из программы...")
        break
    if s.lstrip('-').isdigit():
        print(f"В этом числе {len(s.lstrip('-'))} цифр.")
    else:
        print("Ошибка: данные не являются числом.")
