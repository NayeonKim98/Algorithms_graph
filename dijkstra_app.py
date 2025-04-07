# 📍 최소 배달 시간 - Dijkstra 알고리즘

# 마을 수 N개
# 마을 간 일부 길(간선)만 존재 (부분 연결 가능)
# K번 마을에서 출발

# 모든 마을까지 걸리는 최소 시간을 구하라
# ➡ 최단 시간 경로 (Shortest delivery time)

import heapq

def delivery_time(N, road, K):
    graph = [[] for _ in range(N + 1)]

    for a, b, time in road:
        graph[a].append((b, time))
        graph[b].append((a, time))  # 양방향 도로

    dist = [float('inf')] * (N + 1)
    pq = [(0, K)]  # (시간, 현재 마을)
    dist[K] = 0

    while pq:
        current_time, village = heapq.heappop(pq)

        if dist[village] < current_time:
            continue

        for next_village, travel_time in graph[village]:
            total_time = current_time + travel_time
            
            if total_time < dist[next_village]:
                dist[next_village] = total_time
                heapq.heappush(pq, (total_time, next_village))

    return dist

# 예시 입력
N = 5
road = [
    [1, 2, 1],
    [2, 3, 3],
    [5, 2, 2],
    [1, 4, 2],
    [5, 3, 1],
    [5, 4, 2]
]
K = 1

# 최소 시간 배열 출력
distances = delivery_time(N, road, K)
print(distances[1:])  # [0, 1, 4, 2, 3]

# K 마을에서 각 마을까지 도달 가능한 마을 수 (시간 ≤ 3)
reachable = sum(1 for d in distances if d <= 3)
print("배달 가능한 마을 수:", reachable)  # 출력: 4
