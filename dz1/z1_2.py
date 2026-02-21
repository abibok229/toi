s = input("Введите число: ").strip()
if s and ((s[0] == '-' and s[1:].isdigit()) or s.isdigit()):
    n = int(s)
    print(f"Число {n} {'является' if n % 2 == 0 else 'не является'} четным")
else:
    print("Ошибка: введено не число")
