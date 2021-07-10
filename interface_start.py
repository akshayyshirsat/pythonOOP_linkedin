from abc import ABC, abstractmethod


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass;


class GraphicShape(ABC):
    def __init__(self):
        super().__init__();

    @abstractmethod
    def calArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius;

    def calArea(self):
        return 3.14 * (self.radius ** 2);

    def toJSON(self):
        return f"{{\" Circle\" : {str(self.calArea())} }}"


c = Circle(10);
print(c.calArea());
print(c.toJSON());
