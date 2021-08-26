## 회전(#5097)

```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for i in range(M):
        tmp = numbers[0]
        numbers = numbers[1:]
        numbers.append(tmp)

    print("#{} {}".format(tc,numbers[0]))
```

