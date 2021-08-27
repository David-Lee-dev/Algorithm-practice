## Magnetic(#1220)

```python
def check(row, col):
    for idx in range(row + 1, N):
        if matrix[idx][col] == 1:
            return 0
        elif matrix[idx][col] == 2:
            return 1
    return 0

for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += check(i, j)

    print("#{} {}".format(tc,cnt))
```
---
1. N극(1)과 S극(2) 중에서 하나만 골라 체크하면 된다.
2. N극 자성체가 있는 부분에서 아래로 내려가며 ``1``과 ``2``를 탐색
3. 함수 작동 방식<br>
    - ``1``에서는 0 반환(같은 자성체이므로 합쳐진다고 가정)
    - ``2``에서는 1 반환
    - 반복문이 끝나면 0 반환