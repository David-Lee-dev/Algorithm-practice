## 숫자를 정렬하자(#1966)

```python
T = int(input())
for test_case in range(1, T + 1):
    number = list(map(int, input().split()))
    number.sort()

    print("#{}".format(test_case), end=" ")
    print(*number)

```

