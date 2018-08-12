"""

You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to:
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

EXAMPLE:
Input : [(0, 0), (1, 1), (1, 2)]
Output : 2

"""

# IDEA: Every new point can be achieved at, at worst, 1 step. So if the next point is different (IDC how), I will need
# and extra step. Repeat these for every new point.


# I'll assume points are always well-constructed. That is, they always have an x and a y coordinate.
def minimum_steps_to_traverse_grid(points):
    steps_required = 0
    if not points:
        return steps_required
    for i in range(len(points) - 1):
        if points[i] != points[i+1]:
            steps_required += 1
    if points[-1] != points[-2]:
        steps_required += 1
    return steps_required


class Point(object):
    def __init__(self, x, y):
        if x is None or y is None:
            raise ValueError("Point is missing coordinates x or y.")
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def __ne__(self, other):
        return self.x() != other.x() or self.y() != other.y()
