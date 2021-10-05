## 이진수 표현(#10726)

```python
T = int(input())
def sorting(lst):
    for i in range(len(lst)-1, -1 , -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    containers = sorting(list(map(int, input().split())))
    trucks = sorting(list(map(int, input().split())))
    result = 0

    for t in range(len(trucks)-1, -1, -1):
        truck = trucks[t]
        for c in range(len(containers)-1, -1, -1):
            container = containers[c]
            if container <= truck:
                result += container
                containers[c] = 101
                break
    print("#{} {}".format(tc, result))
```

