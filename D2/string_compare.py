T = int(input())

for test_cass in range(1, T+1):
    N = input()
    M = input()

    for idx in range(len(M) - len(N) + 1):
        if M[idx:idx+len(N)] == N:
            print("#{} {}".format(test_cass, 1))
            break
    else:
        print("#{} {}".format(test_cass, 0))

