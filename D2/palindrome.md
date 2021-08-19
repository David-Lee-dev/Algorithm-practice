## 초심자의 회문 검사(#1989)

```python
T = int(input())

for test_case in range(1, T + 1):
    N = input()
    tmp = len(N)//2

    buf_1 = N[:tmp]
    buf_2 = N[-tmp:]
    
    for i in range(len(buf_1)):
        if(buf_1[i] != buf_2[-i-1]):
            print('#{} 0'.format(test_case))
            break
    else:
        print('#{} 1'.format(test_case))

```

