## 구간합

```python
def summury(numbers, idx):
    result = 0
    for idx_sum in range(M):
        result += numbers[idx + idx_sum]

    return result


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    max_sum = min_sum = summury(numbers, 0)

    for idx in range(1, len(numbers)-M+1):
        sum_puls = summury(numbers, idx)
        # for idx_sum in range(M):
        #     summury += numbers[idx + idx_sum]

        if max_sum < sum_puls:
            max_sum = sum_puls
        if min_sum > sum_puls:
            min_sum = sum_puls

    print("#{} {}".format(test_case, max_sum - min_sum))

```

