## 두개의 숫자열(#1959)

```python
import copy

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, (input().split()))
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        Ai, Bj = Bj, Ai

    result = 0

    for m in range(0, M-N+1):
        num = 0
        for n in range(N):
            num += Ai[n] * Bj[n+m]

        if result < num:
            result = num

    print("#{} {}".format(test_case, result))

```

