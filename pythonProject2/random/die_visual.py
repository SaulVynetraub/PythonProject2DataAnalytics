from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# создание кубика D6
die = Die()

# моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):
    result = die.roll()  # вызов метода броска кубика из класса Die
    results.append(result)

# анализ результатов
frequencies = []  # список для сохранения результатов по выпавшим граням
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)  # сколько раз выпало каждое число (количество вхождений)
    frequencies.append(frequency)

# визуализация результатов
x_values = list(range(1, die.num_sides + 1))  # создание столбцов для каждого результата (от 1 грани до 6)
data = [Bar(x=x_values,
            y=frequencies)]  # набор данных для формирования гистограммы (х - 6 граней, у - частота выпадения каждой)

x_axis_config = {'title': 'Result'}  # конфигурация оси х: название
y_axis_config = {'title': 'Frequency of result'}  # конфигурация оси у
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)  # задание макета и конфигурации гистограммы в целом
offline.plot({'data': data, 'layout': my_layout},
             filename='d6.html')  # функция построения гистограммы: data - данные для построения,
# layout - описание макета, filename - имя сохраняемого файла
