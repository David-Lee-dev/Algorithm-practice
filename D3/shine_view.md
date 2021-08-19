## View(#1206)

```python
for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0

    for i in range(2, N - 2):
        shine_floor = 0
        # 왼쪽
        left_side_1 = buildings[i] - buildings[i-1]
        left_side_2 = buildings[i] - buildings[i-2]
        if left_side_1 < 0 or left_side_2 < 0:
            continue
        left_side_result = left_side_2 if left_side_2 < left_side_1 else left_side_1

        # 오른쪽
        right_side_1 = buildings[i] - buildings[i+1]
        right_side_2 = buildings[i] - buildings[i+2]
        if right_side_1 < 0 or right_side_2 < 0:
            continue
        right_side_result = right_side_2 if right_side_2 < right_side_1 else right_side_1

        shine_floor = right_side_result if right_side_result < left_side_result else left_side_result
        result += shine_floor
    print("#{} {}".format(test_case, result))

```

