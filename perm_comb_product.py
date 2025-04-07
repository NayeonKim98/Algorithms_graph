def perm(arr, r):
    result = []
    used = [False] * len(arr)

    def backtrack(path):
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(len(arr)):
            if not used[i]:
                used[i] = True
                path.append(arr[i])
                backtrack(path)
                path.pop()
                used[i] = False

    backtrack([])
    return result

# 예시
print(perm([1, 2, 3], 2))

def comb(arr, r):
    result = []

    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

# 예시
print(comb([1, 2, 3], 2))

def product(arr, r):
    result = []

    def backtrack(path):
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(len(arr)):
            path.append(arr[i])
            backtrack(path)
            path.pop()

    backtrack([])
    return result

# 예시
print(product([1, 2], 2))
