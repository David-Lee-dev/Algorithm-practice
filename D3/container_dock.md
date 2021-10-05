## 화물 도크(#5202)

```python
T = int(input())

def sorting():
    for i in range(len(time_slot)-1, -1, -1):
        for j in range(i):
            if time_slot[j][1] > time_slot[j + 1][1]:
                time_slot[j], time_slot[j + 1] = time_slot[j + 1], time_slot[j]
    return

for tc in range(1, 1 + T):
    N = int(input())
    time_slot = []
    matrix = [[0] * 24 for _ in range(N)]

    for i in range(N):
        start, end = map(int, input().split())
        time_slot.append((start, end))
    sorting()
    cnt = 0
    end = 0
    while time_slot:
        s, e = time_slot.pop(0)
        if end <= s:
            cnt += 1
            end = e

    print("#{} {}".format(tc, cnt))
```

