"""

LINKED LISTS - QUESTION 6

Implement a function to check if a linked list is a palindrome

Strings are ascii 128 based. So 128 possibilities per char. Input will be valid. --> ASK THIS IN INTERVIEW

"""

from stacks.stack import Stack

"""


SOLUCIONES:

+ Naive: revertir la lista y compararla con la original

+ Copado: te das cuenta que solo necesitas ver si la primer mitad revertida de la lista es igual a la segunda mitad
          Usas un fast runner que itera de a 1, y un slow runner que itera 1 por c/2 del fast runner, para saber
          donde esta la mitad de la lista. Cuando el fast runner llego al final, el slow runner estara en la mitad.
          Por c/u que el slow runner mira, lo pusheas a un STACK. Entonces, al finalizar, te queda la primera mitad
          revertida. Ahora seguis moviendo el slow runner y comparas con el tope del stack. Si es igual, seguis
          moviendote. Si terminaste, es true. Si en alguno no da igual, es false.


"""

from single_linked_list import SingleLinkedList


def is_palindrome(list):
    if not list.head():
        return True  # Empty lists are empty strings, and as such they are palindromes.
    fast_runner = list.head()
    slow_runner = list.head()
    reversed_half = Stack.new()
    i = 0
    # Position slow runner in the middle of the linked list.
    while fast_runner is not None:
        fast_runner = fast_runner.next_element()
        i += 1
        if i % 2 == 0:
            reversed_half.push(slow_runner)
            slow_runner = slow_runner.next_element()
    if i % 2 != 0:  # Edge case for odd length linked lists.
        reversed_half.push(slow_runner)
    while slow_runner is not None:
        elem = reversed_half.pop()
        if slow_runner.data() != elem.data():
            return False
        slow_runner = slow_runner.next_element()
    return True

list1 = SingleLinkedList.new()
list1.append_from_iterable(iterable=['a', 'b', 'a'])
assert is_palindrome(list=list1)
list1 = SingleLinkedList.new()
list1.append_from_iterable(iterable=[])
assert not is_palindrome(list=list1)
list1 = SingleLinkedList.new()
list1.append_from_iterable(iterable=[''])
assert is_palindrome(list=list1)
list1 = SingleLinkedList.new()
list1.append_from_iterable(iterable=['a', 'b', 'b', 'a'])
assert is_palindrome(list=list1)
list1 = SingleLinkedList.new()
list1.append_from_iterable(iterable=['a', 'b', 'c', 'a'])
assert not is_palindrome(list=list1)
