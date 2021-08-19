## 괄호검사(#4866)

```python
T = int(input())
for tc in range(1, T + 1):
    string = input()
    stack = []
    for i in range(len(string)):
        # 없는데 닫기 len(stack) != 0
        if not len(stack) and (string[i] == ')' or string[i] == '}'):
            stack += [string[i]]
            break
        # 다른 걸로 닫기 len(stack) != 0
        elif (string[i] == ')' and stack[-1] == '{') or (string[i] == '}' and stack[-1] == '('):
            break
        # 나머지는 정상이므로 그냥 열고 닫으면 됨
        elif string[i] == '(' or string[i] == '{':
            stack += [string[i]]
        elif string[i] == ')' or string[i] == '}':
            stack = stack[:-1]

    if len(stack):
        print("#{} {}".format(tc, 0))
    else:
        print("#{} {}".format(tc, 1))

```

