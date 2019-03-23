# input = [(1,4), (2,3)] return 3
# input = [(4,6), (1,2)] return 3
# input = {{1,4}, {6,8}, {2,4}, {7,9}, {10, 15}} return 11
from unittest import TestCase

from arrays.M_total_time_covered_by_intervals.algorithm import get_the_total_time_covered_by_the_intervals


class OverlappingIntervalsTest(TestCase):
    def test_overlapping_intervals_returns_3(self):
        self.assertEqual(get_the_total_time_covered_by_the_intervals([(1, 4), (2, 3)]), 3)

    def test_overlapping_intervals_returns_4(self):
        self.assertEqual(get_the_total_time_covered_by_the_intervals([(4, 7), (1, 2)]), 4)

    def test_overlapping_intervals_returns_11(self):
        self.assertEqual(get_the_total_time_covered_by_the_intervals([(1, 4), (6, 8), (2, 4), (7, 9), (10, 15)]), 11)

