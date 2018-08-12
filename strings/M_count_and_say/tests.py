from unittest import TestCase

from strings.M_count_and_say.algorithm import count_and_say


class CountAndSayTest(TestCase):

    def test_count_and_say_of_one(self):
        self.assertEqual(count_and_say(1), '1')

    def test_count_and_say_of_two(self):
        self.assertEqual(count_and_say(2), '11')

    def test_count_and_say_of_three(self):
        self.assertEqual(count_and_say(3), '21')

    def test_count_and_say_of_four(self):
        self.assertEqual(count_and_say(4), '1211')

    def test_count_and_say_of_five(self):
        self.assertEqual(count_and_say(5), '111221')
