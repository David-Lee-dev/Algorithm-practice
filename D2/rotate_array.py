import copy

T = int(input())
for test_case in range(1, T + 1):

    N = int(input())

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    tmp_arr = copy.deepcopy(arr)
    results = []
    for i in range(N):
        results.append([0, 0, 0])

    for result_col in range(3):
        # 90도 회전
        for row in range(N):
            for col in range(N):
                tmp_arr[row][col] = arr[N-col-1][row]
        arr = copy.deepcopy(tmp_arr)

        # 회전된 행렬
        rotate = []
        for tmp in tmp_arr:
            num = 0
            for n in range(len(tmp)):
                num += tmp[n]*(10**(len(tmp)-n-1))
            rotate += [num]

        # 결과값
        for result_row in range(N):
            results[result_row][result_col] = rotate[result_row]

    print("#{}".format(test_case))
    for result in results:
        for i in range(len(result)):
            print(str(result[i]).zfill(N), end=" ")
        print()
