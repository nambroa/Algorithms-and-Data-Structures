"""
MERGE SORT
"""


def merge_sort(data):
    data_length = len(data)
    # Sorted data is initialized with allocated space beforehand to stop worst cases of memory reallocation.
    sorted_data = [None] * data_length
    if data_length < 2:
        # It's already sorted.
        return data
    mid = int(data_length / 2)
    sorted_first_half_of_data = merge_sort(data[mid:])
    sorted_second_half_of_data = merge_sort(data[:mid])
    i = 0
    j = 0
    q = 0
    # After recursion, time to merge.
    while i < len(sorted_first_half_of_data) and j < len(sorted_second_half_of_data):
        if sorted_first_half_of_data[i] < sorted_second_half_of_data[j]:
            sorted_data[q] = sorted_first_half_of_data[i]
            i += 1
            q += 1
        else:
            sorted_data[q] = sorted_second_half_of_data[j]
            j += 1
            q += 1
    if j > i:
        sorted_data[q:] = sorted_first_half_of_data[i:]
    else:
        sorted_data[q:] = sorted_second_half_of_data[j:]
    return sorted_data

assert merge_sort([]) == []
assert merge_sort([1]) == [1]
assert merge_sort([1, 2]) == [1, 2]
assert merge_sort([2, 1]) == [1, 2]
assert merge_sort([6, 5, 1, 4]) == [1, 4, 5, 6]
assert merge_sort([1, 6, 9, 5, 2, 8, 6, 19]) == [1, 2, 5, 6, 6, 8, 9, 19]