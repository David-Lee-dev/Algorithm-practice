## 특별한 정렬(#4843)

```python
def sorting(arr):
    for i in range(len(arr) + 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return None


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    sorting(numbers)

    result = [0] * 10
    index = 0

    for idx in range(10):
        index += ((-1)**(idx)*(len(numbers) - idx))
        result[idx] = numbers[index - 1]

    print("#{}".format(test_case), end=" ")
    print(*result)

```

