from unittest import TestCase

from strings.G_string_rotation.algorithm import is_rotation


class StringRotationTest(TestCase):
    def test_an_empty_string_is_only_a_rotation_of_itself(self):
        self.assertTrue(is_rotation(string1='', string2=''))
        self.assertFalse(is_rotation(string1='', string2='a'))

    def test_two_strings_are_rotations_of_each_other(self):
        self.assertTrue(is_rotation(string1='waterbottle', string2='erbottlewat'))
        self.assertTrue(is_rotation(string1='waterbottle', string2='aterbottlew'))
        self.assertTrue(is_rotation(string1='wawterbottle', string2='wterbottlewa'))

    def test_two_strings_that_are_not_rotations_of_each_other_should_be_classified_as_such(self):
        self.assertFalse(is_rotation(string1='waterbottle', string2='teawbortlt'))
        self.assertFalse(is_rotation(string1='waterbottle', string2='dfghjk'))