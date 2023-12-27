import heapq
import time


class Graph:
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.edges = [[] for _ in range(num_vertices)]
        self.visited = [False] * num_vertices

    def add_edge(self, u, v, w):
        self.edges[u].append((v, w))
        self.edges[v].append((u, w))


def build_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        num_vertices = int(file.readline().strip())
        graph = Graph(num_vertices)
        for line in file:
            u, v, w = map(float, line.strip().split())
            graph.add_edge(int(u) - 1, int(v) - 1, w)
    return graph


# Tarefa A: Calcular a Distância e o Caminho Mínimo entre Vértices Específicos
def dijkstra(graph, start):
    distances = [float('inf')] * graph.v
    previous = [None] * graph.v
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if graph.visited[current_vertex]:
            continue

        graph.visited[current_vertex] = True

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous


def reconstruct_path(previous, start, end):
    path = []
    while end != start:
        path.append(end)
        end = previous[end]
    path.append(start)
    return path[::-1]


def task_a(graph, start, targets):
    start_time = time.time()
    distances, previous = dijkstra(graph, start)
    results = {}
    for target in targets:
        path = reconstruct_path(previous, start, target)
        results[target] = (distances[target], path)
    end_time = time.time()
    return results, end_time - start_time


# Tarefa B: Obter uma Árvore Geradora Mínima
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            elif self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1


def kruskal(graph):
    edges = []
    for u in range(graph.v):
        for v, w in graph.edges[u]:
            edges.append((w, u, v))
    edges.sort()

    ds = DisjointSet(graph.v)
    mst = []
    total_weight = 0

    for w, u, v in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


def task_b(graph):
    start_time = time.time()
    mst, total_weight = kruskal(graph)
    end_time = time.time()
    return mst, total_weight, end_time - start_time


# Tarefa C: Calcular a Excentricidade de Vértices Específicos
def calculate_eccentricity(graph, vertex):
    distances, _ = dijkstra(graph, vertex)
    return max(distances)


def task_c(graph, vertices):
    start_time = time.time()
    eccentricities = {}
    for vertex in vertices:
        eccentricity = calculate_eccentricity(graph, vertex)
        eccentricities[vertex] = eccentricity
    end_time = time.time()
    return eccentricities, end_time - start_time


# MAIN
file_path = ['grafo_W_1.txt','grafo_W_2.txt','grafo_W_3.txt']
for file_path in file_path:
    graph = build_graph_from_file(file_path)

    # Vértices especificados para as tarefas
    specified_vertices = [9, 19, 29, 39, 49]  # Ajustando para índices base 0

    # Executando as tarefas
    a_results = task_a(graph, 0, specified_vertices)
    b_results = task_b(graph)
    c_results = task_c(graph, specified_vertices)

    # Exibindo os resultados
    print("Resultados da Tarefa A:", a_results)
    print("Resultados da Tarefa B:", b_results)
    print("Resultados da Tarefa C:", c_results)
