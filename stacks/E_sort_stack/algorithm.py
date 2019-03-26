"""

STACKS AND QUEUES - QUESTION 5

Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack.
You may not copy the elements into any other data structure (such as an array).
The stack supports push, pop, peek and isEmpty

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes, but it can only use the stack and the temporary stack, no other data structure.
  (not even additional attirbutes)
+ Will the stack always contain elements that can be "ordered"? Yes
+ Will the input always be valid? Yes

"""
from stacks.stack import Stack

"""

La idea es devolver el stack temporal.

Vamos a pushear desde el stack inicial al temporal, con el objetivo de ir poniendo los minimos en orden.
Esto nos garantiza que en el stack temporal tenes [n1 <= n2 <= ... <= nn], entonces los items más chicos están en la
parte de arriba, osea son los últimos en ser popeados.

Para hacer esto, vamos a sacar un elemento del stack inicial. Nos vamos a fijar si es más chico que el tope del stack
temporal (peek). Si es más chico, vamos a remover elementos del temporal al inicial. Ya que debería estar en el tope.
Ahí pusheamos el elemento al stack temporal. Total, como todo lo que pusheamos del temporal al inicial estaba ordenado,
lo podemos volver a pushear al temporal con el mismo loop manteniendo el orden.

"""


def sort_stack(stack):
    if stack.size() == 0:
        return stack
    temp_stack = Stack.new()
    while not stack.is_empty():
        element = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > element:
            temp_stack_element = temp_stack.pop()
            stack.push(temp_stack_element)
        temp_stack.push(element)
    return temp_stack
