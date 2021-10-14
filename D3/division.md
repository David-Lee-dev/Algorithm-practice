## 그룹나누기(#5248)

```python
T = int(input())

def team(i):
    if visited[i] == 1:
        return
    member = [i]
    queue = [i]
    while queue:
        cur = queue.pop(0)
        if visited[cur] == 0:
            visited[cur] = 1
            for j in range(1, len(matrix[cur])):
                if visited[j] == 0 and matrix[cur][j] == 1:
                    queue.append(j)
                    member.append(j)

    return member

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    pairs = list(map(int, input().split()))
    result = []
    visited = [0] * (N + 1)
    for idx in range(0, len(pairs), 2):
        matrix[pairs[idx]][pairs[idx + 1]] = 1
        matrix[pairs[idx + 1]][pairs[idx]] = 1

    for i in range(1, N + 1):
        tmp = team(i)
        if tmp != None:
            result.append(tmp)

    print("#{} {}".format(tc, len(result)))
```

