from random import choice


class RandomWalk():
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_points=10000):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points

        # все блуждания начинаются с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания."""

        # шаги генерируются до достижения нужной длины
        while len(self.x_values) < self.num_points:

            # определение направления и длины перемещения
            x_direction = choice([1, -1])  # 1 для перемещения вправо, -1 - влево
            x_distance = choice([0, 1, 2, 3, 4])  # случайный выбор дальности перемещения
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # отклонение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # вычисление следующих значений х и у
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
