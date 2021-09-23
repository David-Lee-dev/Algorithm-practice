## 노드의 합

```python
T = int(input())

def post(idx, N):
    result = 0
    if idx <= N:
        result = tree[idx] + post(2*idx, N) + post(2*idx + 1, N)
        tree[idx] = result
    return result

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for i in range(M):
        node, value = map(int, input().split())
        tree[node] = value
    post(1, N)

    print("#{} {}".format(tc, tree[L]))


```

---

후위 순회를 이용해서 값을 축적시키면 된다.

1. 후위 순회를 이용해서 가장 레벨이 높은 노드까지 탐색
2. 정해진 트리 범위를 넘어설 경우 0을 반환한다.
3. 재귀 함수가 풀리면서 ``result``에 지금까지 탐색했던 노드들의 합이 계산되고 해당 값이 노드의 값이 된다.
