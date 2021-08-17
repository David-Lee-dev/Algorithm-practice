def palin_check(string):
    for idx in range(len(string)//2):
        if string[idx] != string[len(string)-1-idx]:
            return False
    return True


def length_check(strings, length):
    for i in range(len(strings)):
        for idx in range(100 - length + 1):
            tmp = strings[i][idx:idx + length]
            if palin_check(tmp):
                return tmp


for test_cass in range(1, 11):
    case = int(input())
    matrix = [input() for _ in range(100)]

    for idx in range(100):
        length = len(matrix) - idx
        for idx1 in range(100):
            row = matrix[idx1]
            col = ''
            for idx2 in range(100):
                col += matrix[idx2][idx1]
            tmp = length_check((row, col), length)
            if tmp:
                print("#{} {}".format(test_cass, len(tmp)))
                break
        if tmp:
            break
