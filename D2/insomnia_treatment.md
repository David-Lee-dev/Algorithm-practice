## 새로운 불면증 치료법(#1288)

```python
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = []
    count = 0
    n = 1
    while len(result) != 10:
        tmp = N * n
        count = tmp
        while tmp > 0:
            if (tmp % 10) not in result:
                result += [tmp % 10]
            tmp //= 10
        n += 1

    print("#{} {}".format(test_case, count))

```

