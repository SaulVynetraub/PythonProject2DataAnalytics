import matplotlib.pyplot as plt

from random_walk import RandomWalk

# новые блуждания строятся до тех пор, пока активна программа
while True:
    # построение случайного блуждания
    rw = RandomWalk(150000)  # создание объекта класса
    rw.fill_walk()

    # нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)  # адаптация диаграммы под разрешение экрана
    point_numbers = range(rw.num_points)  # генерирование списка чисел по числу точек в блуждании
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none',
               s=1)  # c - число точек для отображения, cmap - цветовая карта, edgecolors - удаление черного контура точек

    # выделение первой и последней точек
    ax.scatter(0, 0, c='blue', edgecolors='none', s=150)  # прорисовка старта блуждания
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none', s=150)  # прорисовка конечной точки

    # удаление осей
    ax.get_xaxis().set_visible(False)  # ax.get_xaxis() - переводит флаг видимости оси х в False
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
