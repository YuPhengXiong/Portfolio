import heapq


def minEffort(puzzle):
    rows = len(puzzle)
    columns = len(puzzle[0])
    end = rows - 1, columns - 1
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # initialize set so we don't traverse onto nodes we've already visited
    seen = set()

    # keep a running minimum effort variable, and initialize a heap with the current effort for that iteration, as well as "a" and "b" position
    minimum_effort = 0
    heap = [(0, 0, 0)]

    while heap:
        # pop our current effort and position, add it to seen
        current_effort, a, b = heapq.heappop(heap)
        seen.add((a, b))

        minimum_effort = max(minimum_effort, current_effort)
        if (a, b) == end:
            return minimum_effort

        for x, y in neighbors:
            new_a = a + x
            new_b = b + y
            if new_a >= rows or new_a < 0 or new_b >= columns or new_b < 0 or (new_a, new_b) in seen:
                continue
            effort = abs(puzzle[new_a][new_b] - puzzle[a][b])
            heapq.heappush(heap, (effort, new_a, new_b))

    return minimum_effort


print(minEffort([[1, 3, 5], [2, 8, 3], [3, 4, 5]]))
