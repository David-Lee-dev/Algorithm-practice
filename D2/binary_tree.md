## 이진탐색

```python
T = int(input())

def inorder(node, N):
    global cnt
    if node <= N:
        inorder(2*node, N)
        cnt += 1
        tree[node] = cnt
        inorder(2*node + 1, N)

for tc in range(1, 1 + T):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 0

    inorder(1, N)
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))
```

---

중위 우선 탐색을 이용하고, 노드의 값을 ``count``값을 하나씩 증가시키면서 대입하면 된다.
