from unittest import TestCase

from exercises.linked_lists.B_kth_to_last.algorithm import get_kth_to_last_element_from
from exercises.linked_lists.single_linked_list import SingleLinkedList


class GetKthToLastElementTest(TestCase):
    def test_get_kth_to_last_element_just_works_todd_howard_edition(self):
        linked_list = SingleLinkedList.new()
        linked_list.append_from_iterable(iterable=[1, 2, 3, 4, 1, 6, 7, 1])
        self.assertEquals(get_kth_to_last_element_from(linked_list=linked_list, k=0).data(), 1)
        self.assertEquals(get_kth_to_last_element_from(linked_list=linked_list, k=1).data(), 7)
        self.assertEquals(get_kth_to_last_element_from(linked_list=linked_list, k=2).data(), 6)
        self.assertEquals(get_kth_to_last_element_from(linked_list=linked_list, k=3).data(), 1)
        self.assertEquals(get_kth_to_last_element_from(linked_list=linked_list, k=4).data(), 4)
        self.assertEquals(get_kth_to_last_element_from(linked_list=linked_list, k=5).data(), 3)
        self.assertEquals(get_kth_to_last_element_from(linked_list=linked_list, k=6).data(), 2)
        self.assertEquals(get_kth_to_last_element_from(linked_list=linked_list, k=7).data(), 1)
        self.assertRaises(ValueError, get_kth_to_last_element_from, linked_list=linked_list, k=789)
        self.assertRaises(ValueError, get_kth_to_last_element_from, linked_list=SingleLinkedList.new(), k=0)



