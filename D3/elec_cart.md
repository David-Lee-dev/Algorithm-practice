## 전자카트(#5189)

```python
T = int(input())

def max_val(N):
    result = 0
    for i in range(N):
        for j in range(N):
            result += matrix[i][j]
    return result

def search(now, summary):
    global result
    if len(visited) == len(matrix):
        summary += matrix[now][0]
        if result > summary:
            result = summary
        return
    for nxt in range(len(matrix)):
        if nxt not in visited and nxt != now:
            summary += matrix[now][nxt]
            visited.append(nxt)
            search(nxt, summary)
            visited.pop()
            summary -= matrix[now][nxt]

for tc in range(1, 1+ T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = max_val(N)

    visited = [0, ]
    search(0, 0)
    print("#{} {}".format(tc, result))
```

