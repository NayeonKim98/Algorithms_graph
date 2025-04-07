import heapq

def dijkstra(graph, start):
    distance = [float('inf')] * len(graph)
    distance[start] = 0
    pq = [(0, start)]  # (distance, vertex)

    while pq:
        dist, u = heapq.heappop(pq)

        if distance[u] < dist:
            continue
        
        for v, w in graph[u]:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                heapq.heappush(pq, (distance[v], v))
    
    return distance

# 인접 리스트 방식
graph = {
    0: [(1, 2), (2, 5)],
    1: [(0, 2), (2, 1), (3, 3)],
    2: [(0, 5), (1, 1), (3, 2)],
    3: [(1, 3), (2, 2)]
}
