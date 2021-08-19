for tc in range(1, 11):
    length, pwd = map(str, input().split())
    result = pwd[0]
    for i in range(1, int(length)):
        if result:
            if result[-1] == pwd[i]:
                result = result[:-1]
            else:
                result += pwd[i]
        else:
            result += pwd[i]

    print("#{} {}".format(tc, result))
