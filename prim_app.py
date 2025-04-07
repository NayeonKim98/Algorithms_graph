import heapq

def get_distance(a, b):
    # 맨해튼 거리 계산
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def prim(con_list):
    N = len(con_list)
    visited = [False] * N
    heap = []

    # 시작점은 차단기 (0, 0)
    for i in range(N):
        dist = abs(con_list[i][0]) + abs(con_list[i][1])
        heapq.heappush(heap, (dist, i))

    total_cost = 0
    connected = 0

    while heap and connected < N:
        cost, now = heapq.heappop(heap)

        if visited[now]:
            continue

        visited[now] = True
        total_cost += cost
        connected += 1

        for next in range(N):
            if not visited[next]:
                d = get_distance(con_list[now], con_list[next])
                heapq.heappush(heap, (d, next))

    return total_cost


T = 1
for t in range(1, T+1):
    N = 4
    con_list = [(5, 2), (8, 4), (8, 2), (10, 3)]

    result = prim(con_list)
    print(f"#{t} {result}")

# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     con_list = [tuple(map(int, input().split())) for _ in range(N)]

#     result = prim(con_list)
#     print(f"#{t} {result}")
