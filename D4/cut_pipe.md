## 쇠막대기 자르기(#5432)

```python
T = int(input())

for test_cass in range(1, T+1):
    pip = input()
    stack = []
    laser = False

    result = 0
    for idx in range(len(pip)):
        if pip[idx] == '(':
            if not laser:
                laser = not laser
            else:
                stack += [pip[idx]]
        else:
            if laser:
                result += len(stack)
                laser = not laser
            else:
                stack = stack[:-1]
                result += 1

    print("#{} {}".format(test_cass, result))

```

