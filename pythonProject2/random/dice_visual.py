from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# создание двух кубиков D6 и D10 (можно задать два одинаковых D6)
die_1 = Die()
die_2 = Die(10)  # создание кубика с 10 гранями

# моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(50000):  # 50000 бросков кубиков с 6 и 10 гранями
    result = die_1.roll() + die_2.roll()  # вычисление суммы значений граней для каждого броска
    results.append(result)

# анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides  # сохранение максимального результата броска
for value in range(2, max_result + 1):  # от минимального результата (2) до максимального (12)
    frequency = results.count(value)
    frequencies.append(frequency)

# визуализация результатов
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}  # dtick управляет расстояниями между делениями на оси х
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
