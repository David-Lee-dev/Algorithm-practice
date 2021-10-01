## 최대 상금(#1244)

```python
T = int(input())

def back_tracking(c, idx):
    if c == 0:
        money()
        return
    c -= 1
    for i in range(idx, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            if numbers[idx] >= max(numbers[idx:]):
                if len(numbers) - idx > 2:
                    idx += 1
                if len(numbers) - idx == 2:
                    if c % 2:
                        numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
                    money()
                    return
                back_tracking(c, idx)
                idx -= 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

def money():
    global result
    tmp = 0
    for i in range(len(numbers)):
        tmp += numbers[i] * (10 ** (len(numbers) - i - 1))
    if tmp > result:
        result = tmp
    return

for tc in range(1, T + 1):
    result = 0
    tmp, count = map(str, input().split())
    numbers = []
    for i in range(len(tmp)):
        numbers.append(int(tmp[i]))
    if len(numbers) < 3:
        if int(count) % 2:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        money()
    else:
        back_tracking(int(count), 0)
    print("#{} {}".format(tc, result))

```

