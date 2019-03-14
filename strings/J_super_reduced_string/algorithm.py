"""

Steve has a string S, consisting of lowercase English alphabetic letters.
In one operation, he can delete any pair of adjacent letters with same value.
For example, string "aabcc" would become either "aab" or "bcc" after operation.

Steve wants to reduce S as much as possible.
To do this, he will repeat the above operation as many times as it can be performed.
Help Steve out by finding and printing S's non-reducible form!

Note: If the final string is empty, print "Empty String" .

QUESTIONS:

+ Can the string be empty? Yes, treat it as requested.
+ Can the input be None or invalid? No.

"""

"""

You need to iterate every 3 elements. The idea is to check if s[i] != s[i+1] != s[i+2], which would mean that
s[i+1] is not surrounded by itself, therefore it's safe to add. This will not check the first and last char, so
you need to do that manually.

Complexity: O(|string})

"""


def get_super_reduced_form_of(string):
    if len(string) == 0:
        return 'Empty String'
    super_reduced_string = ''
    if string[0] != string[1]:
        super_reduced_string += string[0]
    for i in range(len(string) - 2):
        if string[i] != string[i + 1] != string[i + 2]:
            super_reduced_string += string[i + 1]
    if string[-1] != string[-2]:
        super_reduced_string += string[-1]
    if len(super_reduced_string) == 0:
        return 'Empty String'
    else:
        return super_reduced_string
