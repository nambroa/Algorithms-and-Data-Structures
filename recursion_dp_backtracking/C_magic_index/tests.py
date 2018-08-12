from unittest import TestCase

from exercises.recursion_dp_backtracking.C_magic_index.algorithm import find_magic_index_in, \
    find_follow_up_magic_index_in


class MagicIndexTest(TestCase):
    def test_magic_index_for_array_is_2(self):
        array = [-11, 1, 2, 5, 6, 7]
        self.assertEquals(find_magic_index_in(array), 2)

    def test_magic_index_for_array_is_1(self):
        array = [-2, 1, 4, 7, 9, 23]
        self.assertEquals(find_magic_index_in(array), 1)

    def test_magic_index_for_array_is_4(self):
        array = [-2, -1, 0, 1, 4, 7, 9]
        self.assertEquals(find_magic_index_in(array), 4)

    def test_magic_index_for_array_returns_none(self):
        array =[-4, -2, -1, 0, 9]
        self.assertIsNone(find_magic_index_in(array))

    def test_magic_index_for_empty_array_raises_value_error(self):
        array = []
        self.assertRaises(ValueError, find_magic_index_in, array)


class FollowUpMagicIndexTest(TestCase):
    def test_magic_index_for_array_is_2(self):
        array = [0, 2, 2, 2, 2, 2, 2, 5, 6, 7]
        self.assertEquals(find_follow_up_magic_index_in(array), 2)

    def test_magic_index_for_array_is_1(self):
        array = [-2, 1, 4, 7, 9, 23]
        self.assertEquals(find_follow_up_magic_index_in(array), 1)

    def test_magic_index_for_array_is_4(self):
        array = [-2, -1, 0, 1, 4, 7, 9]
        self.assertEquals(find_follow_up_magic_index_in(array), 4)

    def test_magic_index_for_array_returns_none(self):
        array =[-4, -2, -1, 0, 9]
        self.assertIsNone(find_follow_up_magic_index_in(array))

    def test_magic_index_for_empty_array_raises_value_error(self):
        array = []
        self.assertRaises(ValueError, find_follow_up_magic_index_in, array)