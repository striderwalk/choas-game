from draw import Draw
from point import Point
import math, random

def make_poly(num : int, dis: int, center = Point(0,0)) -> list[Point]:
    # find angle 
    angle = math.pi*2 / num 
    # find each point
    points = []
    for i in range(num): # shift ang by 90 degr to make look nice
        x = dis * math.cos(angle*i - math.pi/2)
        y = dis * math.sin(angle*i - math.pi/2)
        points.append(Point(x,y))
    return points

def frac_point(p1: Point, p2 : Point, frac : float) -> Point:
    diff = p2 - p1
    return p1 + diff * frac


def game(num: int, frac: float, iters : int) -> list:
    # find outer points
    points = make_poly(num, 200)
    for i in points: yield i

    # find first point
    Pcur = random.choice(points)

    # find all points
    for _ in range(iters):
        yield Pcur
        target = random.choice(points)
        Pcur = frac_point(Pcur, target, frac)


def main():
    sides = 5
    frac = 1/((1+math.sqrt(5)/2))
    points = [i for i in game(sides, frac, 3000)]
    
    Draw.dots(points)

if __name__ == "__main__":
    main()

