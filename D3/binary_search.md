## 이진탐색(#5207)

```python
T = int(input())

def bin_search(l, r, num, flag):
    global count
    if l > r:
        return

    m = (l+r) // 2
    if arr[m] == num:
        count += 1
        return
    elif arr[m] > num:
        if flag == 'l':
            return
        bin_search(l, m-1, num, 'l')
    else:
        if flag == 'r':
            return
        bin_search(m + 1, r, num, 'r')



for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    nums = list(map(int, input().split()))
    count = 0
    for n in nums:
        l = 0
        r = N - 1
        side = ''
        bin_search(l, r, n, side)
    print("#{} {}".format(tc, count))

```

