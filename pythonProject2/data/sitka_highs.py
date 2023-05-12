import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)  # метод для создания объекта чтения данных из файла
    header_row = next(reader)  # получение только первой строки файла с заголовками

    # чтение максимальных температур и дат из файла
    dates, highs = [], []
    for row in reader:  # перебор остальных строк в файле
        current_date = datetime.strptime(row[2], "%Y-%m-%d")  # данные из 2 позиции (дата) в объект datetime
        high = int(row[4])  # значение с индексом 4 присваивается high
        dates.append(current_date)
        highs.append(high)

# нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')  # вызов plot с аргументами highs, dates

# форматирование диаграммы
plt.title("Daily high temperatures, 2021", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # вывод меток дат по диагонали, чтобы не перекрывались
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# for index, column_header in enumerate(header_row): # возвращает индекс и его значение при переборе списка
#     print(index, column_header)
