from unittest import TestCase

from strings.F_string_compression.algorithm import compress_string


class StringCompressionTest(TestCase):
    def test_string_of_one_repeated_letter_gets_compressed_successfully(self):
        self.assertEqual(compress_string('aaaa'), 'a4')

    def test_string_of_multiple_repeated_letters_gets_compressed_successfully(self):
        self.assertEqual(compress_string('aaaabbbaaccde'), 'a4b3a2c2d1e1')

    def test_string_compression_returns_original_string_since_compression_is_longer_than_the_original(self):
        self.assertEqual(compress_string('abcde'), 'abcde')