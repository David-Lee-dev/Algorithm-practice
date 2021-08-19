## 간단한 압축풀기(#1946)

```python
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    details = []
    for i in range(N):
        tmp = list(input().split())
        details.append(tmp)

    result = ''
    for detail in details:
        for i in range(int(detail[1])):
            result += detail[0]

    print("#{}".format(test_case))
    for i in range(len(result)):
        print(result[i], end="")
        if not (i+1) % 10:
            print()
    print()

```

