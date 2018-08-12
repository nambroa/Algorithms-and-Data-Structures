"""

Functions that help in basic exercise tasks. Get a bit, set a bit, clear a bit and update a bit.

It's important to note that the position of the bits is notated differently than most other data structures.
Example:
        1      0       1       0       1      = BINARY NUMBER
        4th    3th     2th     1st     0th    = POSITIONS

+ Get_bit will get the ith bit of the number number.
+ Set_bit will set the ith bit of the number number to 1.
+ Clear_bit will set the ith bit of the number number to 0.
+ Clear_bits_from_0th_to_ith_position will clear all bits from the 0th to the ith (INCLUSIVE)
+ Clear_bits_from_most_significant_bit_to_ith will clear all bits from the most signifcant to the ith (INCLUSIVE)
+ Update_bit sets the ith bit to a value v, determinated by the flag bit_is_1.
"""


def get_bit(number, index):
    return (number & (1 << index)) != 0


def set_bit(number, index):
    return number | (1 << index)


def clear_bit(number, index):
    mask = ~(1 << index)  # All 1's except on the ith position, thanks to the negation. This will clear the ith bit.
    return number & mask  # Mask has a 0 at the ith position, so the and will always return 0 at the ith position.


def clear_bits_from_0th_to_ith_position(number, index):
    # -1 represents a sequence of 1's in complement two notation. We shift it left by i+1 bits.
    # This gives us a sequence of 1s in the most significant bits, followed by i bits that are 0.
    mask = (-1 << (index+1))
    return number & mask


def clear_bits_from_most_significant_bit_to_ith(number, index):
    # (1 << index) gives us a mask with a 1 at the ith bit, like 000100 for 1 << 2.
    # We then substract 1, having 000011. We have then 0's from the most significant bit to the ith (inclusive)
    mask = (1 << index) - 1
    return number & mask


def update_bit(number, index, bit_is_1):
    if bit_is_1:
        value = 1
    else:
        value = 0
    mask = ~(1 << index)  # The mask will have all 1's except at the 1th position.
    return (number & mask) | (value << index)
