## 수도 요금 경쟁(#1284)

```python
T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    result = 0

    A_cost = P * W
    B_cost = 0
    if W <= R:
        B_cost = Q
    else:
        B_cost = Q + (W - R)*S

    if A_cost > B_cost:
        result = B_cost
    else:
        result = A_cost

    print("#{} {}".format(test_case, result))

```

