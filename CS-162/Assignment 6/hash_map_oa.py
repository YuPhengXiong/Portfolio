# Name: YuPheng Xiong
# OSU Email: xiongyup@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 3/14/2024
# Description: A hashmap that includes a HashMap class which interacts with a dynamic array and linked list class.
#           Several methods interact with one another to build the hash map, using open addressing to handle collisions.

from a6_include import (DynamicArray, DynamicArrayException, HashEntry,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(None)

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number to find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        TODO: This function updates the key and values pairs in the hash map.
         If the value already exist within the hash map, it will be replaced with the current value, and if the key
         is not in the hash map, then it will be put into the map.
        """
        # Sets variables used for the following codes below.
        empty = 0
        probe_counter = 0
        hash_func = self._hash_function(key)

        # Checks the capacity of the table, and will double if requirement is met.
        if self.table_load() >= 0.5:
            new_capacity = self.get_capacity() * 2
            self.resize_table(new_capacity)

        # While empty is equivalent to 0, sets up the quadratic probe with the variables we were given above.
        # it will also set up the buckets and placements on the hash map.
        while empty == 0:
            quadratic_probe = ((hash_func + (probe_counter * probe_counter)) % self.get_capacity())
            bucket_available = self._buckets.get_at_index(quadratic_probe)
            placement = (HashEntry(key, value))

            # If bucket is none, then sets empty to 1 and increase the size buy 1.
            if bucket_available is None:
                empty = 1
                self._buckets.set_at_index(quadratic_probe, placement)
                self._size = self._size + 1

            # If the bucket at the index is equivalent to key, set empty to 1
            if key == self._buckets.get_at_index(quadratic_probe).key:
                empty = 1
                # If key is equivalent to key is shown true, creates new size the adds 1 to size.
                if key == self._buckets.get_at_index(quadratic_probe).is_tombstone is True:
                    self._size - self._size + 1
                self._buckets.set_at_index(quadratic_probe, placement)

            # Increase the probe_counter by one to keep the quadratic probe formula accurate.
            probe_counter += 1

    def resize_table(self, new_capacity: int) -> None:
        """
        TODO: A function that resizes the key and values on the map through a series of other functions.
        """
        # Checks if the capacity is less than size, and returns if true.
        if new_capacity < self.get_size():
            return
        # Checks if capacity is not prime, and if true, sets the capacity to next prime.
        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)

        # Variable holders
        self._size = 0
        self._capacity = new_capacity
        buckets = self._buckets
        self._buckets = DynamicArray()

        # Goes through a loop in new_capacity and appends none.
        for i in range(new_capacity):
            self._buckets.append(None)
        # Adds the new keys and values of the elements gotten from the bucket into the Dynamic Array
        for j in range(buckets.length()):
            element = buckets.get_at_index(j)
            if element:
                if buckets[j].is_tombstone is False:
                    self.put(element.key, element.value)

    def table_load(self) -> float:
        """
        TODO: A function that returns the hash table load.
        """
        # returns size divided by capacity for the result load.
        return self.get_size() / self.get_capacity()

    def empty_buckets(self) -> int:
        """
        TODO: A function that returns empty buckets in the hash table.
        """
        # Variable holders
        empty_count = 0
        hash_capacity = self.get_capacity()

        # Looping through the hash capacity to check if the index is none or bucket is a tombstone is true. and adds 1
        # to the empty count.
        for i in range(hash_capacity):
            if self._buckets.get_at_index(i) is None or \
                    self._buckets[i].is_tombstone is True:
                empty_count += 1
        return empty_count

    def get(self, key: str) -> object:
        """
        TODO: A function that returns the value of key's passed, and if key is not found, returns none.
        """
        if not self.contains_key(key):
            return None

        if self._buckets.length() < 1:
            return None

        # Variable holders
        empty = 0
        probe_counter = 0
        hash_func = self._hash_function(key)

        while empty == 0:
            # Variable holders
            quadratic_probe = ((hash_func + (probe_counter * probe_counter)) % self.get_capacity())
            bucket_available = self._buckets.get_at_index(quadratic_probe)

            if bucket_available is None or \
                    self._buckets.get_at_index(quadratic_probe).is_tombstone is True:
                probe_counter += 1
                return None

            elif key == self._buckets.get_at_index(quadratic_probe).key:
                probe_counter += 1
                return self._buckets.get_at_index(quadratic_probe).value

            probe_counter += 1

    def contains_key(self, key: str) -> bool:
        """
        TODO: A function that returns True or False depending on if a passed key is in place on the hash map.
         If no keys found in the hash map, returns no keys.
        """
        # Variable holders
        empty = 0
        probe_counter = 0
        hash_func = self._hash_function(key)

        while empty == 0:
            # Variable holders
            quadratic_probe = ((hash_func + (probe_counter * probe_counter)) % self.get_capacity())
            bucket_available = self._buckets.get_at_index(quadratic_probe)

            if bucket_available is None:
                probe_counter += 1
                return False

            if key == self._buckets.get_at_index(quadratic_probe).key and \
                    self._buckets.get_at_index(quadratic_probe).is_tombstone is False:
                probe_counter += 1
                return True

            probe_counter += 1

    def remove(self, key: str) -> None:
        """
        TODO: A function that removes the keys that have been passed, and does nothing otherwise.
        """
        if not self.contains_key(key):
            return None

        if self._buckets.length() < 1:
            return None

        # Variable holders
        empty = 0
        probe_counter = 0
        hash_func = self._hash_function(key)

        while empty == 0:
            # Variable holders
            quadratic_probe = ((hash_func + (probe_counter * probe_counter)) % self.get_capacity())
            bucket_available = self._buckets.get_at_index(quadratic_probe)

            if key == self._buckets.get_at_index(quadratic_probe).key:
                if bucket_available is True:
                    return
                self._buckets.get_at_index(quadratic_probe).is_tombstone = True
                self._buckets.set_at_index(quadratic_probe, self._buckets.get_at_index(quadratic_probe))
                self._size = self._size - 1
                return

            if bucket_available is None:
                return

            if self._buckets.length() <= quadratic_probe:
                return

            probe_counter += 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        TODO: A function that returns a Dynamic Array where every bucket contains a tuple and adds the keys and values.
         Otherwise does nothing.
        """
        # Variable holders
        da = DynamicArray()

        for i in range(self._buckets.length()):
            bucket = self._buckets.get_at_index(i)
            if bucket:
                if bucket.is_tombstone is False:
                    da.append((bucket.key, bucket.value))
        return da

    def clear(self) -> None:
        """
        TODO: A function that clears the contents inside the hash map.
        """
        # Loop that checks if set index is inside the bucket, and if so, set size to 0 to reset.
        for index in range(self._buckets.length()):
            self._buckets.set_at_index(index, None)
            self._size = 0

    def __iter__(self):
        """
        TODO: A function that allows itself to iterate across the map.
        """
        self._index = 0

        return self

    def __next__(self):
        """
        TODO: A function that returns the next item in hash map, based on location of the iterate.
        """
        try:
            value = self._buckets[self._index]
            while value is None or value.is_tombstone is True:
                self._index += 1
                value = self._buckets[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(25, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        if m.table_load() > 0.5:
            print(f"Check that the load factor is acceptable after the call to resize_table().\n"
                  f"Your load factor is {round(m.table_load(), 2)} and should be less than or equal to 0.5")

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(11, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.resize_table(2)
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(12)
    print(m.get_keys_and_values())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - __iter__(), __next__() example 1")
    print("---------------------")
    m = HashMap(10, hash_function_1)
    for i in range(5):
        m.put(str(i), str(i * 10))
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)

    print("\nPDF - __iter__(), __next__() example 2")
    print("---------------------")
    m = HashMap(10, hash_function_2)
    for i in range(5):
        m.put(str(i), str(i * 24))
    m.remove('0')
    m.remove('4')
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)
