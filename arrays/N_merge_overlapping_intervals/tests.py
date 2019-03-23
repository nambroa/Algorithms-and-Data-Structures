from unittest import TestCase

from arrays.N_merge_overlapping_intervals.algorithm import Merger


class MergeOverlappingTest(TestCase):
    def test_merge_example_case_one(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        merged_intervals = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(merged_intervals, Merger().merge_intervals(intervals))

    def test_merge_example_case_two(self):
        intervals = [[1, 6], [8, 10], [15, 18]]
        merged_intervals = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(merged_intervals, Merger().merge_intervals(intervals))

    def test_merge_example_case_three(self):
        intervals = [[1, 6]]
        merged_intervals = [[1, 6]]
        self.assertEqual(merged_intervals, Merger().merge_intervals(intervals))

    def test_merge_example_case_four(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [17, 22], [22, 24]]
        merged_intervals = [[1, 6], [8, 10], [15, 24]]
        self.assertEqual(merged_intervals, Merger().merge_intervals(intervals))
