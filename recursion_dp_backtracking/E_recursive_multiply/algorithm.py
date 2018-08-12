"""

Write a recursive function to multiply two positive integers without using the * operator or the / operator.
You can use addition, subtraction, and bit shifting. You should minimize the number of those operations used.


QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes?
+ Will the input always valid? (aka positive integers)

"""

"""

Complexity: O(log(int_2))

One of the famous "gotcha" questions. Bit manipulation in 2018: instant vomit.
This method is the Russian peasant algorithm. The idea is to double the first number and halve the second number
repeatedly till the second number doesn’t become 1. In the process, whenever the second number becomes odd, we add the
first number to result (result is initialized as 0)

"""


# This function returns int_1 * int_2
def iterative_multiply(int_1, int_2):
    # Check for base cases, if any of the ints is 0 or 1, the multiplying gets really ease.
    if int_2 == 0 or int_1 == 0:
        return 0
    elif int_2 == 1:
        return int_1
    elif int_1 == 1:
        return int_2

    # Main function
    # If int_2 is negative, the while loop will never stop because of complement two's notation.
    # I need to make it positive, and then make the final result negative.
    total_sum = 0
    original_int_2 = int_2
    if original_int_2 < 0:
        int_2 = -int_2
    # Main loop (russian peasant)
    while int_2 != 0:
        if int_2 & 1 == 1:
            total_sum += int_1
        int_1 <<= 1
        int_2 >>= 1

    if original_int_2 < 0:
        total_sum = -total_sum

    return total_sum


"""

Complexity: O(int_2)
The normal answer..

"""


def recursive_multiply(int_1, int_2):
    return _recursive_multiply_sum(int_1, int_2, 0)


def _recursive_multiply_sum(int_1, int_2, sum):
    if int_2 == 0:
        return 0
    if int_2 > 0:
        sum = int_1 + _recursive_multiply_sum(int_1, int_2 - 1, sum)
    if int_2 < 0:
        sum = -int_1 + _recursive_multiply_sum(int_1, int_2 + 1, sum)
    return sum


