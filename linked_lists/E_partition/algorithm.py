"""

LINKED LISTS - QUESTION 4
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes
greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements
less than x. The partition element x can appear anywhere in the "right partition". It does not need to appear
between the left and right partitions.

Note that x does not have to be contained within the list.
Example input: 3 --> 5 --> 8 --> 5 --> 10 --> 2 --> 1 (partition = 5)
Example output: 3 --> 1 --> 2 --> 10 --> 5 --> 5 --> 8

QUESTIONS:

+ Can the linked list be None or empty? Yes
+ Are they all unique numbers? Not necessarily
+ What is x? Integer, object? x is an Int
+ Can I use additional memory? Yes

"""

# A possible approach is to iterate over the list, if the current value is smaller, store it in a linked list L1
# If the current value is higher or the same as x, store it in a linked list L2. Then join both linked lists together
# So the end result would be L1 -> L2.
from linked_lists.single_linked_list import SingleLinkedList


def _validate_linked_list(linked_list):
    if linked_list is None or linked_list.head() is None:
        raise ValueError("Linked list is None or empty.")


def _join_the_lists(smaller_elements_linked_list, bigger_elements_linked_list):
    if smaller_elements_linked_list is None:
        return bigger_elements_linked_list
    if bigger_elements_linked_list is None:
        return smaller_elements_linked_list
    smaller_elements_linked_list.append_node((bigger_elements_linked_list.head()))
    return smaller_elements_linked_list


def partition_around(linked_list, value):
    _validate_linked_list(linked_list)
    current_node = linked_list.head()
    smaller_elements_linked_list = bigger_elements_linked_list = SingleLinkedList.new()
    while current_node is not None:
        if current_node.data() < value:
            # I don't check to add the head here because append_node has that logic already.
            smaller_elements_linked_list.append_node(new_node=current_node)
        else:
            bigger_elements_linked_list.append_node(new_node=current_node)
        current_node = current_node.next_element()
    final_linked_list = _join_the_lists(smaller_elements_linked_list, bigger_elements_linked_list)
    return final_linked_list.head()


# You can do it in place as well. Let's say we have to partition 3->5->8->10 around the value 5.
# We start with current_node being 3. We check the next node 5, storing 3 as previous_node. Since 5 is greater or equal
# Than the value 5 (equal), 3 would be in L1 and 5 in L2. We store those as "L1/L2 pointers". Looking at 8, its greater
# than the value 5, so we add it as the next one of the L2 pointer. Then we change the L2 pointer to 8.
# Finally, since 10 is higher than the value 5, we add it as the next one of the L2 pointer. Then, we join L1 and L2.
# We return the "first element of L1" (store it somewhere) or the "first element of L2" if L1 does not exist.
