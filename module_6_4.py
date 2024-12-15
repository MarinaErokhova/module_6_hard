from math import pi, sqrt

class Figure:
    sides_count = 0
    def __init__(self, color, *sides, sides_count=0):
        self.sides_count = sides_count
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = None

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r,int) and isinstance(g,int) and isinstance(b,int):
            return True
        elif r in range(0, 255) and g in range(0, 255) and b in range(0, 255):
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r,g,b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        if len(sides)!= self.sides_count:
            return False
        for i in sides:
            if not (isinstance(i , int) and i > 0):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides
        self.__radius = self.__sides[0] / (2*pi)

    def get_square(self):
        return (self.__radius ** 2) * pi

class Triangle(Figure):
    sides_count = 3
    __height = None

    def __init__(self, color, *sides):
        super().__init__(color, sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = [sides[0]] * self.sides_count  # переопределение __sides
        print(self.__sides)

    def get_volume(self):
        return self.__sides[0] ** 3

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
