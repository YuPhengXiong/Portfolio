def powerset(inputSet):
    result = []

    # Defines start location in a list, and where we will add new elements into.
    def backtrack(beginning, location):
        length_set = len(inputSet)
        for a in range(beginning, length_set):
            # We increment the location of index by 1, and add in new element into the [].
            backtrack(a + 1, location + [inputSet[a]])
        # adds every iteration done to the list.
        result.append(location)
    backtrack(0, [])
    return result

