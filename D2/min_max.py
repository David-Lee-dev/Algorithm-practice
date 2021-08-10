T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))

    max = min = ai[0]
    for idx in range(1, len(ai)):
        max = ai[idx] if max < ai[idx] else max
        min = ai[idx] if min > ai[idx] else min

    print("#{} {}".format(test_case, max - min))
