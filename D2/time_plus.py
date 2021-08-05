T = int(input())

for test_case in range(1, T + 1):
    times = list(map(int, input().split()))

    result = []
    for i in range(len(times)//2):
        result.append(times[i] + times[i+2])

    if result[1] >= 60:
        result[0] += 1
        result[1] -= 60

    print("#{} {} {}".format(test_case, result[0] % 12 if result[0] % 12 != 0 else: 12, result[1]))
