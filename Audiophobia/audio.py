from sys import stdin, stdout

class UFDS:
    def __init__(self, size):
        self.padre = [I for I in range(size+1)] # cada nodo es su propio representante
        self.rango = [0] * (size+1) # cada nodo tiene rango 0

    def find_set(self, vertice):
        if not (vertice == self.padre[vertice]): # si el vertice pasado no es igual al padre, se actualiza el padre en la recusion
            self.padre[vertice] = self.find_set(self.padre[vertice])
        
        return self.padre[vertice]
    
    def same_set(self, v, w):
        return self.find_set(v) == self.find_set(w)
    
    def union_set(self, v, w):
        if not self.same_set(v,w): # si no están en el mismo conjunto, se procede a unir
            set_v = self.find_set(v)
            set_w = self.find_set(w)
            
            if self.rango[set_v] > self.rango[set_w]: # si v > w se unen
                self.padre[set_w] = set_v
                
            else: # si es < o =, se unen al reves
                self.padre[set_v] = set_w
                if self.rango[set_v] > self.rango[set_w]: # si encima es = el rango, se aumenta en 1 el del padre
                    self.rango[set_w] += 1

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class PathData:
    def __init__(self):
        self.max_supported = float("inf")
        self.actual_max = 0

    def commit_max(self):
        self.max_supported = self.actual_max

    def try_set_max(self, value):
        self.actual_max = max(self.actual_max, value)
        
    def set_max(self, value):
        self.actual_max = value

class Graph:    
    def __init__(self, nodes = [], edges = [], cant_nodes=None):
        self.edges = []
        
        if not cant_nodes:
            self.nodes = {node: [] for node in nodes} # nodos con adyacencias
            
            for edge in edges:
                self.add_edge(edge.start, edge.end, edge.weight) # si manda lista de edges se carga
        
        else:
            self.nodes = {node: [] for node in range(cant_nodes+1)}
    
    def add_edge(self, node_a, node_b, weight):
        if node_a not in self.nodes:
            self.nodes[node_a] = []
            
        if node_b not in self.nodes:
            self.nodes[node_b] = []
        
        edge_a = Edge(node_a,node_b,weight)
        edge_b = Edge(node_b,node_a,weight)
        
        self.nodes[node_a].append(edge_a)
        self.nodes[node_b].append(edge_b)
        
        self.edges.append(edge_a)
        self.edges.append(edge_b)

    def has_node(self, vertex):
        return vertex in self.nodes

    def min_max_weight_path(self, start: int, goal: int):
        path_data = PathData()
        
        if self.has_node(start) and self.has_node(goal):
            self._process_paths(start, goal, set(), path_data)
        
        return path_data.max_supported

    def _process_paths(self, actual, goal, visited, path_data: 'PathData'):
        if actual == goal:
            if path_data.actual_max < path_data.max_supported:
                path_data.commit_max()
        
        else:
            visited.add(actual)
            
            for ady in self.nodes[actual]:
                if ady.end not in visited:
                    last_max = path_data.actual_max
                    path_data.try_set_max(ady.weight)
                    
                    self._process_paths(ady.end, goal, visited, path_data)
                    
                    path_data.set_max(last_max)
        
            visited.discard(actual)

def build_mst(graph: Graph):
    """
    Esto lo uso para generar un grafo con el arbol de exp minima con las aristas,
    dicho arbol luego me sirve para buscar el mayor peso del menor camino
    """
    ufds = UFDS(len(graph.nodes)) # inicio el ufds

    edges = sorted(graph.edges, key=lambda e: e.weight) # ordeno las aristas
    
    mst = []
    
    for edge in edges: # por cada arista
        if not ufds.same_set(edge.start, edge.end): # si conecta 2 conjuntos diferentes
            ufds.union_set(edge.start, edge.end) # uno los conjuntos
            mst.append(edge) # agrego la arista que une los conjuntos
            
        if len(mst) == len(graph.nodes)-1: # si tengo n-1 aristas ya cumple para ser mst
            break
        
    return Graph(list(graph.nodes.keys()), mst)

def end_condition(C,S,Q):
    return C == 0 and S == 0 and Q == 0

case_num = 1

C, S, Q = tuple([int(data) for data in stdin.readline().strip().split(' ')])

while not end_condition(C,S,Q):
    city = Graph(cant_nodes=C)
    for street in range(S):
        node_a, node_b, weight = tuple([int(data) for data in stdin.readline().strip().split(' ')])
        
        city.add_edge(node_a, node_b, weight)

    city = build_mst(city)
    
    results = []
    
    for query in range(Q):
        node_a, node_b = tuple([int(data) for data in stdin.readline().strip().split(' ')])
        
        min_edge = city.min_max_weight_path(node_a, node_b)
        
        results.append(str(min_edge) if (min_edge < float("inf")) else "no path")
    
    stdout.write("Case #{}\n".format(case_num))
    case_num += 1
    
    stdout.write('\n'.join(results).strip() + '\n')
    
    C, S, Q = tuple([int(data) for data in stdin.readline().strip().split(' ')])
    
    if not end_condition(C,S,Q):
        stdout.write('\n')
