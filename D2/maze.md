## 지그재그 숫자(#4875)

```python
def navi(row, col):
    check.append((row, col))
    result = 0
    for idx in range(4):
        if 0 <= row + delta_y[idx] < len(matrix) \
                and 0 <= col + delta_x[idx] < len(matrix) \
                and check[len(check) - 2] != (row + delta_y[idx], col + delta_x[idx]):

            if matrix[row + delta_y[idx]][col + delta_x[idx]] == '0':
                result += navi(row + delta_y[idx], col + delta_x[idx])
                check.pop()
            elif int(matrix[row + delta_y[idx]][col + delta_x[idx]]) > 1:
                return 1
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

    print("#{} {}".format(tc, navi(start[0], start[1])))
```

---

깊이우선탐색을 이용하는 문제.



1. 2 또는 3을 찾아서 출발점으로 선정. 해당 인덱스부터 탐색 시작
2. 상, 하, 좌, 우 순서로 주변을 탐색하여 **0이거나 방문한 적이 없을 때만** 진행
3. 목적지를 찾을 경우 1을 리턴. 없을 경우 0을 리턴



스택 연습을 하기 위해서 이차원 배열이 아닌 스택을 이용해서 체크를 했다. 처음에 인덱스 범위만 검사하는 조건문에 ``elif``문을 붙여서 목적지 체크를 했더니 인덱스 오류가 났다. 애초에 인덱스 범위를 벗어났는데 목적지 여부를 확인하니 생긴 오류였다.
