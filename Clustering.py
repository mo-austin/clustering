

import heapq as pq

class Clustering:
    def __init__(self):
        return

    # Find operation in Union-Find data structure
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Union operation in Union-Find data structure
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Kruskal's algorithm for finding minimum spanning tree
    def kruskal(self, distances, k):
        n = len(distances)
        parent = [i for i in range(n)]  # Initialize parent array for Union-Find
        rank = [0] * n  # Initialize rank array for Union-Find
        edges = []  # Initialize list to store edges

        # Create list of edges with their weights
        for i in range(n):
            for j in range(i+1, n):
                edges.append((distances[i][j], i, j))

        pq.heapify(edges)  # Convert edges list into a priority queue

        clusters = n
        while edges:  # Iterate until there are edges left in the priority queue
            weight, u, v = pq.heappop(edges)  # Get edge with minimum weight
            pu = self.find(parent, u)  # Find representative of u
            pv = self.find(parent, v)  # Find representative of v

            if pu != pv:  # If u and v are not in the same set
                clusters -= 1  # Decrement number of clusters
                self.union(parent, rank, pu, pv)  # Union u and v

                if clusters == k:  # Stop when desired number of clusters is reached
                    break

        min_spacing = float('inf')  # Initialize minimum spacing to positive infinity
        while edges:  # Iterate until there are edges left in the priority queue
            weight, u, v = pq.heappop(edges)  # Get edge with minimum weight
            pu = self.find(parent, u)  # Find representative of u
            pv = self.find(parent, v)  # Find representative of v
            if pu != pv:  # If u and v are not in the same set
                min_spacing = weight  # Update minimum spacing
                break  # Exit the loop as we found the minimum spacing

        return min_spacing  # Return minimum spacing of clustering

    # Method to compute maximum possible spacing for clustering
    def compute(self, k, distances):
        return self.kruskal(distances, k)

# Read input from file
def read_input(filename):
    with open(filename, 'r') as file:
        k = int(file.readline().strip())  # Read number of clusters
        n = int(file.readline().strip())  # Read number of points
        distances = []  # Initialize list to store distances
        for _ in range(n):
            row = list(map(float, file.readline().strip().split()))  # Read distances for each point
            distances.append(row)
    return k, distances


