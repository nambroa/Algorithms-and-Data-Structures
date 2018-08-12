"""

Write a method to compute all permutations of a string whose characters are not necessarily unique.
The list of permutations should not have duplicates

Examples:
    Input: AB
    Output: AB, BA

    Input: AA
    Output: AA

    Input: ABC
    Output: ABC, ACB, BAC, BCA, CBA, CAB

    Input: ABA
    Output: ABA, AAB, BAA

    Input: ABCA
    Output: AABC AACB ABAC ABCA ACBA ACAB BAAC BACA BCAA CABA CAAB CBAA

QUESTIONS YOU SHOULD ASK:

+ Can the string be empty? Yes .In that case, what do you want me to return? ""
+ Will I always get a valid string as an input: Yes, you will never get other structs or None.
+ Will the string always contain repeated chars? No, it may or may not happen.

"""

"""
ALGORITHM 1: Same idea as exercise F, except we now only store the unique permutations.

Complexity: Worst case scenario, O ((N-1!) * N) (I think so)

N-1! Comes from the permutations loop, as you will never loop through all N! permutations. Each loop takes at worst
O(N) since permutation[:i] + first_char + permutation[i:] can be at worst O(N) length.

"""


def _get_all_non_repeated_permutations_of(string, unique_stored_permutations):
    # Base Case
    if len(string) == 0:
        return ""
    first_char = string[0]
    permutations = _get_all_non_repeated_permutations_of(string[1:len(string)], unique_stored_permutations)
    extended_permutations = []
    if permutations == '':
        return [first_char]
    else:
        for permutation in permutations:
            for i in range(len(permutation)+1):
                new_permutation = permutation[:i] + first_char + permutation[i:]
                try:
                    # If the key new_permutation is found, it means I had already made it and it's a repeat.
                    unique_stored_permutations[new_permutation] += 1
                except KeyError:
                    # Since a KeyError was raised, new_permutation is, actually, a new permutation.
                    unique_stored_permutations[new_permutation] = 1
                    extended_permutations.append(new_permutation)
        return extended_permutations


def get_all_non_repeated_permutations_of(string):
    if string is None:
        raise ValueError("No string was provided.")
    if len(string) == 0:
        return [""]
    if len(string) == 1:
        return [string]
    unique_stored_permutations = {}
    return _get_all_non_repeated_permutations_of(string, unique_stored_permutations)

"""

ALGORITHM 2
Complexity: This is at worst case O(N! *N) with all unique characters in a string. However, we can save time in relation to how
many repeated characters the string has. We first build a hashmap that counts how many times each character appears.
Then, for each unique character that our hashmap detected, we build the permutations with that character as a prefix,
subtracting one to the number of appearances of that unique character in the hashmap.

This way, in a case of a string like "aaaaa", we only go through it once, and return the only permutation available,
doing it in O(N).

"""


def make_character_appearances_hashmap(string):
    hashmap = {}
    for char in string:
        try:
            hashmap[char] += 1
        except KeyError:  # Pythonic way is to use try-catch instead of if-else.
            hashmap.update({char: 1})
    return hashmap


def _better_get_all_non_repeated_permutations_of(character_appearances_hashmap, prefix, remaining, permutations):
    # Base case. Permutation completed
    if remaining == 0:
        permutations.append(prefix)
        return permutations

    # Try remaining letters for next char and generate remaining permutations.
    for char in character_appearances_hashmap:
        number_of_appearances = character_appearances_hashmap[char]
        if number_of_appearances > 0:
            character_appearances_hashmap[char] = number_of_appearances - 1
            _better_get_all_non_repeated_permutations_of(character_appearances_hashmap, prefix+char, remaining-1, permutations)
            character_appearances_hashmap[char] = number_of_appearances
    return permutations


def better_get_all_non_repeated_permutations_of(string):
    character_apparitions_hashmap = make_character_appearances_hashmap(string)
    permutations = _better_get_all_non_repeated_permutations_of(character_apparitions_hashmap, "", len(string), [])
    return permutations

