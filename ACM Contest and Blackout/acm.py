from math import inf

class PathData:
    def __init__(self):
        self.min_1 = inf
        self.min_2 = inf

    def try_new_min(self, value):
        pudo = False

        if value < self.min_1:
            self.min_2 = self.min_1
            self.min_1 = value

            pudo = True
        
        elif value < self.min_2:
            self.min_2 = value
            
            pudo = True

        return pudo

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self,n):
        self.vertexes = list(range(n))
        self.edges = [[] * n]

    def connect(self, start, end, weight):
        self.edges[start].append(Edge(start, end, weight))

        self.edges[end].append(Edge(end, start, weight))

    def two_shortest_paths(self):
        """
        DFS que busca 2 caminos minimos
        """
        pass