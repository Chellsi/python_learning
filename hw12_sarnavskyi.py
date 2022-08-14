# task1 Доопрацюйте класс Line так,
# щоб в атрибути begin та end обʼєктів цього класу можна було записати тільки обʼєкти класу Point.
# Використовуйте property

# task2 Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
# Реалізуйте перевірку даних, аналогічно до класу Line.
# Визначет атрибут, що містить площу трикутника (за допомогою property).
# Для обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)

class Point:
    _x = None
    _y = None

    @property  # getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    @property  # getter
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._y = value

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord


point1 = Point(0, 3)
point1.x = 100
point2 = Point(4, 0)
point3 = Point(3, 5)


class Line:

    _begin = None
    _end = None

    @property  # getter
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._begin = value

    @property  # getter
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._end = value

    def __init__(self, begin_point: Point, end_point: Point):
        self.begin = begin_point
        self.end = end_point

    @property
    def length(self):
        print('in length_getter')
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


class Triangle:

    _left_side = None
    _top_side = None

    @property  # getter
    def left_side(self):
        return self._left_side

    @left_side.setter
    def left_side(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._left_side = value

    @property  # getter
    def top_side(self):
        return self._top_side

    @top_side.setter
    def top_side(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._top_side = value

    def __init__(self, first_point: Point, second_point: Point, third_point: Point):
        self.left_side = first_point
        self.top_side = second_point
        self.right_side = third_point

    @property
    def area(self):
        a = ((self.left_side.x - self.top_side.x) ** 2 + (self.left_side.y - self.top_side.y) ** 2) ** 0.5
        b = ((self.top_side.x - self.right_side.x) ** 2 + (self.top_side.y - self.right_side.y) ** 2) ** 0.5
        c = ((self.right_side.x - self.left_side.x) ** 2 + (self.right_side.y - self.left_side.y) ** 2) ** 0.5
        p = a + b + c
        return (p*(p-a)*(p-b)*(p-c)) ** 0.5


line1 = Line(point2, point1)

tri1 = Triangle(point1, point2, point3)

print(line1.length)

print(tri1.area)
