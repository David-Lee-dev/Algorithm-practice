## 정사각형 방(#1861)

```python
T = int(input())
delta_col = [0, 0, -1, 1]
delta_row = [-1, 1, 0, 0]

for tc in range(1, 1 + T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    numbers = [0] * N**2
    numbers.append(0)
    for row in range(N):
        for col in range(N):
            for i in range(4):
                tmp_row = row + delta_row[i]
                tmp_col = col + delta_col[i]
                if 0 <= tmp_row < N and 0 <= tmp_col < N:
                    if matrix[row][col] + 1 == matrix[tmp_row][tmp_col]:
                        numbers[matrix[row][col]] = 1

    i = len(numbers) - 1
    result = [0, 0]
    while i > 0:
        count = 0
        if numbers[i] == 1:
            while numbers[i] == 1:
                count += 1
                i -= 1
            if result[1] <= count:
                result[0] = i + 1
                result[1] = count
        else:
            i -= 1

    print("#{} {} {}".format(tc, result[0], result[1] + 1))

```

---

1. 가장 높은 지역을 출발지로 설정

2. 범위 내에 있을 경우

   a. 너 낮은 지역일 경우 방문

   b. 낮지 않을 경우 깎아서 방문

DFS를 이용한 문제. ``stack.pop()``을 통해서 방문 스택을 한 번만 조정했어야 했는데 a 분기 b 분기에서 모두 해서 계속 틀렸다.
