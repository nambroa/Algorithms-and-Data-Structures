"""

Given an input string, reverse the string word by word.

Example:

Given s = "the sky is blue",

return "blue is sky the".

IMPORTANT:

+ A sequence of non-space characters constitutes a word.
+ Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
+ If there are multiple spaces between words, reduce them to a single space in the reversed string.

QUESTIONS:

+ Can the input be None? No
+ Can the input be ''? No
+ Can the input be just empty spaces? Like '            '? No

"""


def reverse(string):
    words_list = string.split()
    return ' '.join([word for word in words_list[::-1]])  # Thank you Python.


# In order to preserve spaces, use strip() instead of split()



"""

Just for comparison: a non Pythonic solution. I mean just look at this.

"""


def is_space_character(char):
    return ord(char) == 32


def get_first_index_from_the_end_that_isnt_a_space(A):
    index = len(A) - 1
    for i in range(len(A) - 1, -1, -1):
        char = A[i]
        if is_space_character(char):
            index -= 1
        else:
            # I finish since I found my first letter.
            break
    return index


def reverseWords(A):
    first_letter_from_the_end_index = get_first_index_from_the_end_that_isnt_a_space(A)
    if not A or (first_letter_from_the_end_index == 0):
        # Case when A is empty or just one letter.
        return A
    reversed_words = []
    beggining_of_word_index = first_letter_from_the_end_index
    end_of_word_index = first_letter_from_the_end_index
    while beggining_of_word_index > -1:
        char = A[beggining_of_word_index]
        if not is_space_character(char):
            beggining_of_word_index -= 1
        else:
            # Word is over. Space character found. I add it to the reversed words list.
            reversed_words.extend(A[beggining_of_word_index + 1:end_of_word_index + 1] + " ")
            beggining_of_word_index -= 1
            end_of_word_index = beggining_of_word_index
            # Advance until I find the end of the next word (there can be multiple spaces).
            whitespace_found = is_space_character(A[beggining_of_word_index])
            while whitespace_found:
                beggining_of_word_index -= 1
                end_of_word_index -= 1
                if beggining_of_word_index <= -1:
                    # String ended.
                    break
                whitespace_found = is_space_character(A[beggining_of_word_index])
    if beggining_of_word_index == -1 and not is_space_character(A[beggining_of_word_index + 1]):
        # Need to add the first word, since it wasnt a whitespace and the while ended before adding it..
        reversed_words.extend(A[beggining_of_word_index + 1:end_of_word_index + 1])
    return "".join([letter for letter in reversed_words])
