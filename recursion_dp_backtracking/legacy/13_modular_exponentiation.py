"""

Implement pow(A, B) % C.

In other words, given A, B and C,
find (AB)%C.

Input : A = 2, B = 3, C = 3
Return : 2
2^3 % 3 = 8 % 3 = 2

"""

"""

x^n can be so big that is doesn't fit in a normal integer (yes I know python extends them to fit memory but usually
integers are 4 bytes long). Normal integers go from -2^31 to 2^31 only. Long can be short for big numbers as well.

Modular operations are conmutative. This means (a * b) % M = ((a % M) * (b % M)) % M

We can use this to do the following:

+ In the case that n is EVEN:
(x^n) % M = (x^(n/2) * x^(n/2)) % M = ((x^(n/2) % M) * (x^(n/2) % M)) % M

+ In the case that n is ODD:
(x^n) % M = (x * x^(n-1)) % M = ((x % M) * (x^(n-1) % M)) % M

+ In the case that n is 0:
(x^n) % M = 1

"""


# Time complexity of this function is O(log n).
def modular_exponentiation(base, exponent, mod):
    """
    :param base: positive number
    :param exponent: positive number
    :param mod: positive number
    :return: (base^exponent) % mod
    """
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:  # Case exponent even
        recursive_modular = modular_exponentiation(base=base, exponent=exponent / 2, mod=mod)
        return (recursive_modular * recursive_modular) % mod
    else:  # Case exponent odd
        recursive_modular = modular_exponentiation(base=base, exponent=exponent-1, mod=mod)
        return ((base % mod) * recursive_modular) % mod

