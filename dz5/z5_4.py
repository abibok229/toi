import random
import datetime
from array import array

def main() -> None:
    today = datetime.date.today()
    five_years_ago = today - datetime.timedelta(days=365 * 5)

    total_days = (today - five_years_ago).days

    offsets = [random.randint(0, total_days) for _ in range(10)]

    date_array = array('i', offsets)

    dates = [five_years_ago + datetime.timedelta(days=offset) for offset in date_array]

    for i in range(len(dates) - 1):
        diff = abs((dates[i+1] - dates[i]).days)
        print(f"Разница между {dates[i]} и {dates[i+1]}: {diff} дней")

if __name__ == "__main__":
    main()
