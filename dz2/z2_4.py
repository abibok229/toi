text = input("Введите строку: ")

words = text.split()

word_count = {}

for word in words:
    lower_word = word.lower()
    if lower_word in word_count:
        word_count[lower_word] += 1
    else:
        word_count[lower_word] = 1

for word, count in word_count.items():
    print(f"{word}: {count}")
