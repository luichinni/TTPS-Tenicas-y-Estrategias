import heapq
import math
from sys import stdin, stdout

class minHeap:
    def __init__(self):
        self._heap = []

    def push(self, value):
        heapq.heappush(self._heap, value)

    def pop(self):
        return heapq.heappop(self._heap)

    def empty(self):
        return len(self._heap) == 0

class Connection:
    def __init__(self, s1, s2, latency):
        """
        Connection = Edge = Arista
        """
        self.s1 = s1
        self.s2 = s2
        self.latency = latency


class Network:
    def __init__(self, servers):
        """
        Network = Graph = Grafo
        """
        self.servers = [server for server in range(servers)]
        self.connections = [[] for _ in range(servers)]
    
    def connect(self, s1, s2, latency):
        self.connections[s1].append(Connection(s1,s2,latency))
        self.connections[s2].append(Connection(s2,s1,latency))

    def min_latency_between(self, s1, s2):
        """
        Dijkstra Ok para estos casos
        """

        distancias = [math.inf] * len(self.servers)
        distancias[s1] = 0

        cola_p = minHeap()

        cola_p.push((distancias[s1], s1))

        while not cola_p.empty():
            lat, sv = cola_p.pop()

            if lat > distancias[sv]:
                # si la dist es mayor la ignoro
                continue

            for ady in self.connections[sv]:
                # latencia entre actual y adyacente
                latencia = lat + ady.latency

                if latencia < distancias[ady.s2]:
                    # actualizo la latencia si es menor y lo encolo nuevamente
                    distancias[ady.s2] = latencia
                    cola_p.push((latencia, ady.s2))
        
        return distancias[s2] if distancias[s2] != math.inf else 'unreachable'# retorno la dist minima
    

casos = int(stdin.readline())

rta = []

for case in range(casos):
    servers, connections, S, T = tuple([int(data) for data in stdin.readline().strip().split(' ')])

    net = Network(servers)

    for _ in range(connections):
        s1, s2, latency = tuple([int(data) for data in stdin.readline().strip().split(' ')])
        net.connect(s1, s2, latency)

    rta.append("Case #{}: {}".format(case + 1, net.min_latency_between(S, T)))

stdout.write("\n".join(rta) + "\n")
