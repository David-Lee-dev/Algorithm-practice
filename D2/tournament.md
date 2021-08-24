## 토너먼트 카드게임(#4880)

```python
def result(i, j):
    if member[i] == member[j]:
        return i
    elif member[i] == 1: # i = 가위
        return j if member[j] == 2 else i
    elif member[i] == 2: # i = 바위
        return i if member[j] == 1 else j
    elif member[i] == 3: # i = 보
        return j if member[j] == 1 else i

def match(i, j):
    if j - i < 1:
        return i
    elif j - i + 1 == 2:
        return result(i, j)
    else: # 3명 이상일 때
        return result(match(i, (i+j)//2), match(((i+j)//2) + 1, j))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    member = list(map(int, input().split()))

    print("#{} {}".format(tc, match(0, len(member) - 1)+1))
```

---

1. 0번을 시작으로 하여 0번 부터 N-1번까지 계속해서 반으로 나눠 토너먼트를 만든다
2. 홀수여서 한 명만 남을 경우 부전승
3. 2명이 남을 경우 게임 결과 반환
4. 3명 이상 남을 경우 재귀호출하여 반으로 나눈다.
