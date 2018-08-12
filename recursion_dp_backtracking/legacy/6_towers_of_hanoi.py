"""

You have 3 towers and N disks of different sizes which can slide onto any tower.
The puzzle starts with the disks sorted in ascending order of size from top to bottom (top contains the smallest one).
You have the following constraints:
    + Only one disk can be moved at a time.
    + A disk is slid off the top of one tower onto another tower.
    + A disk cannot be placed on top of a smaller disk.

Write a program to move the disks from the first tower to the last using Stacks.

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes?
+ Will the input always valid?

"""
from django.core.exceptions import ValidationError

from stacks.stack import Stack

"""

The idea is that you have 3 towers: Origin, Destination and Buffer.

You first move the top (n-1) disks from Origin to Buffer, using Destination as a buffer.
Then you move the last disk (the biggest one) from Origin to Destination.
After that, you move the top (n-1) disks from Buffer to Destination, using Origin as a buffer.

"""


class Tower(object):
    def __init__(self, index):
        self._disks = Stack.new()
        self._index = index

    def index(self):
        return self._index

    def add(self, disk):
        if not self._disks.is_empty() and self._disks.peek() <= disk:
            # You can't add a disk that is bigger than the current top.
            raise ValidationError
        self._disks.push(disk)

    def move_top_to(self, tower):
        top = self._disks.pop()
        tower.add(top)

    def move_disks(self, number_of_disks, destination, buffer):
        if number_of_disks > 0:
            self.move_disks(number_of_disks-1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(number_of_disks-1, destination, self)

    def show(self):
        self._disks.show()


tower_zero = Tower(0)
tower_one = Tower(1)
tower_two = Tower(2)
tower_zero.add(4)
tower_zero.add(3)
tower_zero.add(2)
tower_zero.add(1)
tower_zero.move_disks(number_of_disks=4, destination=tower_two, buffer=tower_one)
tower_two.show()

