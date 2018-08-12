"""

Given a collection of intervals, return the merge of all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.

"""


def merge_overlapping_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda interv: interv[0])
    start_of_overlapping_interval = sorted_intervals[0]
    end_of_overlapping_interval = sorted_intervals[0]
    intervals = []
    for i in xrange(1, len(sorted_intervals)):
        interval = sorted_intervals[i]
        if interval[0] <= end_of_overlapping_interval[1]:
            end_of_overlapping_interval = interval
        else:
            merged_interval = [start_of_overlapping_interval[0], end_of_overlapping_interval[1]]
            intervals.append(merged_interval)
            start_of_overlapping_interval = interval
            end_of_overlapping_interval = interval
    # Append the last interval that isn't counted in the for loop
    intervals.append([start_of_overlapping_interval[0], end_of_overlapping_interval[1]])
    return intervals

merge_overlapping_intervals([[1,3],[2,6],[8,10],[15,18]])