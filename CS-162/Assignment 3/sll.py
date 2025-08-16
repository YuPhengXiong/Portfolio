# Name: YuPheng Xiong
# OSU Email: xiongyup@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: January 12, 2024
# Description:


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        TODO: Inserts a new node at the beginning of the list.
        """
        new_node = SLNode(value)

        new_node.next = self._head.next

        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        TODO: Inserts a new node at the end of the list.
        """
        new_node = SLNode(value)

        node = self._head
        while node.next is not None:
            node = node.next

        node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Grabs a new value and inserts it into a specific area in the index list.
        """
        if index < 0 or index > self.length():  # Check index
            raise SLLException('Invalid index position')

        new_node = SLNode(value)  # Create a new node

        current = self._head

        for _ in range(index):  # find the node at the index
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Grabs a new value and removes it from a specific area in the index list.
        """
        if index < 0 or index >= self.length():
            raise SLLException

        current = self._head
        prev = None

        for _ in range(index + 1):
            prev = current
            current = current.next

        prev.next = current.next

    def remove(self, value: object) -> bool:
        """
        TODO: This method removes a value in a Linked List, and determines if the list is true or false,
         based on the value being compared and determines if equivalent from old and new list.
        """
        current = self._head.next
        prev = self._head

        # find the node with the given value
        while current is not None:
            if current.value == value:
                prev.next = current.next
                return True
            prev = current
            current = current.next

        return False

    def count(self, value: object) -> int:
        """
        TODO: This method counts all the elements in the linked list that matches the provided value given.
        """
        count = 0
        current = self._head.next  # Start from the first node

        while current is not None:
            if current.value == value:
                count += 1
            current = current.next

        return count

    def find(self, value: object) -> bool:
        """
        TODO: Returns true or false based on if the provided value is in the list.
        """
        current = self._head.next  # Start at first node

        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Returns a new LinkedList that contains the requested node from the original list,
         starting with the node located at the requested start index.
        """
        if start_index < 0 or start_index >= self.length() or size < 0 or start_index + size > self.length():
            raise SLLException

        new_list = LinkedList()  # Create new linked list
        current = self._head.next
        index = 0

        # Move to start_index
        while index < start_index:
            current = current.next
            index += 1

        # Copy size
        for _ in range(size):
            new_list.insert_back(current.value)
            current = current.next

        return new_list


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
