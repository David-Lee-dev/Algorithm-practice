## 의석이의 세로로 말해요(#5356)

```python
T = int(input())
for test_case in range(1, T + 1):
    N = [input() for _ in range(5)]
    result = ''

    max_len = len(N[0])
    for idx in range(1, len(N)):
        if max_len < len(N[idx]):
            max_len = len(N[idx])

    for col in range(max_len):
        for row in range(5):
            if len(N[row]) > col:
                result += N[row][col]
    print("#{} {}".format(test_case, result))

```

