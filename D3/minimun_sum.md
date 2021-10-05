## 최소합(#5188)

```python
T = int(input())

def search(row, col, summary):
    global result

    # 끝에 다다르기 전 최솟값을 넘어가면 패스
    if summary > result:
        return

    summary += matrix[row][col]
    # 최솟값 갱신
    if row == len(matrix) - 1 and col == len(matrix) - 1:
        if result > summary:
            result = summary
            return

    # 이동
    if row < len(matrix) - 1:
        search(row + 1, col, summary)
    if col < len(matrix) - 1:
        search(row, col + 1, summary)


for tc in range(1, 1 + T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 9999

    search(0, 0, 0)
    print("#{} {}".format(tc, result))
```

