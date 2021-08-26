## 지그재그 숫자(#1986)

```python
def BPS(s, g):
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        for i in range(len(edges[t])):
            if visited[edges[t][i]] == 0:
                queue.append(edges[t][i])
                visited[edges[t][i]] = visited[t] + 1

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V + 1)]
    for i in range(1, E + 1):
        s, d = map(int, input().split())
        edges[s] += [d]
        edges[d] += [s]
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    queue = []

    BPS(S, G)
    if visited[G]:
        print("#{} {}".format(tc, visited[G]-1))
    else:
        print("#{} {}".format(tc, 0))

```
---
너비우선탐색 이용

1. 큐가 빌 때까지(탐색이 모두 끝날 때까지) 반복 진행
2. 처음 방문한 노드일 경우 ``이전 노드의 값 + 1``하여 ``visited``리스트에 값 할당
3. 목적지의 ``visited``값이 0이 아닐 경우 정답. 아닐 경우 0

이전 노드의 값에 1을 더하는 방법으로 노드끼리 루프를 이루었을 때에도 정확한 거리 값을 측정할 수 있다.

