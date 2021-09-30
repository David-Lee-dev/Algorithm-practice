## 이진수(#5185)

```python
T = int(input())

for tc in range(1, 1+T):
    num = float(input())

    binary = ''
    while num != 0:
        num *= 2
        if num >= 1:
            binary += '1'
            num -= 1
        else:
            binary += '0'

    if len(binary) > 12:
        print("#{} {}".format(tc, 'overflow'))
    else:
        print("#{} {}".format(tc, binary))
```

