def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def kruskal(n, edges):
    parent = list(range(n))
    edges.sort(key=lambda x: x[2])  # weight 기준 정렬
    total_cost = 0

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            total_cost += weight

    return total_cost

edges = [
    (0, 1, 3), (1, 2, 1), (2, 3, 2),
    (0, 3, 5), (1, 3, 4)
]
