T = int(input())

tmp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
table = ''
table += tmp
table += tmp.lower() + '0123456789+/'
del tmp
# index 찾기


def find_index(word):
    count = 0
    for i in table:
        if i == word:
            return count
        count += 1

# 2진수 변환


def make_2n(number):
    tmp = ''
    while number > 1:
        tmp += str(number % 2)
        number //= 2
    tmp += str(number)

    for i in range(6 - len(tmp)):
        tmp += '0'

    return tmp[-1::-1]

# 10진수 변환


def make_10n(words):
    words = words[-1::-1]
    tmp = 0
    for i in range(len(words)):
        tmp += int(words[i])*(2**i)
    return tmp


for test_case in range(1, T + 1):
    string = input()
    n_2 = ''
    for n in range(0, len(string), 4):
        words = string[n:n+4]
        for word in words:
            tmp = find_index(word)
            n_2 += make_2n(tmp)

    result = []
    for n in range(0, len(n_2), 8):
        words = n_2[n:n+8]
        result.append(make_10n(words))

    print("#{}".format(test_case), end=" ")
    for num in result:
        print(chr(num), end="")
    print()
