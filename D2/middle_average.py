T = int(input())

for test_case in range(1, T + 1):

    N = list(map(int,input().split()))

    min_num = N[0]
    max_num = N[0]

    result = 0
    for i in N:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i
        result += i
    result -= (min_num + max_num)
    result = int((result / (len(N) - 2)) * 10)
    result = (result//10) +1 if result%10 > 4 else (result//10)

    print('#{} {}'.format(test_case, result))