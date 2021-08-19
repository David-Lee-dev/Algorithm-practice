## 파스칼의 삼각형(#2005)

```python
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    print('#{}'.format(test_case))
    
    pre_layer = [1, 1]
    now_layer = []
    
    for i in range(1, N+1):
        if(i>2):
            for j in range(i):
                if(j > 0 and j < i-1):
                    now_layer += [pre_layer[j-1] + pre_layer[j]]
                else:
                    now_layer += [1]
                print(now_layer[j], end=' ')
            pre_layer = now_layer
            now_layer = []
            print()
        else:
            if(i == 1):
                print('1')
            else:
                print('1 1')

```

