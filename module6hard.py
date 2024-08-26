import math


class Figure:

    def __init__(self, color, sides: int, filled=True):
        self.sides_count = 0
        self._sides = sides
        self._color = color
        self.filled = filled

    def get_color(self):
        return self._color

    def _is_valid_color(self, r, g, b):
        return (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
                and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255)

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]

    def _is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *new_count):
        if self._is_valid_sides(*new_count):
            self._sides = list(new_count)


class Circle(Figure):
    def __init__(self, color, sides: int, filled=True):
        super().__init__([color], sides, filled)
        self.sides_count = 1
        self._radius = sides / (2 * math.pi)

    def get_square(self):
        return math.pi * self._radius ** 2


class Triangle(Figure):

    def __init__(self, color, sides: int, filled=True):
        super().__init__([color], sides, filled)
        self.sides_count = 3
        self._height = self._calculate_height()

    def _calculate_height(self):
        a, b, c = self._sides
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return (2 * s) / 2

    def get_square(self):
        return 0.5 * self._sides[0] * self._height


class Cube(Figure):

    def __init__(self, color, sides: int, filled=True):
        super().__init__([color], [sides] * 12, filled)
        self.sides_count = 12
        self._sides = [sides] * 12

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and self._is_valid_sides(new_sides[0]):
            self._sides = [new_sides[0]] * 12

    def get_volume(self):
        return self._sides[0] ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())