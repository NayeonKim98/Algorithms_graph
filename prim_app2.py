# 문제 요약 
# **여러 개의 섬**이 존재하고,

# 각 섬은 **다리**로 연결 가능하며,

# 다리마다 **비용**이 존재
# ➡ 모든 섬을 **사이클 없이 최소 비용**으로 연결해야 한다.
# MST 문제이며, 연결 그래프 + 최소 비용 조건 → Prim 알고리즘 적합

import heapq

def connect_islands(n, costs):
    graph = [[] for _ in range(n)]
    
    for a, b, cost in costs:
        graph[a].append((b, cost))
        graph[b].append((a, cost))  # 양방향 연결

    visited = [False] * n
    min_heap = [(0, 0)]  # (비용, 시작섬)
    total_cost = 0

    while min_heap:
        cost, island = heapq.heappop(min_heap)

        if visited[island]:
            continue

        visited[island] = True
        total_cost += cost

        for next_island, next_cost in graph[island]:
            if not visited[next_island]:
                heapq.heappush(min_heap, (next_cost, next_island))

    return total_cost


n = 4
costs = [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 1],
    [2, 3, 8]
]
print(connect_islands(n, costs))  # ✅ 출력: 4
