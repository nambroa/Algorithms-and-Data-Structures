"""

Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in
two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them.
Design an algorithm to find a path for the robot from the top left to the bottom right

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes?
+ How does the grid come? Array of arrays, starting at [0,0] and ending at [n,n]
+ Is the input always valid? Yes
+ How do I know if a cell is off limit? Instead of the cell, you will recieve None.
+ Do I need to find the shortest way? No, just any one of them (if there is more than 1).'
+ Will there always be a way? Yes

"""


# Example Grid: [[0,0], [0,1], [0,2], [1,0], [1,1], None, [2,0], None, [2,2]]


class Point(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column

    @classmethod
    def new(cls, row, column):
        point = cls(row, column)
        return point


# This algorithm will take O(rows*columns) since we only hit each cell once (thanks to the memoized failed_points)
def get_path(maze, row, column, path, failed_points):
    # We check for off limits
    if row < 0 or column < 0 or not maze[row][column]:
        return False

    point = Point(row, column)
    at_origin = row == 0 and column == 0
    if point not in failed_points and (
                    at_origin or get_path(maze, row - 1, column, path, failed_points) or get_path(maze, row, column - 1,
                                                                                                  path,
                                                                                                  failed_points)):
        path.append(point)
        return True

    failed_points.add(point)
    return False


def find_path_to_exit_in(maze):
    if not maze:
        return None
    path = []
    failed_points = set()
    # We try and find the path to row n, col n in the maze, using failed_points to remember where not to go through.
    if get_path(maze=maze, row=len(maze) - 1, column=len(maze[0]) - 1, path=path, failed_points=failed_points):
        return path
    return None
