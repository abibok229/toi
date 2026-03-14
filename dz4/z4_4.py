def info_decorator(func):
    def deco(*args, **kwargs):
        print(f"Функция `{func.__name__}` вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
        return result
    return deco

@info_decorator
def calculate_area(length: float, width: float) -> float:
    return length * width

if __name__ == "__main__":
    calculate_area(5, 10)
