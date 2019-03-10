"""

Implement an algorithm to print all valid (i.e properly opened and closed) combinations of n pairs of parentheses.

EXAMPLE:
    + Input: 3
    + Output: ((())), (()()), (())(), ()(()), ()()()

"""


def generate_parenthesis(n):
    if n is None: raise ValueError("Amount of pairs of parenthesis is None.")
    if n == 0: return []
    if n < 0: raise ValueError("Amount of pairs of parenthesis is negative.")
    result = []
    _generate_parenthesis_recursive(result, "(", n - 1, n)
    return result


def _generate_parenthesis_recursive(result, current, left, right):
    if left == 0 and right == 0:
        result.append(current)
    if left > 0:
        # First add the left parenteses.
        _generate_parenthesis_recursive(result, current + "(", left - 1, right)
    if left < right:
        # Then add the right ones.
        # We need left < right in order to create a valid parentheses, otherwise we risk something like "((()".
        _generate_parenthesis_recursive(result, current + ")", left, right - 1)
