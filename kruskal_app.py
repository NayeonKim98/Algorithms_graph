# 🔗 도시 전력망 나누기 - Kruskal 알고리즘 풀이

# 간선들을 가중치 기준으로 정렬
# 가장 비싼 간선을 제외한 나머지로 MST 구성
# 결과적으로 두 개의 전력망으로 분리됨

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def divide_electricity(n, edges):
    parent = list(range(n + 1))  # 도시 번호가 1부터 시작한다고 가정
    edges.sort(key=lambda x: x[2])  # 비용 기준 정렬

    total_cost = 0
    max_edge_cost = 0

    for a, b, cost in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
            max_edge_cost = cost  # 마지막에 연결된 가장 큰 간선

    return total_cost - max_edge_cost

n = 7
edges = [
    (1, 2, 3),
    (2, 3, 2),
    (3, 4, 5),
    (4, 5, 1),
    (5, 6, 2),
    (6, 7, 7),
    (1, 7, 8)
]
print(divide_electricity(n, edges))  # ✅ 출력: 17
