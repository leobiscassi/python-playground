class Rectangle:
    """A class to manufacture rectangle objects"""
    def __init__(self, posn, w, h):
        """Initialize rectangle at posn, with width w, height h"""
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return f"({self.corner}, {self.width}, {self.height})"

    def grow(self, delta_width, delta_height):
        """Grow (or shrink) this object by the deltas"""
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """Move this object by the deltas"""
        self.corner.x += dx
        self.corner.y += dy

