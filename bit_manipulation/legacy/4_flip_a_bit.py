"""

You have an integer and you can flip exactly one bit from a 0 to an 1. Write code to find the length of the
longest sequence of 1's you could create.

EXAMPLE INPUT: 1775 (binary= 11011101111)
EXAMPLE OUTPUT: 8

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes
+ Can I assume only positive numbers? Yes

"""

# For an integer, get the alternating sequences of 0's and 1's that contain it, reversed in order to match
# Binary indexation (which is the opposite of an index, since the position of the 1 in 001 is position 0)


class Solution(object):
    def flip_a_bit(self, integer):
        alternating_sequences = self.get_alternating_sequences_of_(integer)
        already_flipped = False
        longest_sequence = 0
        current_length = 0
        # Check for zeroes at the beggining.
        if alternating_sequences[0] == 1:
            already_flipped = True
            current_length += 1
        index = 1
        for digit_count in alternating_sequences[1:]:
            if index % 2 == 0:  # It means we are counting 0's.
                if digit_count == 1:
                    if already_flipped:
                        current_length = alternating_sequences[index-1]
                    else:
                        already_flipped = True
                        current_length += digit_count
                elif digit_count > 1:
                    longest_sequence = max(longest_sequence, current_length)
                    current_length = 0
            else: # Counting 1's
                current_length += digit_count
            longest_sequence = max(longest_sequence, current_length)
            index += 1
        longest_sequence = max(longest_sequence, current_length)
        return longest_sequence

    def get_alternating_sequences_of_(self, integer):
        alternating_sequences = []
        current_sequence_count = 0
        check_for = 0
        # We want the first elem of the list to be the number of zeroes, so we know how the sequence behaves.
        # This way, the indexes 0, 2, 4...contains the zeroes and the 1, 3, 5.. contain the ones
        while integer != 0:
            if check_for == 0:
                if integer & 1 == 0:  # Last current digit is a zero.
                    current_sequence_count += 1
                else:
                    check_for = 1
                    alternating_sequences.append(current_sequence_count)
                    current_sequence_count = 1
            elif check_for == 1:
                if integer & 1 == 1:  # Last current digit is a one.
                    current_sequence_count += 1
                else:
                    check_for = 0
                    alternating_sequences.append(current_sequence_count)
                    current_sequence_count = 1
            integer >>= 1  # Shift integer to the right, losing the least valued digit that I just checked.
        alternating_sequences.append(current_sequence_count)
        return alternating_sequences


