# Name: YuPheng Xiong
# OSU Email: xiongyup@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2
# Due Date: Feburary 2, 2024
# Description: Implement a Bag ADT class by completing the skeleton code provided in the file
#              bag_da.py. You will use the DynamicArray class that you implemented in Part 1 of
#              this assignment as the underlying data storage for your Bag ADT.


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        TODO: Function add element(s) to the bag
        """
        self._da.append(value)
        pass

    def remove(self, value: object) -> bool:
        """
        TODO: Function removes element(s) from the bag
        """
        counter = 0

        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
            return True
        return False

    def count(self, value: object) -> int:
        """
        TODO: Counts the number of instances in the Bag
        """
        count = 0
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        TODO: Clears anything in the bag
        """
        while self._da.length() > 0:
            self._da.remove_at_index(0)

    def equal(self, second_bag: "Bag") -> bool:
        """
        TODO: Checks if the bag is equal to the second bag
        """
        if self._da.length() != second_bag.size():
            return False

        for i in range(self._da.length()):
            if self.count(self._da.get_at_index(i) != second_bag.count(self._da.get_at_index(i))):
                return False

        return True

    def __iter__(self):
        """
        TODO: Creates an iterator that iterate over the Bag's elements
        """
        self._index = 0
        return self

    def __next__(self):
        """
        TODO: Gets the next item in the bag
        """
        if self._index >= self._da.length():
            raise StopIteration
        value = self._da.get_at_index(self._index)
        self._index += 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
