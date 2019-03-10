"""

Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.

NOTE: This exercise is very vague in it's composition. It is paramount to ask for examples of the two dimensional array.

QUESTIONS TO ASK:
+ Can the array be None or empty? (For this exercise, let's assume it can be both and we should raise an exception.)
+ Can the array be one dimensional? (For this exercise, let's assume it can't.)
+ Can the colors be invalid? (For this exercise, let's assume they can't.)
+ Can the given point be outside of the screen? (For this exercise, let's assume it can't)

"""


# The problem says to fill "all the area". Recursion comes to mind first.

# We are given the beggining_point. I asume to have a function get_color(point) that allows me to know
# the color of the beggining point. I need this because, for example, if the point is blue and the new color is red,
# I knoW I need to paint fill the surrounding blue area (because it can be of many different colors).

# The idea is to check if screen.color(point) matches the original color. If it does, I paint it with the new color.
# Once that is done, I move in the four directions. That is, x+1, x-1, y+1, y-1. Basically create four other points
# and try to paint fill there.

class Point:
    @classmethod
    def create(cls, x, y):
        point = cls(x, y)
        return point

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y


class Color:
    @classmethod
    def white(cls):
        return (255, 255, 255)

    @classmethod
    def red(cls):
        return (255, 0, 0)

    @classmethod
    def green(cls):
        return (0, 255, 0)

    @classmethod
    def blue(cls):
        return (0, 0, 255)

    @classmethod
    def yellow(cls):
        return (255, 255, 0)


class Screen:
    @classmethod
    def create(cls, surface_size):
        screen = cls(surface_size)
        return screen

    def __init__(self, surface_size):
        self._surface = [[Color.white() for _ in surface_size] for _ in surface_size]

    def surface(self):
        return self._surface

    def color(self, point):
        return self.surface()[point.x][point.y]

    def change_color_of(self, point, new_color):
        self.surface()[point.x()][point.y()] = new_color


class Painter:
    def paint_fill(self, screen, beggining_point, new_color):
        self._check_for_invalid_screen(screen)
        original_color = screen.color(beggining_point)  # This would throw IndexError if the point was out of the screen
        self.paint_in_all_directions(beggining_point, screen, original_color, new_color)

    def _check_for_invalid_screen(self, screen):
        if not screen or len(screen) == 0:
            raise ValueError("Screen is invalid.")

    def paint_in_all_directions(self, current_point, screen, original_color, new_color):
        if screen.color(current_point) == original_color:
            screen.change_color_of(current_point, new_color)
            # I only want to paint in all directions if the current position was painted.
            # Otherwise I would be not be filling an entire zone, because it would be separated by current_point
            self.paint_in_all_directions(Point.create(current_point.x() + 1, current_point.y()), screen,
                                         original_color, new_color)
            self.paint_in_all_directions(Point.create(current_point.x() - 1, current_point.y()), screen,
                                         original_color, new_color)
            self.paint_in_all_directions(Point.create(current_point.x(), current_point.y() + 1), screen,
                                         original_color, new_color)
            self.paint_in_all_directions(Point.create(current_point.x(), current_point.y() - 1), screen,
                                         original_color, new_color)
