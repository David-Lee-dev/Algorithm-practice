## 간단한 소인수분해(#1945)

```python
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    numbers = [2, 3, 5, 7, 11]
    result = []

    for number in numbers:
        count = 0
        while (N % number) == 0:
            N //= number
            count += 1
        result.append(count)

    print("#{}".format(test_case), end=" ")
    print(*result)

```

