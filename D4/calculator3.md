## 길찾기(#1219)

```python
for tc in range(1, 11):
    N = int(input())
    string = input()

    postfix = []
    cal = []

    for i in range(len(string)):
        if string[i] == '(':
            cal.append(string[i])
        elif string[i] in '0123456789':
            postfix.append(string[i])
        elif string[i] in '/*-+':
            if cal:
                if string[i] in '/*':
                    while cal[-1] not in '+-(':
                        postfix.append(cal.pop())
                        if not cal:
                            break
                    cal.append(string[i])
                else:
                    while cal[-1] != '(':
                        postfix.append(cal.pop())
                        if not cal:
                            break
                    cal.append(string[i])
            else:
                cal.append(string[i])
        else:
            if cal:
                while cal[-1] != '(':
                    postfix.append(cal.pop())
                    if not cal:
                        break
                cal.pop()

    for i in range(len(postfix)):
        if postfix[i] == '+':
            b = int(cal.pop())
            a = int(cal.pop())
            cal.append(a + b)
        elif postfix[i] == '-':
            b = int(cal.pop())
            a = int(cal.pop())
            cal.append(a - b)
        elif postfix[i] == '*':
            b = int(cal.pop())
            a = int(cal.pop())
            cal.append(a * b)
        elif postfix[i] == '/':
            b = int(cal.pop())
            a = int(cal.pop())
            cal.append(a / b)
        else:
            cal.append(postfix[i])

    print("#{} {}".format(tc, cal[0]))
```

---

괄호까지 포함된 후위계산식



#### 후위계산식 변경 과정

제약 사항 : 계산 기호는 `+`,`*` 뿐이다. 숫자는 0 - 9만 있다.

1. 숫자와 ``(``는 기본적으로 push
2. `+`는 계산식 ``(``가 나오거나 빌 때까지 pop 하여 숫자가 담긴 스택에 push한 뒤에, 마지막으로 push
3. `*`는 `+`나 ``(``가 나올 때까지  계산식 스택에서 pop하고, push
4. 계산식 스택이 비어 있으면 무조건 push

#### 계산 과정

1. 0번 인덱스부터 계산식까지 탐색. 숫자는 모두 스택에 push
2. 계산식이 나오면 스택에서 두 개를 pop하여 계산한 뒤 다시 push
3. 마지막으로 남은 숫자 하나가 정답



제약사항에는 ``+``와``*``만 나온다고 되어 있지만, 연습 삼아 ``-``과 ``/``도 포함시켰다.
