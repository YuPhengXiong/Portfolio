from collections import deque


def solve_puzzle(Board, Source, Destination):
    """Solve the puzzle to find the shortest path from Source to Destination."""

    # returns destination if start is exact same spot
    if Source == Destination:
        return [Source]

    rows = len(Board)
    columns = len(Board[0])

    # Directions: Left, Right, Up, Down
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Determine if location is lock/blocked
    if Board[Source[0]][Source[1]] == "#" or Board[Destination[0]][Destination[1]] == "#":
        return None

    # Queue that stores (row, col, path_to_here)
    queue = deque([(Source[0], Source[1], [Source])])

    # Visited set to keep track of visited cells
    visited = set()
    visited.add(Source)

    # Perform BFS
    while queue:
        row, column, path = queue.popleft()

        # Check all four directions
        for direct in directions:
            new_row, new_col = row + direct[0], column + direct[1]

            # Check if the new position is within bounds and not visited
            if 0 <= new_row < rows and 0 <= new_col < columns:
                if (new_row, new_col) not in visited and Board[new_row][new_col] == "-":
                    # If we reach the destination, return the path
                    if (new_row, new_col) == Destination:
                        return path + [(new_row, new_col)]

                    # Mark the new cell as visited and add to the queue
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, path + [(new_row, new_col)]))

    # If no path is found, return None
    return None


Puzzle = [
    ["-", "-", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["#", "-", "#", "#", "-"],
    ["-", "#", "-", "-", "-"]
]

# Example 1
source = (0, 2)
destination = (2, 2)

path = solve_puzzle(Puzzle, source, destination)
print(path)  # Output should be: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]

# Example 2
source = (0, 0)
destination = (4, 4)

path = solve_puzzle(Puzzle, source, destination)
print(path)  # Output should be: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

# Example 3 (No Path)
source = (0, 0)
destination = (4, 0)

path = solve_puzzle(Puzzle, source, destination)
print(path)  # Output should be: None

# Example 4 (Same Start and End)
source = (0, 0)
destination = (0, 0)

path = solve_puzzle(Puzzle, source, destination)
print(path)  # Output should be: [(0, 0)]
