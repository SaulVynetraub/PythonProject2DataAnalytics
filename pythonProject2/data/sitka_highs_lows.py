import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # получение дат, температурных min и max из файла
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.plot(dates, highs, c='red', alpha=0.5)  # alpha - степень прозрачности вывода
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)  # facecolor определяет цвет закрашиваемой области

# форматирование диаграммы
plt.title("Daily high and low temperatures, 2021", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
