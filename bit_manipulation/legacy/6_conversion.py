"""

Write a function to determine the number of bits you would need to flip to convert integer A to integer B.

EXAMPLE INPUT: A = 29 (11101) B=15 (01111)
EXAMPLE OUTPUT: 2

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes
+ Can I assume A and B of equal bit length? No
+ Will A and B be positive? Yes

"""


def conversion(a, b):
    different_bits_between_a_b = a ^ b
    number_of_bits_to_flip = 0
    while different_bits_between_a_b != 0:
        number_of_bits_to_flip += 1
        different_bits_between_a_b &= different_bits_between_a_b - 1
    return number_of_bits_to_flip


print(conversion(a=29, b=15))


