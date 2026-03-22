import random
import string
from pathlib import Path

def main() -> None:
    dir_path = Path.home() / "Desktop" / "dz5" / "random files"
    dir_path.mkdir(parents=True, exist_ok=True)

    chars = string.ascii_letters + string.digits
    created_files = []

    for _ in range(10):
        while True:
            random_name = ''.join(random.choices(chars, k=8)) + ".txt"
            file_path = dir_path / random_name
            if not file_path.exists():
                break
        file_path.touch()
        created_files.append(file_path)

    for path in created_files:
        print(path.absolute())

if __name__ == "__main__":
    main()
