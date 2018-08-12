"""

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.

QUESTIONS YOU SHOULD ASK:
+ Will the input always be valid? Yes
+ Will the intervals always contain positive integers? Yes
+ Does the new interval come in a valid form? (aka (8,10) instead of (10, 8)) Yes


"""

# Definition for an interval.
from unittest import TestCase


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def is_inside(self, interval):
        return self.start >= interval.start and self.end <= interval.end

    def in_between_left(self, interval):
        return self.end >= interval.start and self.start <= interval.end

    def in_between_right(self, interval):
        return self.start <= interval.end <= self.end

    def can_merge_with(self, interval):
        return self.is_inside(interval) or self.in_between_left(interval) or self.in_between_right(interval)

    def is_not_zero(self):
        return self.start != 0 or self.end != 0

    def __str__(self):
        return "(%s, %s)" % (self.start, self.end)


class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if not intervals:
            return [new_interval]
        merged_interval = new_interval
        new_intervals = []
        current_index = -1
        for (index, interval) in enumerate(intervals):
            if interval.can_merge_with(merged_interval):
                min_start = min(interval.start, merged_interval.start)
                max_end = max(interval.end, merged_interval.end)
                merged_interval = Interval(min_start, max_end)
            elif interval.start > merged_interval.end:
                new_intervals.append(merged_interval)
                new_intervals.append(interval)
                current_index = index
                break
            else:
                new_intervals.append(interval)
        if current_index == -1:
            new_intervals.append(merged_interval)
            return new_intervals
        else:
            for interval in intervals[current_index+1:]:
                new_intervals.append(interval)
            return new_intervals


class MergeIntervalsTest(TestCase):
    def test_merge_intervals_interviewbit_1(self):
        interval_1 = Interval(s=1, e=2)
        interval_2 = Interval(s=3, e=6)
        intervals = [interval_1, interval_2]
        new_interval = Interval(s=8, e=10)
        sol = Solution()
        merged_intervals = sol.insert(intervals, new_interval)
        self.assertEqual(merged_intervals, [interval_1, interval_2, new_interval])

    def test_merge_intervals_interviewbit_2(self):
        i1 = Interval(s=1, e=2)
        i2 = Interval(s=3, e=5)
        i3 = Interval(s=6, e=7)
        i4 = Interval(s=8, e=10)
        i5 = Interval(s=12, e=16)
        new_interval = Interval(s=4, e=9)
        intervals = [i1, i2, i3, i4, i5]
        sol = Solution()
        merged_intervals = sol.insert(intervals, new_interval)
        self.assertEqual(len(merged_intervals), 3)
        self.assert_interval_values(interval=merged_intervals[0], start=1, end=2)
        self.assert_interval_values(interval=merged_intervals[1], start=3, end=10)
        self.assert_interval_values(interval=merged_intervals[2], start=12, end=16)

    def assert_interval_values(self, interval, start, end):
        self.assertEqual(interval.start, start)
        self.assertEqual(interval.end, end)
