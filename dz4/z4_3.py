def append_to_file(text: str, filename: str) -> None:
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f.readlines(), start=1):
            if i % 2 == 0:
                print(line, end='')

if __name__ == "__main__":
    filename = "example.txt"
    append_to_file("Новая строка", filename)
