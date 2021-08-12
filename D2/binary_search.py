def binary_search(P, key):
    count = 0
    start = 1
    end = P
    # 이진 탐색
    while start <= end:
        mid = (start + end) // 2
        if mid == key:
            return count
        elif mid < key:
            start = mid
            count += 1
        else:
            end = mid
            count += 1
    return P


T = int(input())
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    member = []
    member += [binary_search(P, Pa)] + [binary_search(P, Pb)]

    if member[0] < member[1]:
        print("#{} {}".format(test_case, 'A'))
    elif member[0] > member[1]:
        print("#{} {}".format(test_case, 'B'))
    else:
        print("#{} {}".format(test_case, 0))
