"""

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

QUESTIONS YOU SHOULD ASK:
+ Is the input always going to be valid? Yes.
+ Can I get zeroes in the list? Yes.
+ Should I form the largest number with them or try to ignore them from the function? Use them to form it.

"""
from fractions import Fraction

"""

Since sorting in descending order doesn't work (because 34 > 9 but 9 appears first in the finished number), we need to
sort on a custom comparison A or B.

A) Given numbers X and Y, we append to form XY and YX, and then we compare. If XY > YX, then X should come first,
   otherwise Y should come first.

B) Given a number X, we calculate it's fraction in relation to the number of digits it has. For example, if X=3, then
   the fraction is 3/10^1 = 3/10. If X=30, the fraction is 30/10^2 = 30/100. In order to make 3 come before 30 as we
   need, we subtract 1 from the denominator. That makes X=3 --> 3/9 and X=30 --> 30/99, such as 3/9 > 30/99. This
   subtraction of 1 makes sure that all the cases of 3 vs 30 or 30 vs 300 always prioritize the number with the least
   digit count.
    It also makes the cases of 3 vs 31 or 3 vs 3i, with i > 3 favor the case of 3i as it should be. For example,
    X=3 --> 3/9 and X=34 --> 34/99 such that 3/9 < 34/99. Of course this also means that 3 vs 3i will favor 3 with
    i < 3. With i == 3 it doesn't matter, since they are "the same".

"""


def largest_number(numbers):
    # Sort by the fraction method B)
    numbers = sorted(numbers, key=lambda n: Fraction(n, (10 ** len(str(n)))-1), reverse=True)
    i = 0
    # This while is in place in case the array is full of zeroes. It will make answer just a '0' which is the
    # largest number.
    while i < len(numbers) - 1:
        if numbers[i] != 0:
            break
        else:
            i += 1
    answer = ''.join(str(digit) for digit in numbers[i:])
    return answer