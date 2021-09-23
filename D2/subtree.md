## subtree

```python
def inorder(node):
    global count
    if node:
        inorder(tree[0][node])
        count += 1
        inorder(tree[1][node])

T = int(input())
for tc in range(1, 1 + T):
    E, N = map(int, input().split())
    numbers = list(map(int, input().split()))
    tree = [[0] * (E + 2) for _ in range(2)]
    count = 0

    for idx in range(0, len(numbers), 2):
        parent = numbers[idx]
        child = numbers[idx + 1]
        for i in range(2):
            if tree[i][parent] == 0:
                tree[i][parent] = child
                break

    inorder(N)
    print("#{} {}".format(tc, count))
```

