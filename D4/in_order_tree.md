## 중위순회(#1231)

```python
    def in_order(n):
        if n:
            in_order(left[n])
            print(data[n], end='')
            in_order(right[n])
        return


    for tc in range(1, 11):
        N = int(input())
        data = [0] * (N + 1)
        left = [0] * (N + 1)
        right = [0] * (N + 1)
        for i in range(1, N + 1):
            ip = list(map(str, input().split()))
            data[int(ip[0])] = ip[1]
            if len(ip[2:]) > 1:
                left[int(ip[0])] = int(ip[2])
                right[int(ip[0])] = int(ip[3])
            elif len(ip[2:]) > 0:
                left[int(ip[0])] = int(ip[2])
        print("#{} ".format(tc), end='')
        in_order(1)
        print()
```
중위 순회 탐색