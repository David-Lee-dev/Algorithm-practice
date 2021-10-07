## 동철이의 일 분배(#1865)

```python
T = int(input())

def BT(no, summary):
    global result

    if summary <= result:
        return

    if 0 not in visited:
        if summary > result:
            result = summary
        return

    for idx in range(len(percentage)):
        if visited[idx] == 0 and percentage[no][idx] != 0:
            visited[idx] = 1
            BT(no + 1, summary * percentage[no][idx] / 100)
            visited[idx] = 0

for tc in range(1, 1 + T):
    N = int(input())
    percentage = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    BT(0, 1)
    print("#{} {:.6f}".format(tc, result * 100))
```

---

