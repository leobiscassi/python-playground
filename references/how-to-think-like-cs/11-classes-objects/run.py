from points import Point
from rectangles import Rectangle
from mytime import MyTime, add_time, increment

if __name__ == '__main__':
    '''
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
    '''

    tim1 = MyTime(11, 59, 30)
    print(tim1)

    current_time = MyTime(9, 65, 30)
    bread_time = MyTime(3, 35, 0)
    done_time = add_time(current_time, bread_time)
    print(done_time)

    print(tim1)
    tim1.increment(121)
    print(tim1)