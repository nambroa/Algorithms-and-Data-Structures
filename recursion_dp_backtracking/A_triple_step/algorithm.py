"""

A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes?
+ Will the input always be a number (aka valid)?
+ Will the input always be positive? (Yes)

"""


# Length of stairs = n
# I assume stairs start at 0, so I want the amount of ways a child can run up to the (n+1)th stair.
# Fibonacci called, and he demands royalties.

def amount_of_ways_to_run_up_the_stairs(length_of_stairs):
    memo = [0 for i in range(length_of_stairs+1)]
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    for i in range(3, length_of_stairs+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[length_of_stairs]