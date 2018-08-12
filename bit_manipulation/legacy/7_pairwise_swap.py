"""

Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g bit 0 and bit 1
are swapped, bit 2 and bit 3 are swapped, and so on).

"""

"""

The solution operates on shifting the odd bits first, and then the even bits.

First, we mask to obtain only the odd bits by masking with 10101010.. (0xAA..). Then, we shift them to the right.
(with logical right shift, since we want a 0 in the sign bit so that the even bit can replace it).

Then, we mask to obtain only the even bits by masking with a 010101.. (0x55..). Then, we shift them to the left.

"""


def swap(integer):
    # First, we create a mask to obtain only the odd bits
    odd_bits_mask = 0xAAAAAAAA  # Equivalent to 1010101010..
    # Then, we create a mask to obtain only the even bits
    even_bits_mask = 0x55555555
    odd_bits_of_integer = integer & odd_bits_mask
    even_bits_of_integer = integer & even_bits_mask
    # Shift the odd bits to the right, and the even to the left.
    odd_bits_of_integer_shifted = odd_bits_of_integer >> 1
    even_bits_of_integer_shifted = even_bits_of_integer << 1
    return odd_bits_of_integer_shifted | even_bits_of_integer_shifted
