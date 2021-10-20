## 최소 신장 트리(#5249)

```python
def make(N):
    for i in range(N):
        parents[i] = i

def find(el):
    if el == parents[el]:
        return el
    parents[el] = find(parents[el])
    return parents[el]

def union(a, b):
    aRoot = find(a)
    bRoot = find(b)
    if aRoot == bRoot:
        return False

    parents[bRoot] = aRoot

    return True

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])

    parents = [0] * (V + 1)
    make(V + 1)

    result = 0
    cnt = 0
    for edge in edges:
        if(union(edge[0], edge[1])):
            result += edge[2]
            cnt += 1
            if cnt == V + 1:
                break

    print("#{} {}".format(tc, result))

```

