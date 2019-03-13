"""

Given a list of arrays of time intervals, write a function that calculates the total amount of time
covered by the intervals.
For example:
input = [(1,4), (2,3)] return 3
input = [(4,6), (1,2)] return 3
input = {{1,4}, {6,8}, {2,4}, {7,9}, {10, 15}} return 11

QUESTIONS TO ASK (with example answers to guide the solution):

+ Can the list of arrays be None or empty? Yes, both.
+ Is the list of arrays sorted? No, it can come in any order.
+ Can I use additional memory? Yes.
+ Can I modify the list of arrays? No, you can't.

"""


# We start by getting the starting times and the ending times of the intervals separately. Then, we sort those.
# The main point here is to iterate them at the same time with indexes i and j.

# If the current starting times is smaller than the current ending times, it means that you could potentially start
# there. So we remember this decision and advance the i. If, in the next iteration, the current starting times is
# still smaller, we WONT take that as a potential starting time. This is because the array is sorted, so the
# starting_times[i+1] will always be higher than starting_times[i]. And, as such, it's total time would be lower.
# In order to achieve this, we have a "current_count" that increases each time we find a starting time and
# decreases each time we find an ending time. Only when "current_count" is zero, we will take a new starting_time.

# If the current ending times is smaller, we have to check "current_count".
# If it isnt zero, it means that you can search further.
# If it is zero, this is the best ending time to form the interval

def get_the_total_time_covered_by_the_intervals(intervals):
    _validate_empty_or_none_intervals(intervals)
    starting_times = [interval[0] for interval in intervals]
    ending_times = [interval[1] for interval in intervals]
    starting_times.sort()
    ending_times.sort()
    total_time = current_starting_time = current_count = i = j = 0
    while i < len(starting_times) and j < len(ending_times):
        if starting_times[i] <= ending_times[j]:
            if current_count == 0:
                current_starting_time = starting_times[i]
            current_count += 1
            i += 1
        else:
            current_count -= 1
            if current_count == 0:
                total_time += ending_times[j] - current_starting_time
            j += 1
    total_time += (ending_times[len(ending_times) - 1] - current_starting_time)  # Last iteration.
    return total_time


def _validate_empty_or_none_intervals(intervals):
    if intervals is None or len(intervals) == 0:
        raise ValueError("Intervals is None or empty.")
