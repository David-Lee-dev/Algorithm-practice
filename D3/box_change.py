T = int(input())
for test_case in range(1, T + 1):
    N, Q = map(int, input().split())

    L_R = []
    for idx in range(Q):
        L_R += list(map(int, input().split()))

    result = [0]*N
    for idx_N in range(Q):
        L = L_R[2*idx_N]
        R = L_R[2*idx_N+1]

        for idx_L_R in range(L-1, R):
            result[idx_L_R] = idx_N+1

    print("#{}".format(test_case), end=" ")
    print(*result)
