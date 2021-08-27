## 진기의 최고급 붕어빵(#1860)

```python
def sale_slot(slot):
    if len(sale) <= slot:
        for idx_2 in range(len(sale), slot):
            sale.append(0)
        sale.append(1)
    else:
        sale[slot] += 1
    return

def take_out_cnt(slot):
    result = 0
    for idx_3 in range(slot + 1):
        result += sale[idx_3]
    return result

T = int(input())
for tc in range(1, 1 + T):
    N, M, K = map(int, input().split())  # 인원, 생산 시간, 생산량
    enter = list(map(int, input().split()))  # 도착 시간
    sale = [0]  # 시간대 별 판매량
    result = 'Possible'

    for idx_1 in range(N):
        # 만들기도 전에 오면 웨이팅
        if enter[idx_1] < M:
            result = 'Impossible'
            break

        sale_slot(enter[idx_1] // M) # 손님이 온 시간대
        take_out = take_out_cnt(enter[idx_1] // M) # 손님이 도착했을 때 지금까지 가져간 양
        amount = (enter[idx_1] // M) * K - take_out # 만들어 놓은 양 - 가져간 양

        # 만들어 놓은 양보다 가져간 양이 많으면 웨이팅
        if amount < 0:
            result = 'Impossible'
            break

    print("#{} {}".format(tc, result))
```
처음에는 손님이 들어올 때마다 가져간 양을 하나씩 더해서 해결하려고 했다. 하지만 10초에 3개씩 만들 수 있다고 가정했을 때 ``10 10 10 10 20 10``의 문자열이 입력되면 PASS해야 하지만, 그렇지 못하게 된다.<br>
그래서 손님이 온 시간대 별로 가져간 양을 기록해서 해결했다. 손님이 왔을 때, 해당 시간대 이전에 가져간 양을 모두 더하면 정확한 양을 기록할 수 있다.

 - 기본 결과는 ``가능``이고, 반복문에서 별다른 일이 없으면 결과는 변하지 않는다.
 - 반복문 작동 방식
    1. 붕어빵 제작 소요 시간보다 일찍오면 ``불가능``
    2. 손님이 온 시간대를 기록. ex) 60초 제작 시간일 때, 60~119초까지는 첫번째 시간대이다.
    3. 손님 도착 시간대 이전까지 판매량을 모두 더한다.
    4. 도착 시간대까지 만들 수 있는 최대한의 양에서 판매량을 뺀다

