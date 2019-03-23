"""

Given a collection of intervals, return the merge of all overlapping intervals.

For example:

Given [[1,3],[2,6],[8,10],[15,18]],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.

EXAMPLE CLARIFYING QUESTIONS:

+ Can the array of intervals be empty? Yes.
+ Can the array of intervals be None? Yes
+ Can the array of intervals have only one interval? Yes
+ Will all the numbers in the interval be positive integers? Yes
+ Will the intervals be sorted? No.

"""


# Seems like an iterative solution. The idea is to iterate over the intervals and merge them on the spot.
# First, we will sort the intervals by their starting hour. This will cost O(N * LOG N) complexity. Then we iterate.

# We Start with [1,3], then move to [2,6]. Since 2 is higher than 1, I dont replace the starting hour.
# 6 is higher than 3 and its the end member of the tuple, so I have a new merged interval --> [1,6].

# Then I see [8,10]. Since 8 is higher than the end, I can't really merge it with [1,6]. I add [1,6] to the merged
# intervals list and set [8,10] as the new current interval.

# Moving on to [15,18], same situation as [1,6] with [8,10]. I return [1,6], [8,10], [15,18]


class Merger(object):
    def merge_intervals(self, intervals):
        self._validate_intervals(intervals)
        if len(intervals) == 1:
            return intervals
        return self._merge_intervals(intervals)

    def _validate_intervals(self, intervals):
        if intervals is None or len(intervals) == 0:
            raise ValueError("Intervals are None or empty.")

    def _sort_intervals_by_starting_hour(self, intervals):
        return sorted(intervals, key=lambda interval: interval[0])

    def _merge_intervals(self, intervals):
        intervals = self._sort_intervals_by_starting_hour(intervals)
        merged_intervals = []
        current_merged_interval = intervals[0]
        for interval in intervals[1:]:
            if self._can_merge_with_current_merged_interval(interval, current_merged_interval):
                current_merged_interval = self._merge(current_merged_interval, interval)
            else:
                merged_intervals.append(current_merged_interval)
                current_merged_interval = interval
        # Check last iteration, in case the for ended but it wasn't merged.
        if merged_intervals[-1] != current_merged_interval:
            merged_intervals.append(current_merged_interval)
        return merged_intervals

    def _can_merge_with_current_merged_interval(self, interval, current_merged_interval):
        # Example: [1,6] can't be merged with [8,10] since [8,10] starts later than the ending of [1,6].
        # If the current_merged_interval is empty, that means that I can always merge it.
        return current_merged_interval[1] >= interval[0]

    def _merge(self, current_merged_interval, interval):
        # If the current_merged_interval is empty, that means a new merging iteration is in place.
        return [min(current_merged_interval[0], interval[0]), max(current_merged_interval[1], interval[1])]
