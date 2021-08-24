## 지그재그 숫자(#4874)

```python
def cal(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a // b

T = int(input())
for tc in range(1, T + 1):
    string = list(map(str, input().split()))
    stack = []
    i = 0

    while string[i] != '.':
        if string[i] not in '/*-+':
            stack.append(string[i])
        else:
            if len(stack) > 1:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(cal(a, b, string[i]))
            else:
                break
        i += 1

    if len(stack) == 1 and i == len(string) - 1:
        print("#{} {}".format(tc, stack[0]))
    else:
        print("#{} {}".format(tc, 'error'))
```

---

입력 받은 후위 계산식을 풀면 되는 문제.

1. 숫자는 stack에 push
2. 연산자는 숫자 두 개를 꺼내서 연산한 뒤 stack에 push
3. stack의 길이가 1이고**(숫자 하나만 들어있고)**, 인덱스가 ``string-1``과 같으면**(계산식이 올바르면)** 출력

문제에서 나눗셈은 항상 나누어 떨어진다고 하여 항상 나누어 떨어지는 숫자가 주어지는 줄 알았지만, ``//``연산자를 이용해야 한다는 뜻이었다.
