class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph:
    def __init__(self, vertices):
        self.V = vertices  
        self.edges = []  

    def add_edge(self, source, destination, weight):
        self.edges.append(Edge(source, destination, weight))

    def bellman_ford(self, start):
        distance = [float('inf')] * self.V
        predecessor = [None] * self.V
        distance[start] = 0

        for _ in range(self.V - 1):
            for edge in self.edges:
                if distance[edge.source] != float('inf') and \
                   distance[edge.source] + edge.weight < distance[edge.destination]:
                    distance[edge.destination] = distance[edge.source] + edge.weight
                    predecessor[edge.destination] = edge.source

        for edge in self.edges:
            if distance[edge.source] != float('inf') and \
               distance[edge.source] + edge.weight < distance[edge.destination]:
                print("Граф содержит отрицательный цикл")
                return None, None

        return distance, predecessor

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 1, 1)
    g.add_edge(3, 4, 5)
    g.add_edge(4, 3, -3)

    distances, predecessors = g.bellman_ford(0)
    if distances is not None:
        print("Кратчайшие расстояния от вершины 0:")
        for i in range(len(distances)):
            print(f"До вершины {i}: {distances[i]}")
