"""

STACKS AND QUEUES - QUESTION 6

An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
People must adopter either the "oldest" of all animals at the shelter, or they can selecter whether they would
prefer a dog or a cat (and would receive the oldest animal of that type). They cannot select which specific
animal they would like. Create the data structures to maintain this system and implement operations such as
enqueue, dequeueAny, dequeueDog and dequeueCat. You may use linked-lists.

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes

"""
from datetime import datetime

import pytz

from queue import Queue


class Animal(object):
    def __init__(self, **kwargs):
        self._timestamp = datetime.now(pytz.utc)

    @classmethod
    def new(cls):
        animal = cls()
        return animal

    def time_of_arrival(self):
        return self._timestamp

    def is_cat(self):
        return False

    def is_dog(self):
        return False


class Dog(Animal):
    def is_dog(self):
        return True


class Cat(Animal):
    def is_cat(self):
        return True


class AnimalShelter(object):
    def __init__(self, **kwargs):
        self.cats = Queue.new()
        self.dogs = Queue.new()

    def enqueue(self, animal):
        if animal.is_cat():
            self.cats.insert(animal)
        self.dogs.insert(animal)

    def dequeue_dog(self):
        if not self.dogs.is_empty():
            return self.dogs.pop()
        raise ValueError("No dogs to give!")

    def dequeue_cat(self):
        if not self.cats.is_empty():
            return self.cats.pop()
        raise ValueError("No cats to give!")

    def dequeue_any(self):
        if self.cats.is_empty():
            return self.dequeue_dog()
        if self.dogs.is_empty():
            return self.dequeue_cat()
        first_cat = self.cats.peek()
        first_dog = self.dogs.peek()
        if first_cat.time_of_arrival() < first_dog.time_of_arrival():
            return first_cat
        return first_dog