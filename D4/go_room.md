## 자기 방으로 들어가기(#1219)

```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * 401

    min_move = 0
    for i in range(len(rooms)):
        s = rooms[i][0] - ((rooms[i][0] + 1) % 2)
        e = rooms[i][1] + (rooms[i][1] % 2)
        if e < s:
            s, e = e, s

        for j in range(s, e + 1):
            check[j] += 1
            if min_move < check[j]:
                min_move = check[j]

    print("#{} {}".format(tc, min_move))

```

