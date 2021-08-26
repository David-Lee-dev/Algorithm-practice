## 미로1(#1226)

```python
SIZE = 16

def search(row, col):
    maze[row][col] = 1
    for i in range(4):
        if 0 <= row+delta[i][0] < SIZE and 0 <= col+delta[i][1] < SIZE: # 인덱스가 범위 안에 있고
            if maze[row+delta[i][0]][col+delta[i][1]] % 3 == 0: # 길이거나 도착지
                maze[row + delta[i][0]][col + delta[i][1]] = 1
                search(row + delta[i][0], col + delta[i][1])
    return

for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(SIZE)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    point = []
    # 출발지, 목적지 탐색 point = [start_row, start_col, end_row, end_col]
    for i in range(SIZE):
        for j in range(SIZE):
            if maze[i][j] > 1:
                point.append(i)
                point.append(j)
                break

    search(point[0], point[1])
    if maze[point[2]][point[3]] == 3: # 도착지가 3이면 도달하지 못 했음
        print("#{} 0".format(tc))
    else:
        print("#{} 1".format(tc))
```

---

1. 인덱스가 범위 내에 있고 길이면 0을 1로 바꾼다.
2. 도착지가 3이면 도달하지 못했음.
