"""

Write a function to find the nth "count and say sequence" given an integer n.

The "count and say sequence" is a special recursive sequence. Here are some base cases:
N   String to Print
1   1
2   1 1
3   2 1
4   1 2 1 1

Base case: n = 1 ---> print "1"
For n = 2 ---> Look at the previous string and write the number of times a digit is seen and the digit itself.
               In this case, digit 1 is seen 1 time in a row, so print "1 1"
For n = 3 ---> Digit 1 is seen two times in a row, so print "2 1"
For n = 4 ---> Digit 2 is seen 1 time, then digit one is seen one time, print "1 2 1 1"
For n = 5 ---> Digit 1 is seen one time, then digit 2 is seen two times, then digit one is seen two times.
               Print "1 1 1 2 2 1"

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes.
+ Will the input always be valid? No, it can be None
+ Can n be negative? No. Can it be zero? Yes, return 1.


"""

"""

Count and say is a recursive function, and you have to do all the steps (so no memoization for optimizing)

"""


def count_and_say(n):
    if n is None or n <= 0:
        raise ValueError('N is None or is lower than 1.')
    # Base cases.
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    # Other cases: I can assume n is higher than 2. So it will always have 2 or more chars.
    else:
        previous_iteration = '11'
        for i in range(2, n):
            new_iteration = ''
            current_char = previous_iteration[0]
            amount_of_times = 1
            for char in previous_iteration[1:]:
                # Count the amount of times chars are seen. Print amount_of_times+char for each char.
                # Then replace previous iteration with the result.
                if char == current_char:
                    amount_of_times += 1
                else:
                    new_iteration = new_iteration + str(amount_of_times) + current_char
                    current_char = char
                    amount_of_times = 1
            new_iteration = new_iteration + str(amount_of_times) + current_char
            previous_iteration = new_iteration
        return previous_iteration
