for test_cass in range(1, T+1):
    str1 = input()
    str2 = input()
    words = dict()
    for idx in range(len(str1)):
        words[str1[idx]] = 0
    for idx in range(len(str2)):
        if words.get(str2[idx]) != None:
            words[str2[idx]] += 1
    result = 0
    for value in words.values():
        if result < value:
            result = value

    print("#{} {}".format(test_cass, result))
