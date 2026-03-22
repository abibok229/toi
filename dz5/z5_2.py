import random
import math
import statistics

def main() -> None:
    numbers = [random.randint(1, 100) for _ in range(100)]

    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    stdev = statistics.stdev(numbers)
    sqrt_sum = math.sqrt(sum(numbers))
    rounded_sqrt = round(sqrt_sum, 2)

    print(f"Среднее: {mean:.2f}, Медиана: {median:.2f}, "
          f"Стандартное отклонение: {stdev:.2f}, Корень из суммы: {rounded_sqrt:.2f}")

if __name__ == "__main__":
    main()
