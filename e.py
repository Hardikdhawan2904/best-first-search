from queue import PriorityQueue

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, cost):
        self.adj_list[u].append((v, cost))
        self.adj_list[v].append((u, cost))  # Undirected graph

    def best_first_search(self, start, goal, heuristic):
        visited = [False] * self.V
        pq = PriorityQueue()
        pq.put((heuristic[start], start))  # (heuristic, node)
        visited[start] = True

        print("\nBest First Search Path:")
        while not pq.empty():
            node = pq.get()[1]
            print(node, end=" ")

            if node == goal:
                print("\nGoal reached!")
                return

            for neighbor, _ in self.adj_list[node]:
                if not visited[neighbor]:
                    pq.put((heuristic[neighbor], neighbor))
                    visited[neighbor] = True

        print("\nGoal not reachable.")

# Example graph
g = Graph(8)
edges = [
    (0, 1, 2), (0, 2, 1), (1, 3, 4), (1, 4, 2), (2, 5, 3),
    (3, 6, 6), (4, 6, 5), (5, 6, 4), (6, 7, 2)
]

for u, v, cost in edges:
    g.add_edge(u, v, cost)

heuristic = [7, 6, 2, 3, 6, 5, 1, 0]  # Example heuristic values
g.best_first_search(0, 7, heuristic)
