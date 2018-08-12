from unittest import TestCase

from exercises.strings.J_super_reduced_string.algorithm import get_super_reduced_form_of


class SuperReducedString(TestCase):
    def test_super_reduced_string_of_empty_string_should_return_empty_string(self):
        self.assertEqual(get_super_reduced_form_of(''), 'Empty String')

    def test_super_reduced_string_of_aabcc_should_be_b(self):
        self.assertEqual(get_super_reduced_form_of('aabcc'), 'b')

    def test_super_reduced_string_of_aadbcc_should_be_db(self):
        self.assertEqual(get_super_reduced_form_of('aadbcc'), 'db')

    def test_super_reduced_string_of_aadbcce_should_be_dbe(self):
        self.assertEqual(get_super_reduced_form_of('aadbcce'), 'dbe')

    def test_super_reduced_string_of_aadxbcce_should_be_dxbe(self):
        self.assertEqual(get_super_reduced_form_of('aadxbcce'), 'dxbe')

    def test_super_reduced_string_of_caadxbcce_should_be_cdxbe(self):
        self.assertEqual(get_super_reduced_form_of('caadxbcce'), 'cdxbe')