from unittest import TestCase

from arrays.D_maximum_absolute_difference.algorithm import maximum_absolute_difference


class MaximumAbsoluteDifferenceTest(TestCase):
    def test_maximum_absolute_difference_is_returned_successfully(self):
        self.assertEquals(5, maximum_absolute_difference([1, 3, -1]))
