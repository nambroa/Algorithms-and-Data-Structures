"""

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Example :

Input : "XIV"
Return : 14
Input : "XX"
Output : 20

QUESTIONS:

+ Can the input be None? Yes
+ Can the input be empty? Yes
+ Can the input be invalid? No
+ Can the input be negative or with coma or 0? No

"""


"""

The roman numerals to use are listed below:

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

The idea is to iterate over the string and check by pairs. That is because a roman numeral changes depending on its
adjacent numeral. So for example I = 1 and V = 5, but IV = 4.

Also note that IV = 4 and IX = 9, but when going to 100 we get XL = 40 and XC = 90. The pattern repeats.
It's important to know that 49 != IL. You need the correct letters for the magnitude, so XLIX = 49
The number that can "subtract" are 1, 10, and so on..

So, when checking by pairs, we need to see if roman[i] is smaller than roman[i+1] and their scale.
    If roman[i] is I, I need to know if roman[i+1] is X or V.
    If roman[i] is X, I need to know if roman[i+1] is L or C.
    If roman[i] is C, I need to know if roman[i+1] is D or M.

If there is match, for example roman[i] = I and roman[i+1] = X, I calculate it's value and then move by 2.
If there is no match, I calculate the value of roman[i] and move by 1.

"""


conversion_table = {'I': 1, 'V': 5, 'IV': 4, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
                    'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}


def convert_roman_to_integer(roman):
    if roman is None:
        raise ValueError('Roman number is None.')
    if len(roman) == 0:
        return 0
    if len(roman) == 1:
        return conversion_table[roman]
    integer_conversion = 0
    i = 0
    while i < len(roman):
        current_roman = roman[i]
        next_roman = roman[i+1]
        try:
            integer_conversion += conversion_table[current_roman+next_roman]
            # There was a match of two romans (i.e IV, IX), so I have to advance in the string by two.
            i += 2
        except KeyError:
            integer_conversion += conversion_table[current_roman]
            i += 1
    return integer_conversion



