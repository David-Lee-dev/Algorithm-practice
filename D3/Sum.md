## Sum(#1208)

```python
import sys
sys.stdin = open('input.txt')

T = 10


def summury(arr, row, row_movement, col, col_movement):
    result = 0
    for idx in range(len(arr)):
        result += arr[row][col]
        row += row_movement
        col += col_movement

    return result


for test_case in range(1, T + 1):
    trash = int(input())
    N = 100

    arr = [list(map(int, input().split())) for _ in range(N)]

    row_col_cross_sum = []

    for idx in range(N):
        row_col_cross_sum += [summury(arr, idx, 0, 0, 1)]    # 행 합
        row_col_cross_sum += [summury(arr, 0, 1, idx, 0)]    # 열 합

    row_col_cross_sum += [summury(arr, 0, 1, 0, 1)]
    row_col_cross_sum += [summury(arr, 0, 1, N-1, -1)]

    # 선택 정렬
    for i in range(len(row_col_cross_sum)-1):
        for j in range(i+1, len(row_col_cross_sum)):
            if row_col_cross_sum[i] > row_col_cross_sum[j]:
                row_col_cross_sum[i], row_col_cross_sum[j] = row_col_cross_sum[j], row_col_cross_sum[i]

    print("#{} {}".format(test_case, row_col_cross_sum[-1]))

```

