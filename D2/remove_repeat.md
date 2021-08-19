## 반복문자 지우기(#4873)

```python
T = int(input())
for tc in range(1, T + 1):
    N = list(input())
    stack = N[0]
    for i in range(1, len(N)):
        if stack:
            if stack[-1] == N[i]:
                stack = stack[:-1]
            else:
                stack += N[i]
        else:
            stack += N[i]

    print("#{} {}".format(tc, len(stack)))

```

