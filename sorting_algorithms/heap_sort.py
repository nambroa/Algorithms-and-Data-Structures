"""

    HOW TO HEAP SORT

1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. We then swap the root node with the last node and
   delete the last node from the heap.
3. Repeat 1 and 2 steps while size of heap is greater than 1.

"""

# To heapify subtree rooted at index i.
# n is size of heap. FOR MAXHEAPS
def heapify(arr, arr_length, root_index):
    largest = root_index  # Initialize largest as root
    left_child = 2 * root_index + 1  # left = 2*i + 1
    right_child = 2 * root_index + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if left_child < arr_length and arr[root_index] < arr[left_child]:
        largest = left_child

    # See if right child of root exists and is
    # greater than root
    if right_child < arr_length and arr[largest] < arr[right_child]:
        largest = right_child

    # Change root with one of its childs, if they were bigger.
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]  # swap
        # Heapify the root again.
        heapify(arr, arr_length, largest)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" % arr[i]),
