"""

Julius Caesar protected his confidential information by encrypting it in a cipher.
Caesar's cipher rotated every letter in a string by a fixed number K to the right, making it unreadable by his enemies.
Given a string S and a number K, encrypt S and print the resulting string.

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

For example: 'middle-Outz' should be encripted to 'okffng-Qwvb' if k=2

QUESTIONS:

+ What happens if I recieve a character that loops when encripted? Example z and k=3. Return the char c.
+ Can I get an empty string as input? Yes
+ Can the input be None? Yes
+ Can the input be invalid? Like an int? No, only strings.
+ What can the string contain? Any char (including spaces), remember to only encript lowercase and uppercase letters.

"""

"""

Idea: Make an alphabet class that can give you the next letter in the Alphabet of k, so you encapsulate that.

Remember that ord('a') gives you the ASCII value of 'a'.
Also, the ASCII value of 'b' is ord('a')+1. The same follows for the rest of the letters.

chr(27) gives you the str of ASCII value 27.

"""


class Alphabet(object):
    def __init__(self):
        self._alphabet = ['a'] + [chr(ord('a') + i) for i in range(1, 26)]

    def alphabet(self):
        return self._alphabet


class CaesarCipher(object):
    def __init__(self):
        self._alphabet = Alphabet()

    def alphabet(self):
        return self._alphabet.alphabet()

    def get_char_k_spaces_away_from(self, char, k):
        if char not in self.alphabet():
            raise ValueError("Char not in alphabet.")
        index_of_char = ord(char) - 97  # This is because letters start at 97 in ASCII value.
        if 25 < k+index_of_char:
            # This ridiculous line is because the alphabet has 26 letters only, so if it's bigger than 25 I need to loop
            # over it to find the correct char and not raise an IndexError.
            index_of_new_char = (k+index_of_char) % 26
        else:
            index_of_new_char = index_of_char+k
        return self.alphabet()[index_of_new_char]

    def get_conversion_of(self, string, k):
        if string is None:
            raise ValueError("String is None.")
        if len(string) == 0:  # Caesar Cipher of empty strings is just an empty string.
            return string
        caesar_cipher = ''
        for char in string:
            try:
                new_char = self.get_char_k_spaces_away_from(char.lower(), k)
                new_char = new_char.upper() if char.isupper() else new_char
                caesar_cipher += new_char
            except ValueError:  # Char not in alphabet, I don't need to encript it.
                caesar_cipher += char
        return caesar_cipher


# Remember to treat uppercase and lowercase differently!

def get_caesar_cipher_of(string1, k):
    return CaesarCipher().get_conversion_of(string1, k)


