T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    result = []
    for money in moneys:
        result += [N // money]
        N %= money

    print("#{}".format(1))
    print(*result)
