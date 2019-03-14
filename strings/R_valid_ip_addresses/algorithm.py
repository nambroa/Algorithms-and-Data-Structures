# coding=utf-8
"""

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where  A,B,C and D are numbers from 0-255.
The numbers cannot be 0 prefixed unless they are 0. That means '0' is the only valid "ip part" that can be zero.
'00', '000' are not valid.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)

QUESTIONS:

+ Can the digits be floats or imaginary numbers? No
+ Can the input be invalid? No
+ Can the input be empty? Yes
+ Will the input always be large enough to form an IP? No, you should check if it is smaller than 8 digits in length.
The input shouldn't be bigger than 12 digits in length.

"""

"""

The idea is to iterate over all the digits, trying all the combinations out as soon as you see them.
We know that the IP has 4 parts.
The A part always starts from the beginning, and part B always follows part A. Part C follows B, and so on.
Since parts are dependant from each other, we need to form each part in unison. We can't just get all the parts A
, then all the parts B, etc.
We will use a counter for each part (i,j,k). We will have as a restriction that each counter needs to be smaller
than the length of the digits (in order to stop). Also, each counter needs to be smaller than the one that follows it.
For example the counter for part B must always be smaller than the counter for part C.

For part A, we know we have to possibilities. digits[0..1] and digits[0..2], so the counter for part A should never
be higher than 3.
You can apply the same logic to all the counters to get their boundaries.

"""


def restore_ip_addresses_from(digits):
    digits = digits.strip()
    n = len(digits)
    if 12 < n < 4:
        # Invalid length for ip address.
        return []
    ip_addresses = []
    i = 1
    while i <= 3 and i < n:
        j = i + 1
        while j <= i + 3 and j < n:
            k = j + 1
            while k <= j + 3 and k < n:
                # First part of the ip
                a = int(digits[:i])
                # Second part of the ip
                b = int(digits[i:j])
                # Third part of the ip
                c = int(digits[j:k])
                # Fourth part of the ip
                d = int(digits[k:])
                # If digits[0] == '0' and i > 1 --> That part of the ip is longer than 1, so the zero is invalid.
                if (digits[0] == '0' and (i > 1 or a != 0)) or (digits[i] == '0' and (j > i + 1 or b != 0)) or (
                        digits[j] == '0' and (k > j + 1 or c != 0)) or (digits[k] == '0' and (n > k + 1 or d != 0)):
                    # Do Nothing
                    k += 1
                    continue
                # Check if it's a valid ip.
                elif 255 >= a >= 0 and 255 >= b >= 0 and 255 >= c >= 0 and 255 >= d >= 0:
                    ip_addresses.append(digits[:i] + "." + digits[i:j] + "." + digits[j:k] + "." + digits[k:])
                k += 1
            j += 1
        i += 1
    return ip_addresses
