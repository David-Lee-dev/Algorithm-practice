## 암호생성기(#1225)

```python
def cycle():
    global stop
    for i in range(1, 6):
        tmp = nums.pop(0) - i
        if tmp <= 0:
            nums.append(0)
            stop = True
            return
        else:
            nums.append(tmp)
    return

for _ in range(1, 11):
    tc = input()
    nums = list(map(int, input().split()))
    stop = False
    while stop == False:
        cycle()

    print("#{}".format(tc), end=" ")
    print(*nums)

```
---
큐를 이용한 문제
1. 첫 숫자를 pop해서 규칙에 맞게 수정.
2. 조건이 맞으면 ``stop``을 ``True``로 하여 반복문 종료
