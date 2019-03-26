"""

STACKS AND QUEUES - QUESTION 1

Describe how you could use a single array to implement three stacks.

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes
+ Do you want a dynamic approach to stack length? No
+ Do you want to be able to access, append, and pop from each individual stack easily? Yes
+ Will the sizes always be positive? They are integers, positive or negative. They can't be 0 though.
+ What can the stacks contain? Numbers
+ Will the input always be valid? Yes
+ Will I always recieve the 3 lengths? Yes

"""


class ThreeStackArray(object):
    # We are on Python, the array will always -within reason- be able to hold the three stacks, since lists are dynamic.
    @classmethod
    def create(cls, first_stack_length, second_stack_length, third_stack_length):
        if first_stack_length < 0 or second_stack_length < 0 or third_stack_length < 0:
            raise ValueError("One of the stack lengths is negative.")
        three_stack_array = cls(first_stack_length, second_stack_length, third_stack_length)
        return three_stack_array

    def __init__(self, first_stack_length, second_stack_length, third_stack_length):
        self._first_stack_length = first_stack_length
        self._first_stack_current_length = 0
        self._second_stack_length = second_stack_length
        self._second_stack_current_length = 0
        self._third_stack_length = third_stack_length
        self._third_stack_current_length = 0
        self._array = [None * first_stack_length+second_stack_length+third_stack_length]

    def _current_second_stack_new_element_position(self):
        second_stack_beggining_index = self._first_stack_length  # Since indexes start at 0.
        return second_stack_beggining_index + self._second_stack_current_length

    def _current_first_stack_new_element_position(self):
        first_stack_beggining_index = 0
        return first_stack_beggining_index + self._first_stack_current_length

    def _current_third_stack_new_element_position(self):
        third_stack_beggining_index = self._first_stack_length + self._second_stack_length  # Since indexes start at 0.
        return third_stack_beggining_index + self._third_stack_current_length

    def _check_maximum_length_limit(self, current_length, total_length):
        if current_length >= total_length:
            raise ValueError("Stack maximum limit reached, please remove one of the elements first.")

    def _check_minimum_length_limit(self, current_length):
        if current_length <= 0:
            raise ValueError("Stack minimum limit reached, please add at least one elements before removing.")

    def push_to_first_stack(self, elem):
        self._check_maximum_length_limit(current_length=self._first_stack_current_length,
                                         total_length=self._first_stack_length)
        self._array[self._current_first_stack_new_element_position()] = elem
        self._first_stack_current_length += 1

    def push_to_second_stack(self, elem):
        self._check_maximum_length_limit(current_length=self._second_stack_current_length,
                                         total_length=self._second_stack_length)
        self._array[self._current_second_stack_new_element_position()] = elem
        self._second_stack_current_length += 1

    def push_to_third_stack(self, elem):
        self._check_maximum_length_limit(current_length=self._third_stack_current_length,
                                         total_length=self._third_stack_length)
        self._array[self._current_third_stack_new_element_position()] = elem
        self._third_stack_current_length += 1

    def peek_from_first_stack(self):
        return self._array[self._current_first_stack_new_element_position()-1]

    def peek_from_second_stack(self):
        return self._array[self._current_second_stack_new_element_position() - 1]

    def peek_from_third_stack(self):
        return self._array[self._current_third_stack_new_element_position() - 1]

    def pop_from_first_stack(self):
        self._check_minimum_length_limit(current_length=self._first_stack_current_length)
        # We can't remove since we would be dealing we O(|array|). We will put None on the field instead.
        elem = self._array[self._current_first_stack_new_element_position()-1]
        self._array[self._current_first_stack_new_element_position()-1] = None
        self._first_stack_current_length -= 1
        return elem

    def pop_from_second_stack(self):
        self._check_minimum_length_limit(current_length=self._second_stack_current_length)
        # We can't remove since we would be dealing we O(|array|). We will put None on the field instead.
        elem = self._array[self._current_second_stack_new_element_position()-1]
        self._array[self._current_second_stack_new_element_position()-1] = None
        self._second_stack_current_length -= 1
        return elem

    def pop_from_third_stack(self):
        self._check_minimum_length_limit(current_length=self._third_stack_current_length)
        # We can't remove since we would be dealing we O(|array|). We will put None on the field instead.
        elem = self._array[self._current_third_stack_new_element_position()-1]
        self._array[self._current_third_stack_new_element_position()-1] = None
        self._third_stack_current_length -= 1
        return elem

