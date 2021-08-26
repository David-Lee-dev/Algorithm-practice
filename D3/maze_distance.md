## 미로의 거리(#5105)

```python
def navi(row, col):
    check.append((row, col))
    result = 0
    for idx in range(4):
        # 인덱스 범위 내에 있거나, 방문한 적이 없는경우
        if 0 <= row + delta_y[idx] < len(matrix) \
                and 0 <= col + delta_x[idx] < len(matrix) \
                and check[len(check) - 2] != (row + delta_y[idx], col + delta_x[idx]):
            # 길일 경우
            if matrix[row + delta_y[idx]][col + delta_x[idx]] == '0':
                result += navi(row + delta_y[idx], col + delta_x[idx])
                check.pop()
            # 목적지 일경우
            elif int(matrix[row + delta_y[idx]][col + delta_x[idx]]) > 1:
                return len(check)
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [input() for _ in range(N)]
    delta_x = [0, 0, -1, 1]
    delta_y = [-1, 1, 0, 0]
    check = []
    start = 0
    for i in range(N):
        for j in range(N):
            if int(matrix[i][j]) > 1:
                start = (i, j)
                break
        if start:
            break

    result = navi(start[0], start[1])
    if result:
        print("#{} {}".format(tc, result - 1))
    else:
        print("#{} {}".format(tc, result))

```
---
[미로(#4875)](https://github.com/David-Lee-dev/Algorithm-practice/blob/master/D2/maze.md)와 코드는 같다.<br>

1. 2 또는 3을 찾아서 출발점으로 선정. 해당 인덱스부터 탐색 시작
2. 상, 하, 좌, 우 순서로 주변을 탐색하여 **0이거나 방문한 적이 없을 때만** 진행
3. 목적지를 찾을 경우 ``len(check)``을 리턴. 없을 경우 0을 리턴

목적지를 찾았을 때만 지금까지 지나온 길의 수를 반환하면 된다.