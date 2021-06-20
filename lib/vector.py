class Vector:
    def __init__(self, x: int, y: int) -> object:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "({};{})".format(self.x, self.y)

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, o: object) -> object:
        return Vector(self.x + o.x, self.y + o.y)

    def __abs__(self) -> int:
        return self.distance(Vector(0, 0))

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y

    def __hash__(self) -> int:
        return hash(str(self))

    def distance(self, o: object) -> int:
        return abs(o.x - self.x) + abs(o.y - self.y)