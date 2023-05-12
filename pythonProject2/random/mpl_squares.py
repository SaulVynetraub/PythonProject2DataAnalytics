import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25] # хранение данных для графика (ось у)
# input_values = [1, 2, 3, 4, 5] # переопределение точек построения (не с 0) (ось х)
# x_values = [1, 2, 3, 4, 5] # задание координат для точек вручную списком
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))  # задание диапазона по x автоматически
y_values = [x ** 2 for x in x_values]  # вычисление функции (квадрат) по y
plt.style.use('seaborn')  # применение цветовой схемы для поля диаграммы
fig, ax = plt.subplots()  # функция для генерации поддиаграмм на 1 диаграмме
# ax.scatter(x_values, y_values, c='red', s=10) # нанесение точек на диаграмму, 10 - размер точек, c - цвет
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10) # со своей цветовой схемой
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)  # с цветовой картой, градиент по возрастанию у
# ax.plot(input_values, squares, linewidth=3) # построение осмысленного граф. представления для чисел по вручную заданным данным

# назначение заголовка диаграммы и меток осей
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# назначение шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)

# назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 1100000])  # минимум и максимум по осям х и у

plt.show()  # вызов графика по данным
# plt.savefig('squares_plot.png', bbox_inches='tight') # сохранение диаграммы в файле, 1 - имя файла, 2 - отсекает лишнее пространство
