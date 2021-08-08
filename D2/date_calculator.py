T = int(input())
years = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
for test_case in range(1, T + 1):
    days = list(map(int, input().split()))

    result = 0
    for i in range(days[0], days[2]):
        result += years[i]

    print("#{} {}".format(test_case, result - days[1] + 1 + days[3]))
