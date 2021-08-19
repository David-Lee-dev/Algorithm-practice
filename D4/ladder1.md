## ladder1(#1210)

```python
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    move_row = [0, -1, 0]
    move_col = [-1, 0, 1]
    di_move = 1

    now_row = 99
    now_col = 0
    for col in range(100):
        if ladder[99][col] == 2:
            now_col = col

    while now_row > 0:
        now_row += move_row[di_move]
        now_col += move_col[di_move]

        if di_move == 0:
            if now_col - 1 < 0 or ladder[now_row][now_col - 1] == 0:
                di_move = 1
        elif di_move == 2:
            if now_col + 1 >= 100 or ladder[now_row][now_col + 1] == 0:
                di_move = 1
        elif now_col - 1 >= 0 and ladder[now_row][now_col - 1] == 1:
            di_move = 0
        elif now_col + 1 < 100 and ladder[now_row][now_col + 1] == 1:
            di_move = 2

    print("#{} {}".format(test_case, now_col))

```

