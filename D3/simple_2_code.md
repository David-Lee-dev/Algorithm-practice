## 단순 2진 암호코드(#1240)

```python
pattern = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]

    count = 0
    binary_pwd = ''
    for code in matrix:
        if '1' not in code:
            continue
        count += 1
        if binary_pwd == '':
            for i in range(len(code) -1, -1, -1):
                if code[i] == '1':
                    binary_pwd = code[i-56+1:i+1]
                    break
    pwd = []
    for i in range(0, len(binary_pwd), 7):
        pwd.append(pattern[binary_pwd[i:i+7]])
    result = (pwd[0] + pwd[2] + pwd[4] + pwd[6])*3 + pwd[1] + pwd[3] + pwd[5]

    if count >= 5 and (result + pwd[7]) % 10 == 0:
        print("#{} {}".format(tc, sum(pwd)))
    else:
        print("#{} {}".format(tc, 0))
```

