T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    arr = [0]*N*N
    row_plus = True
    col_plus = False

    n = 0
    count = 1
    loop_count = N

    while (0 in arr):
        if count > N:
            loop_count -= 1
            for i in range(loop_count):
                if row_plus:
                    arr[n+N] = count
                    n += N
                else:
                    arr[n-N] = count
                    n -= N
                count += 1
            row_plus = not row_plus


            for j in range(loop_count):
                if col_plus:
                    arr[n+1] = count
                    n += 1
                else:
                    arr[n-1] = count
                    n -= 1
                count += 1
            col_plus = not col_plus

        else:   
            arr[n] = count   
            count += 1
            if count < N+1:
                n += 1
                
    print('#{}'.format(test_case))
    count = 1

    for i in range(len(arr)):
        print(arr[i], end=' ')
        if(count == N):
            print()
            count = 0
        count += 1