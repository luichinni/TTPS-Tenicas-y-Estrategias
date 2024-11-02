"""
nro servers
s0: conn1 conn2 conn3
s1: ...
"""
from sys import stdin, stdout

def create_graph(cant_nodos, orden):
    grafo = [[] for _ in range(cant_nodos)]
    
    if cant_nodos > 0:
        for I in range(cant_nodos):
            data = stdin.readline().split(' ')
            
            node = int(data[0])
            
            orden.append(node)
            
            if len(data) > 2:
                grafo[node] = [int(ady) for ady in data[2:]]
                
    return grafo

def get_critical_links(v, graph, fathers, lowest_reachable, visited, n_discovered):
    global counter
    
    critical_returns = []
    
    visited[v] = True
    
    n_discovered[v] = counter
    counter += 1
    
    lowest_reachable[v] = n_discovered[v]
    
    for W in graph[v]:
        if not visited[W]:
            fathers[W] = v
            
            for critical_link in get_critical_links(W, graph, fathers, lowest_reachable, visited, n_discovered):
                critical_returns.append(critical_link)
            
            if lowest_reachable[W] > n_discovered[v]:
                # puente critico                
                critical_returns.append((min(W,v),max(W,v)))
        
            lowest_reachable[v] = min(lowest_reachable[v],lowest_reachable[W])
        
        elif not (fathers[v] == W):
            lowest_reachable[v] = min(lowest_reachable[v],n_discovered[W])
            
    return critical_returns

counter = 1

for linea in stdin:
    counter = 1
    
    if (linea.strip() == ''):
        continue
    
    conexiones = int(linea)
    
    orden = []

    grafo = create_graph(conexiones, orden)
    
    padres = [-1] * conexiones
    menor_alcanzable = [conexiones] * conexiones
    visited = [False] * conexiones
    n_discovered = [-1] * conexiones
    
    criticos = []
    
    for v in orden:
        if not visited[v]:
            for critical in get_critical_links(v,grafo,padres,menor_alcanzable,visited,n_discovered):
                criticos.append(critical)
    
    stdout.write("{} critical links\n".format(len(criticos)))
    
    criticos = sorted(criticos, key=lambda par: (par[0], par[1]))
    
    for critico in criticos:
        stdout.write("{} - {}\n".format(critico[0],critico[1]))
    
    stdout.write("\n")
    