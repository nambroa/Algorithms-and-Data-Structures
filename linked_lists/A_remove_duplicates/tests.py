from unittest import TestCase

from exercises.linked_lists.A_remove_duplicates.algorithm import remove_duplicates_from
from exercises.linked_lists.single_linked_list import SingleLinkedList


class RemoveDuplicatesTest(TestCase):
    def test_removing_duplicates_from_an_empty_list_results_in_an_empty_list(self):
        linked_list = SingleLinkedList.new()
        linked_list.append_from_iterable(iterable=[])
        self.assertEquals(linked_list.length(), 0)
        linked_list = remove_duplicates_from(linked_list=linked_list)
        self.assertEquals(linked_list.length(), 0)

    def test_the_last_element_is_removed_from_the_list_and_the_tail_is_set_properly(self):
        linked_list = SingleLinkedList.new()
        linked_list.append_from_iterable(iterable=[1, 2, 3, 4, 1, 6, 7, 1])
        linked_list = remove_duplicates_from(linked_list=linked_list)
        self.assertFalse(linked_list.has_repeated_nodes())
        self.assertTrue(linked_list.tail().data(), 7)

    def test_all_nodes_but_one_are_removed_since_they_are_all_duplicates(self):
        linked_list = SingleLinkedList.new()
        linked_list.append_from_iterable(iterable=[1, 1, 1, 1, 1])
        self.assertTrue(linked_list.length(), 5)
        linked_list = remove_duplicates_from(linked_list=linked_list)
        self.assertTrue(linked_list.length(), 1)
        self.assertTrue(linked_list.head().data(), 1)
        self.assertEquals(linked_list.head(), linked_list.tail())
