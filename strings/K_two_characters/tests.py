from unittest import TestCase

from strings.K_two_characters.algorithm import two_characters


class TwoCharactersTest(TestCase):
    def test_returns_length_0_for_string_t_created_from_empty_string(self):
        string = ""
        self.assertEqual(two_characters(string), 0)

    def test_returns_length_2_for_string_t_created_from_string_abca(self):
        string = "abca"
        self.assertEqual(two_characters(string), 2)

    def test_returns_length_5_for_string_t_created_from_string_beabeefeab(self):
        string = "beabeefeab"
        self.assertEqual(two_characters(string), 5)