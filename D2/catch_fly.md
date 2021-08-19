## 파리 퇴치(#2001)

```python
T = int(input())

for test_case in range(1, T + 1):
    
    N, M = map(int,input().split())
    [list(map(int,input().split())) for _ in range(N)]

    kill = 0
    for col in range(N-M+1):
        for row in range(N-M+1):
            buf = 0
            for tool_col in range(M):
                for tool_row in range(M):
                    buf += arr[row+tool_row][col+tool_col]
            if(buf > kill):
                kill = buf
    print('#{} {}'.format(test_case, kill))
```

