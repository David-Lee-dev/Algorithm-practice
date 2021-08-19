## Flatten(#1208)

```python
def max_min_idx(numbers, index=True):
    max_result = numbers[0]
    min_result = numbers[0]
    result = [0, 0]
    for idx in range(1, len(numbers)):
        if max_result < numbers[idx]:
            max_result = numbers[idx]
            result[0] = idx
        if min_result > numbers[idx]:
            min_result = numbers[idx]
            result[1] = idx

    if index:
        return (result[0], result[1])
    else:
        return (max_result, min_result)


T = 10
for test_case in range(1, T + 1):
    N = int(input())  # 덤프 횟수
    boxs = list(map(int, input().split()))

    # 카운트 정렬g
    # count = [0] * 100
    # for idx in range(100):
    #     count[boxs[idx]-1] += 1
    #
    # for idx in range(1,100):
    #     count[idx] = count[idx] + count[idx-1]
    #
    # temp = [0]*100
    # for idx in range(99, -1, -1):
    #     count[boxs[idx]-1] -= 1
    #     temp[count[boxs[idx]-1]] = boxs[idx]

    for idx in range(N):
        max_box, min_box = max_min_idx(boxs)
        boxs[max_box] -= 1
        boxs[min_box] += 1

    result = max_min_idx(boxs, False)

    print("#{} {}".format(test_case, (result[0] - result[1])))

```

