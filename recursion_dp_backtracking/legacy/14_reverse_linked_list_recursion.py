"""

Reverse a linked list using recursion.

Example :
Given 1->2->3->4->5->NULL,

return 5->4->3->2->1->NULL.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next_element = None

class LinkedList:
    def __init(self, head):
        self.head = head  # Should be a ListNode

    def Reverse_List_Recursion(self, node):
        if node.next_element is None:
            # Reach the end, set the ending element of the list as the new head.
            self.head = node
            return
        self.Reverse_List_Recursion(node.next_element)
        next_node = node.next_element
        next_node.next_element = node
        node.next_element = None

    def reverseList(self, p):
        # @param A : head node of linked list
        # @return the head node in the linked list
        self.head = p
        self.Reverse_List_Recursion(p)
        return self.head