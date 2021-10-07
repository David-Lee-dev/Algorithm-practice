## 퀵정렬(#5205)

```python
def quick():
    while stack:
        l, r = stack.pop()
        pivot = l
        i = l
        j = r
        if i >= j:
            continue
        while i < j:
            while i <= j and arr[i] <= arr[pivot]:
                i += 1
            while i <= j and arr[j] >= arr[pivot]:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[pivot], arr[j] = arr[j], arr[pivot]
        stack.append((l, j-1))
        stack.append((j + 1, r))


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))

    stack = [(0, len(arr) - 1)]
    quick()
    print("#{} {}".format(tc, arr[N//2]))

```

