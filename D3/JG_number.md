## 정곤이의 단조 증가하는 수(#6190)

```python
T = int(input())
def divide(n):
    tmp = []
    while n > 0:
        tmp += [n % 10]
        n //= 10
    return tmp

def check(n):
    sep = divide(n)
    for i in range(len(sep)-1):
        if sep[i+1] > sep[i]:
            return -1
    return n

def max(li):
    result = li[0]
    for i in range(1, len(li)):
        if result < li[i]:
            result = li[i]

    return result

for tc in range(1, 1 + T):
    N = int(input())
    numbers = list(map(int, input().split()))
    Ai_Aj = []
    up_nums = []
    result = 0
    # Ai * Aj 리스트 만들기
    for i in range(N - 1):
        for j in range(i + 1, N):
            Ai_Aj += [numbers[i] * (numbers[j])]
    # 단조 증가하는 수 리스트 만들기
    for i in range(len(Ai_Aj)):
        if Ai_Aj[i] > 9:
            tmp = check(Ai_Aj[i])
            if tmp != -1:
                up_nums.append(tmp)
    #단조 증가하는 수 중에서 최댓값 찾기
    if up_nums:
        result = max(up_nums)
    else:
        result = -1

    print("#{} {}".format(tc, result))

```
---
1. Ai * Aj 모든 경우의 수 중에서
2. 단조증가인 수를 추려내고
3. 최대값을 구한다.