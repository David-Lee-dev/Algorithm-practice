## 정식이의 은행업무(#4366)

```python
T = int(input())

def change_bit(index):
    if n2[index] == '1':
        n2[index] = '0'
    else:
        n2[index] = '1'

def _2_to_10(n2):
    result = 0
    for i in range(len(n2)):
        result += int(n2[i]) * (2**(len(n2) - 1 - i))
    return result

def _10_to_3(num):
    result = []
    while num > 2:
        result.append(str(num%3))
        num //= 3
    result.append(str(num))
    return ''.join(result[::-1])

def check(n3, t):
    count = 0
    for i in range(len(n3)):
        if n3[i] != t[i]:
            count += 1

    if count == 1:
        return True
    return False

for tc in range(1, 1 + T):
    n2 = list(input())
    n3 = input()
    result = 0

    for i in range(len(n2)):
        change_bit(i)
        Dec = _2_to_10(n2)
        Trit = _10_to_3(Dec)
        if len(n3) == len(Trit):
            if check(n3, Trit):
                result = Dec
                break
        change_bit(i)

    print("#{} {}".format(tc,result))
```

