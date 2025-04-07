import heapq

def prim(graph, start):
    visited = [False] * len(graph)
    min_heap = [(0, start)]  # (weight, vertex)
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue
        
        visited[u] = True
        total_cost += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return total_cost

# 인접 리스트 형식
graph = {
    0: [(1, 3), (3, 5)],
    1: [(0, 3), (2, 1), (3, 4)],
    2: [(1, 1), (3, 2)],
    3: [(0, 5), (1, 4), (2, 2)]
}