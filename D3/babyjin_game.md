## 베이비진 게임(#5203)

```python
T = int(input())

def baby_jin(player):
    cnt_lst = [0] * 10
    result = False
    for idx in range(len(player)):
        cnt_lst[player[idx]] += 1

    run = triple = i = 0
    while i < 10:
        if i <= 7:
            if cnt_lst[i] >= 1 and cnt_lst[i + 1] >= 1 and + cnt_lst[i + 2] >= 1:
                cnt_lst[i] -= 1
                cnt_lst[i + 1] -= 1
                cnt_lst[i + 2] -= 1
                run += 1
                result = True

        if cnt_lst[i] >= 3:
            cnt_lst[i] -= 3
            triple += 1
            result = True

        i += 1

    return result

for tc in range(1, 1 + T):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    result = 0

    for i in range(0, len(cards), 2):
        player1.append(cards[i])
        player2.append(cards[i + 1])
        player1_result = baby_jin(player1)
        player2_result = baby_jin(player2)
        if player1_result == 1 and player2_result == 0:
            result = 1
            break
        elif player1_result == 0 and player2_result == 1:
            result = 2
            break
        elif player1_result == 1 and player2_result == 1:
            result = 1
            break

    print("#{} {}".format(tc, result))
```

