## 어디에 단어가 들어갈 수 있을까(#1979)

```python
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    count = 0
    for i in range(N):
        tmp_row = 0
        tmp_col = 0
        
        for j in range(N):
            #행 이동 연산
            if matrix[j][i]:
                tmp_row += 1
                if(tmp_row == K):
                    count += 1
                if(tmp_row == K + 1):
                    count -= 1
            else:
                tmp_row = 0
            #열 이동 연산
            if matrix[i][j]:
                tmp_col += 1
                if(tmp_col == K):
                    count += 1
                if(tmp_col == K + 1):
                    count -= 1
            else:
                tmp_col = 0

    print('#{} {}'.format(test_case, count))
```

