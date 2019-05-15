from points import Point
from rectangles import Rectangle

if __name__ == '__main__':
    box = Rectangle(Point(0, 0), 100, 200)
    bomb = Rectangle(Point(100, 80), 5, 10)

    print("box: ", box)
    print("bomb: ", bomb)
    box.width += 50
    box.height += 100
    print("box: ", box)

    r = Rectangle(Point(10, 5), 100, 50)
    print("r: ", r)
    r.grow(25, -10)
    print("r: ", r)
    r.move(-10, 10)
    print("r: ", r)

    p1 = Point(3, 4)
    p2 = Point(3, 4)

    print("p1 is p2? ", p1 is p2)

    p3 = p1
    print("p1 is p3? ", p1 is p3)

    print("== on Points p1 and p2 returns ", p1 == p2)

    a = [2, 3]
    b = [2, 3]
    print("== on lists a and b returns ", a == b)