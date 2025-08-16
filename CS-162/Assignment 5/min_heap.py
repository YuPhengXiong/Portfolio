# Name: YuPheng Xiong
# OSU Email: xiongyup@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 5
# Due Date: March 4, 2024
# Description: This program uses the imported functions from dynamic_array, and uses it for the new class MinHeap,
# With its functions add, is_empty, get_min, remove_min, build_heap, size, clear, and heapsort.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        TODO: Adds a new variable into the MinHeap.
        """
        current_length = self._heap.length()
        current_index = current_length
        if self._heap.length() == 0:
            self._heap.append(node)
            return
        self._heap.append(node)
        while current_index != 0:
            parent_index = int((current_index - 1) / 2)
            parent = self._heap.get_at_index(parent_index)
            if parent > node:
                temp_parent = parent_index
                parent_index = current_index
                current_index = temp_parent
                self._heap.set_at_index(parent_index, parent)
                self._heap.set_at_index(current_index, node)
            else:
                return

    def is_empty(self) -> bool:
        """
        TODO: Returns true or false for it the statement is true.
        """
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        TODO: Returns an object with the minimum number in the heap.
        """
        if self._heap.length() == 0:
            raise MinHeapException
        return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        TODO: Identity's the minimal number and removes it for the next index and continues till there is nothing left.
        """
        min_value = self._heap[0]
        self._heap.set_at_index(0, self._heap[self._heap.length() - 1])
        self._heap.remove_at_index(self._heap.length() - 1)
        _percolate_down(self._heap, 0, self._heap.length())
        return min_value

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Receives a DynamicArray with objects in any order, and build a MinHeap from the array.
        """
        new_heap = DynamicArray()
        for r in range(da.length()):
            _value = da[r]
            new_heap.append(_value)
        self._heap = new_heap
        parent = da.length() // 2 - 1
        while parent >= 0:
            _percolate_down(self._heap, parent, da.length())
            parent -= 1

    def size(self) -> int:
        """
        TODO: Returns the heap length.
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        TODO: Clears the contents or objects in MinHeap.
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    parent = da.length() // 2 - 1
    last = da.length() - 1
    for r in range(parent, -1, -1):
        _percolate_down(da, r, da.length())
    while last > 0:
        parent_node = da[0]
        da[0] = da[last]
        da[last] = parent_node
        _percolate_down(da, 0, last)
        last -= 1


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int, last: int) -> None:
    """
    TODO: Write your implementation
    """
    while parent < last:
        left_child = parent * 2 + 1
        right_child = parent * 2 + 2
        min_child = parent
        if left_child < last and da[left_child] < da[min_child]:
            min_child = left_child
        if right_child < last and da[right_child] < da[min_child]:
            min_child = right_child
        if left_child < last and right_child < last and da[left_child] == da[right_child] \
                and da[left_child] < da[min_child]:
            min_child = left_child
        if min_child == parent:
            break
        temp = da[parent]
        da[parent] = da[min_child]
        da[min_child] = temp
        parent = min_child
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
