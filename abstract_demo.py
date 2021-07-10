from abc import ABC, abstractmethod


class GraphicShape:
    def __init__(self):
        super().__init__();

    @abstractmethod
    def calArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius;

    def calArea(self):
        return 3.14 * (self.radius ** 2);


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side;

    def calArea(self):
        return self.side * self.side;


c = Circle(10);
print(c.calArea());

s = Square(20);
print(s.calArea());