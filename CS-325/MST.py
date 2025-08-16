import heapq


def Prims(G):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST)
    of a graph represented by an adjacency matrix.
    """

    n = len(G)
    mst_edges = []  # List to store the edges of the MST
    visited = [False] * n
    min_heap = []   # Priority queue to pick the edge with the smallest weight

    # Start from vertex 0
    visited[0] = True
    # b stands for vertex
    for b in range(n):
        if G[0][b] != 0:  # If there is an edge from vertex 0 to v
            heapq.heappush(min_heap, (G[0][b], 0, b))  # (weight, from, to)

    # a stands for edge
    while min_heap:
        weight, a, b = heapq.heappop(min_heap)  # Get the edge with the smallest weight

        if visited[b]:
            continue  # Skip if the vertex is already included in MST

        # Add the edge to the MST
        mst_edges.append((a, b, weight))
        visited[b] = True

        # Add all edges from v to the heap
        for c in range(n):
            if not visited[c] and G[b][c] != 0:
                heapq.heappush(min_heap, (G[b][c], b, c))

    return mst_edges


G = [[0, 8, 5, 0, 0, 0, 0],
     [8, 0, 10, 2, 18, 0, 0],
     [5, 10, 0, 3, 0, 16, 0],
     [0, 2, 3, 0, 12, 30, 14],
     [0, 18, 0, 12, 0, 0, 4],
     [0, 0, 16, 30, 0, 0, 26],
     [0, 0, 0, 14, 4, 26, 0]]

print(Prims(G))
