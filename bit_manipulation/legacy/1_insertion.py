"""

You are given two 32 bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at bit i.
You can assume that the bits j through i have enough space to fit all of M.
That is, if M=10011, you can assume that there are at least 5 bits between j and i.

EXAMPLE INPUT: N= 10000000000, M=10011, i=2, j=6
EXAMPLE OUTPUT: N = 10001001100

"""


def insert_M_into_N(N, M, i, j):

    # First, create mask with all 1's except between j and i.
    all_ones = ~0  # Sequence of all 1's.
    left = all_ones << (j+1)  # 1's before position j, then all 0's.
    right = ((1 << i) -1)  # 1's after position i.
    mask = left | right  # All 1's, except the 0's between i and j. Ex: 1100011

    # Clear bits j through i from N, then put M in there.
    N_cleared = N & mask
    M_shifted = M << i

    return bin(N_cleared | M_shifted)

insert_M_into_N(N=0b10000000000, M=0b10011, i=2, j=6)