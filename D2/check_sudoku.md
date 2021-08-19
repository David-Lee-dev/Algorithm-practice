## 스도쿠 검증(#1974)

```python
T = int(input())

for test_case in range(1, T + 1):
    answer_sheet = []
    for i in range(9):
        answer_sheet.append(list(map(int, input().split())))

    result = 1

    for row in range(9):
        tmp = 0
        for col in range(9):
            tmp += answer_sheet[row][col]
        if tmp != 45:
            result = 0
            break

    for col in range(9):
        tmp = 0
        for row in range(9):
            tmp += answer_sheet[row][col]
        if tmp != 45:
            result = 0
            break

    if result:
        for row_start_point in range(0, 7, 3):
            for col_start_point in range(0, 7, 3):
                tmp = 0
                for row in range(row_start_point, row_start_point+3):
                    for col in range(col_start_point, col_start_point+3):
                        tmp += answer_sheet[row][col]

                if tmp != 45:
                    result = 0
                    break
            if tmp != 45:
                result = 0
                break

    print("#{} {}".format(test_case, result))

```

