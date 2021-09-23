## 사칙연산(#1232)

```python
def summary(idx):
    if len(tree[idx]) == 1:
        return int(tree[idx][0])
    else:
        if tree[idx][0] == '-':
            return summary(int(tree[idx][1])) - summary(int(tree[idx][2]))
        elif tree[idx][0] == '+':
            return summary(int(tree[idx][1])) + summary(int(tree[idx][2]))
        elif tree[idx][0] == '*':
            return summary(int(tree[idx][1])) * summary(int(tree[idx][2]))
        else:
            return summary(int(tree[idx][1])) // summary(int(tree[idx][2]))

for tc in range(10):
    N = int(input())
    tree = dict()
    for i in range(N):
        nodes = list(map(str, input().split()))
        tree[int(nodes[0])] = nodes[1:]
    print("#{} {}".format(tc+1, summary(1)))

```

---

