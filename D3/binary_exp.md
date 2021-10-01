## 이진수 표현(#10726)

```python
T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())

    binary = ''
    while M > 1:
        binary = str(M % 2) + binary
        M //= 2
    binary = (str(M) + binary).zfill(30)
    if '0' in binary[-N:]:
        print("#{} {}".format(tc, 'OFF'))
    else:
        print("#{} {}".format(tc, 'ON'))


```

