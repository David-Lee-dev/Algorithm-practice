## 이진수(#5185)

```python
num16 = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

T = int(input())

for tc in range(1, 1+T):
    N, M = map(str, input().split())

    binary = ''
    for i in range(len(M)):
        num10 = num16[M[i]]
        tmp = []
        while num10 > 1:
            tmp.append(str(num10 % 2))
            num10 //= 2
        tmp.append(str(num10))
        tmp = tmp[::-1]
        while len(tmp) < 4:
            tmp = ['0'] + tmp
        binary += "".join(tmp)

    print("#{} {}".format(tc, binary))
```

