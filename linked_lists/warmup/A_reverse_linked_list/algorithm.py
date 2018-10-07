# Reverse a singly-linked list.
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# 1 needs to point at null.
# 2 needs to point at 1.
# We iteratively go through the linked list. We need to store the previous and current node. Our objective is to
# Make the current node point to the previous node only (since this isn't a double-linked list).


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_linked_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Check for empty input or empty list.
        if head is None or head.next is None:
            return head
        current_node = head
        previous_node = None
        while current_node is not None:
            old_next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = old_next_node
        return previous_node

