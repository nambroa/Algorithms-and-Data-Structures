from unittest import TestCase

from strings.H_caesar_cipher.algorithm import get_caesar_cipher_of


class CaesarCipherTest(TestCase):
    def test_returns_empty_string_for_cipher_with_empty_string(self):
        string = ""
        self.assertEqual(get_caesar_cipher_of(string1=string, k=45), "")

    def test_returns_encrypted_string_for_cypher_with_valid_input(self):
        string = "middle-Outz"
        self.assertEqual(get_caesar_cipher_of(string1=string, k=2), "okffng-Qwvb")

    def test_returns_encrypted_string_for_cypher_with_valid_input_with_points_and_big_k(self):
        string = "www.abc.xy"
        self.assertEqual(get_caesar_cipher_of(string1=string, k=87), "fff.jkl.gh")
