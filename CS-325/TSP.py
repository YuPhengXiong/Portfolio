def solve_tsp(G):
    n = len(G)  # number of cities
    seen = [False] * n  # to keep track of visited cities
    path = []  # stores the path taken
    current_city = 0  # start from the first city (node 0)

    seen[current_city] = True
    path.append(current_city)

    for a in range(n - 1):
        # Find the nearest unvisited city
        nearest_city = None
        min_distance = float('inf')

        for i in range(n):
            if not seen[i] and 0 < G[current_city][i] < min_distance:
                nearest_city = i  # moves on the next city
                min_distance = G[current_city][i]

        # Move to the nearest city
        seen[nearest_city] = True
        path.append(nearest_city)
        current_city = nearest_city

    # Return to the starting city
    path.append(path[0])

    return path


G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
]

# Output the path taken
print(solve_tsp(G))
