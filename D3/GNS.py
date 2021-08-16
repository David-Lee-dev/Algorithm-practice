def change(word, numbers):
    for idx in range(len(numbers)):
        if word == numbers[idx]:
            return idx

T = int(input())
for test_case in range(1, T+1):
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    case = list(map(str, input().split()))
    string = list(map(str, input().split()))
    tmp = [0] * 10

    for idx in range(len(string)):
        tmp[change(string[idx], numbers)] += 1

    print(case[0])
    for i in range(len(tmp)):
        for j in range(tmp[i]):
            print(numbers[i], end=" ")
    print()
