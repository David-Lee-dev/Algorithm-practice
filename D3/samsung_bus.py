T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    roots = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]
    result = [0] * P

    for i in range(len(roots)):
        for c in range(len(C)):
            if C[c] >= roots[i][0] and C[c] <= roots[i][1]:
                result[c] += 1

    print("#{}".format(test_case), end=" ")
    print(*result)
