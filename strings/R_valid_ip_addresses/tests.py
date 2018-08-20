from unittest import TestCase

from strings.R_valid_ip_addresses.algorithm import restore_ip_addresses_from


class RestoreIPAddressesTest(TestCase):
    def test_ip_addresses_are_restored_successfully(self):
        restored_ip_addresses = ['255.255.11.135', '255.255.111.35']
        self.assertEqual(restore_ip_addresses_from("25525511135"), restored_ip_addresses)

    def test_one_ip_address_is_restored(self):
        restored_ip_address = ['255.255.255.255']
        self.assertEqual(restore_ip_addresses_from("255255255255"), restored_ip_address)

    def test_two_ip_addresses_are_restored(self):
        restored_ip_addresses = ['200.189.21.187', '200.189.211.87']
        self.assertEqual(restore_ip_addresses_from("20018921187"), restored_ip_addresses)

    def test_several_ip_addresses_are_restored(self):
        restored_ip_addresses = ['1.122.121.112', '11.22.121.112', '11.221.21.112', '11.221.211.12', '112.2.121.112',
                                 '112.21.21.112', '112.21.211.12', '112.212.1.112', '112.212.11.12', '112.212.111.2']
        self.assertEqual(restore_ip_addresses_from("1122121112"), restored_ip_addresses)