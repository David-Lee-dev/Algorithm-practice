T = int(input())
for i in range(T):
    N = int(input())
    days = list(map(int, input().split(' ')))[::-1]
    
    answer = 0
    now_max = days[0]

    for j in range(1, N):
        if now_max > days[j]:
            answer += now_max - days[j]
        else:
            now_max = days[j]

    print('#{} {}'.format(i+1, answer))