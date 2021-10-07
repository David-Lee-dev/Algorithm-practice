## 전기버스2(#5208)

```python
T = int(input())

def BT(now, count):
    global result
    count += 1
    # 횟수가 최소값을 넘어가면 중지
    if result < count:
        return

    # 끝에 도달할 경우
    if now + battery[now] + 1 >= len(battery):
        # 최솟값 갱신
        if result > count:
            result = count
            return

    # 현 위치에서 갈 수 있는 인덱스 범위 지정
    can = range(now+1, now+battery[now]+1)
    for c in can:
        BT(c, count)

for tc in range(1, 1 + T):
    tmp = list(map(int, input().split()))
    N = tmp[0] # 정류장 개수
    battery = tmp[1:] + [0] # 정류장별 배터리 용량
    result = N

    for n in range(1, len(battery[:battery[0]])+1):
        BT(0+n, 0)
    print("#{} {}".format(tc, result))
```

