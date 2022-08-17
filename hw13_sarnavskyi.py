# task1 Доопрацюйте класс Triangle з попередньої домашки наступним чином:
# обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=)
# print() обʼєкту классу Triangle показує координати його вершин
# print(triangle1)
# > (Point(1,0) Point(5,9) Point(3,3))

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
point4 = Point(4, 6)


class Line:

    _begin = None
    _end = None

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._begin = value

    @property
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
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


class Triangle:

    _left_point = None
    _top_point = None
    _right_top = None

    @property
    def left_point(self):
        return self._left_point

    @left_point.setter
    def left_point(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._left_point = value

    @property
    def top_point(self):
        return self._top_point

    @top_point.setter
    def top_point(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._top_point = value

    @property
    def right_point(self):
        return self._right_point

    @right_point.setter
    def right_point(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._right_point = value

    def __init__(self, first_point: Point, second_point: Point, third_point: Point):
        self.left_point = first_point
        self.top_point = second_point
        self.right_point = third_point

    @property
    def area(self):
        a = ((self.left_point.x - self.top_point.x) ** 2 + (self.left_point.y - self.top_point.y) ** 2) ** 0.5
        b = ((self.top_point.x - self.right_point.x) ** 2 + (self.top_point.y - self.right_point.y) ** 2) ** 0.5
        c = ((self.right_point.x - self.left_point.x) ** 2 + (self.right_point.y - self.left_point.y) ** 2) ** 0.5
        p = (a + b + c) / 2
        return (p*(p-a)*(p-b)*(p-c)) ** 0.5

    def __eq__(self, other):
        return self.area == other.area

    def __ge__(self, other):
        return self.area >= other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __repr__(self):
        return f'(Point ({self.left_point.x},{self.left_point.y}) ' \
               f'Point ({self.right_point.x},{self.right_point.y}) ' \
               f'Point ({self.top_point.x},{self.top_point.y}))'


line1 = Line(point2, point1)

tri1 = Triangle(point1, point2, point3)

tri2 = Triangle(point1, point2, point4)

print(tri1 > tri2)
print(tri1)
