## 종이붙이기(#4869)

```python
def floor(n):
    global stack
    if n == 1:
        return 1
    elif n == 2:
        return 3
    if n >= len(stack):
        stack += [floor(n-1) + (2 * floor(n-2))]
    return stack[n-1]


T = int(input())
for tc in range(1, T + 1):
    stack = [1, 3]
    N = int(input()) // 10
    floor(N)
    print("#{} {}".format(tc, stack[-1]))

```

