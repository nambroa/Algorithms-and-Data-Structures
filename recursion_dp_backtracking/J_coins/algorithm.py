"""

Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.

Hints: #300, #324, #343, #380, #394

QUESTIONS TO ASK:
+ Can the n be None or negative or floating point? (For this question, let's assume it can.)
+ Can the n be zero? (For this question, let's assume it can't.)
+ Can the n be string/invalid struct? (For this question, let's assume it can't.)

"""

# Since this questions says: given an infinite number.. write all the ways to represent... we can understand
# it's probably a recursive question. So we need our base case and our recursive case.

# The main idea is to first decide how many quarters you will use. Then, for that amount, calculate all the ways to
# fill the extra cents with nickels, dimes and pennies. Do this for every combination of quarters you can use.
# So, something like this:
# 1) I decide how many quarters to use. I can have something extra, like 10 cents.
# 2) I decide how many dimes to use with the rest. I can have something extra, like 6 cents.
# 3) I decide how many nickels to use with the rest. I can have something extra, like 2 cents.
# 4) I decide how many pennies to use with the rest. Always 1 way (BASE CASE)
