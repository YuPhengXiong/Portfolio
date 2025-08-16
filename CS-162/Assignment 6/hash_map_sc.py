# Name: YuPheng Xiong
# OSU Email: xiongyup@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 3/14/2024
# Description: A hashmap that includes a HashMap class which interacts with a dynamic array and linked list class.
#           Several methods interact with one another to build the hash map, using open addressing to handle collisions.


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

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
        Increment from given number and the find the closest prime number
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
        # Checks the capacity of the table, and will double if requirement is met.
        if self.table_load() >= 1:
            new_capacity = self.get_capacity() * 2
            self.resize_table(new_capacity)

        # Variable holders
        hash_fun_1 = self._hash_function(key)
        hash_index = hash_fun_1 % self.get_capacity()

        # Checks if a passed key at a certain index is not none, and then remove old key and inserts new key with value.
        if self._buckets.get_at_index(hash_index).contains(key) is not None:
            self._buckets.get_at_index(hash_index).remove(key)
            self._buckets.get_at_index(hash_index).insert(key, value)
        # Checks if key at index is none, and if so then inserts new key and values, and increase size by 1.
        elif self._buckets.get_at_index(hash_index).contains(key) is None:
            self._buckets.get_at_index(hash_index).insert(key, value)
            self._size = self._size + 1

    def resize_table(self, new_capacity: int) -> None:
        """
        TODO: A function that resizes the key and values on the map through a series of other functions.
        """
        if new_capacity < 1:
            return

        # Variable holders for LinkedList and DynamicArray
        LL = LinkedList()
        da = DynamicArray()

        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)
        # Loop every index in new capacity, append linked list to dynamic array
        for i in range(new_capacity):
            da.append(LinkedList())
        # A loop through the capacity, creating nodes to add buckets to certain index of buckets, if bucket is none,
        # adds key and values of node.
        for b in range(self.get_capacity()):
            node_to_add = self._buckets.get_at_index(b)
            if node_to_add is not None:
                for node in node_to_add:
                    LL.insert(node.key, node.value)

        # Variable holders
        self._size = 0
        self._buckets = da
        self._capacity = new_capacity

        for node in LL:
            self.put(node.key, node.value)

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
        hash_table_capacity = self.get_capacity()
        # Looping through the hash capacity to check if the index is none or bucket is a tombstone is true. and adds 1
        # to the empty count.
        for i in range(hash_table_capacity):
            if self._buckets.get_at_index(i).length() == 0:
                empty_count += 1
        return empty_count

    def get(self, key: str):
        """
        TODO: A function that returns the value of key's passed, and if key is not found, returns none.
        """
        # Variable holders
        hash_fun_1 = self._hash_function(key)
        hash_index = hash_fun_1 % self.get_capacity()

        if not self.contains_key(key):
            return None
        else:
            return self._buckets.get_at_index(hash_index).contains(key).value

    def contains_key(self, key: str) -> bool:
        """
        TODO: A function that returns True or False depending on if a passed key is in place on the hash map.
         If no keys found in the hash map, returns no keys.
        """
        # Variable holders
        hash_fun_1 = self._hash_function(key)
        hash_index = hash_fun_1 % self.get_capacity()

        if self.get_capacity() == 0:
            return False

        if self._buckets.get_at_index(hash_index).contains(key):
            return True
        else:
            return False

    def remove(self, key: str) -> None:
        """
        TODO:  A function that removes the keys that have been passed, and does nothing otherwise.
        """
        # Variable holders
        hash_fun_1 = self._hash_function(key)
        hash_index = hash_fun_1 % self.get_capacity()

        if not self.contains_key(key):
            return

        if self._buckets.get_at_index(hash_index).contains(key):
            self._buckets.get_at_index(hash_index).remove(key)
            self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        TODO: A function that returns a Dynamic Array where every bucket contains a tuple and adds the keys and values.
         Otherwise does nothing.
        """
        da = DynamicArray()

        for i in range(self._buckets.length()):
            buckets = self._buckets[i]
            for b in buckets:
                da.append((b.key, b.value))
        return da

    def clear(self) -> None:
        """
        TODO: A function that clears the contents inside the hash map.
        """
        LL = LinkedList()
        hash_table_capacity = self.get_capacity()
        # Loop that checks if set index is inside the bucket, and if so, set size to 0 to reset.
        for i in range(hash_table_capacity):
            self._buckets.set_at_index(i, LL)
            self._size = 0


def find_mode(da: DynamicArray) -> tuple[DynamicArray, int]:
    """
    TODO: A function that tracks multiple nodes within the map, and will be found based on the values we found, and
     return a tuple and array. It will also display the frequency of the modes.
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    map = HashMap(da.length())
    highest_frequency = 0
    return_da = DynamicArray()

    # A loop through the length of the inputs of dynamic array, creating a key and value based on the arrays. If both
    # value and keys exist, adds 1 to value, and inputs key and values. Otherwise set value to 1.
    for i in range(da.length()):
        key = da.get_at_index(i)
        value = map.get(key)
        if value:
            value += 1
            map.put(key, value)
        else:
            value = 1
            map.put(key, value)
        # Checks if value is greater than the highest frequency, and if so set frequency to value, and apends they key
        # to the Dynamic Array. Otherwise, checks if equivalent and appends.
        if value > highest_frequency:
            highest_frequency = value
            return_da = DynamicArray()
            return_da.append(key)
        elif value == highest_frequency:
            return_da.append(key)

    return return_da, highest_frequency


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
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

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
    m = HashMap(53, hash_function_1)
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

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
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

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")
