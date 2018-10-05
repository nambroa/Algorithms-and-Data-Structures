# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


class Solution:
    def fizzbuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzbuzz_values = []
        for i in range(1, n + 1):
            fizzbuzz_values.append(self.get_fizzbuzz_value_of(i))
        return fizzbuzz_values

    def get_fizzbuzz_value_of(self, n):
        fizzbuzz_value = ''
        if n % 3 == 0:
            fizzbuzz_value += 'Fizz'
        if n % 5 == 0:
            fizzbuzz_value += 'Buzz'
        if not fizzbuzz_value:
            return str(n)
        return fizzbuzz_value

