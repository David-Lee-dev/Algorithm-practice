## 격자판의 숫자 이어 붙이기(#2819)

```python
T = int(input())
delta_col = [0, 0, -1, 1]
delta_row = [-1, 1, 0, 0]

def DFS(row, col, string):
    string += matrix[row][col]

    if len(string) == 7:
        result.add(string)
        return

    for i in range(4):
        row += delta_row[i]
        col += delta_col[i]
        if 0 <= row < 4 and 0 <= col < 4:
            DFS(row, col, string)
        row -= delta_row[i]
        col -= delta_col[i]


for tc in range(1, 1 + T):
    matrix = [list(map(str, input().split())) for _ in range(4)]
    result = set()
    for row in range(4):
        for col in range(4):
            DFS(row, col, '')
    print("#{} {}".format(tc ,len(result)))

```

