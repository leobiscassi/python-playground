class Point:
    """Create a new Point, at coordinates x, y"""
    def __init__(self, x=0, y=0):
        """Create a new point at x, y"""
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

    def distance_from_origin(self):
        """Compute my distance from the origin"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        """Return the halfway point between myself and the target"""
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2

        return Point(mx, my)