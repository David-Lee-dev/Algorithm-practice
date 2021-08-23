## 계산기2(#1223)

```python
def cal(a, b, c):
    if c == '+':
        return a + b
    return a * b

for tc in range(1, 11):
    N = int(input())
    string = input()

    stack_cal = []
    stack_result = []
    for i in range(N):
        if string[i] in '1234567890':
            stack_result += [string[i]]
        else:
            if stack_cal:
                if string[i] == '+':
                    while stack_cal:
                        stack_result += [stack_cal.pop()]
                    stack_cal += [string[i]]
                else:
                    while stack_cal[-1] == '*':
                        stack_result += [stack_cal.pop()]
                        if not stack_cal:
                            break
                    stack_cal += [string[i]]

            else:
                stack_cal += [string[i]]
    for i in range(len(stack_cal)):
        stack_result += [stack_cal.pop()]

    for i in range(len(stack_result)):
        if stack_result[i] in '1234567890':
            stack_cal += [stack_result[i]]
        else:
            b = int(stack_cal.pop())
            a = int(stack_cal.pop())
            stack_cal += [str(cal(a, b, stack_result[i]))]

    print("#{} {}".format(tc, stack_cal[-1]))
```

---

중위계산식을 후위계산식으로 바꿔서 계산해야 한다.

#### 후위계산식 변경 과정

제약 사항 : 계산 기호는 ``+``,``*`` 뿐이다. 숫자는 0 - 9만 있다.

1. 숫자는 기본적으로 push
2. ``+``는 계산식 스택이 빌 때까지 pop 하여 숫자가 담긴 스택에 push한 뒤에, 마지막으로 push
3. ``*``는 ``+``가 나올 때까지 계산식 스택에서 pop하고, push
4. 계산식 스택이 비어 있으면 무조건 push

#### 계산 과정

1. 0번 인덱스부터 계산식까지 탐색. 숫자는 모두 스택에 push
2. 계산식이 나오면 스택에서 두 개를 pop하여 계산한 뒤 다시 push
3. 마지막으로 남은 숫자 하나가 정답

---

숫자가 10 이상 나온다면 코드 수정이 필요하다. 당장 떠오르는 방법은 후위계산식을 만드는 과정에서 계산식이 나올 때까지 다른 변수에 저장해두었다가 한 번에 push 해주는 방법이다.

```python
tmp = ''
if string[i] in '1234567890':
	tmp += string[i]
else:
	stack += [tmp]
    # 이하 생략
```

이런 식으로 진행할 것 같다.

괄호가 포함되고 계산식도 모두 사용하면 좀 더 조건이 많아질텐데 큰 변화는 없을 것 같다.

