T = int(input())

for test_case in range(1, T + 1):
    STRING = input()
    
    tmp1 = ''
    tmp2 = ''
    result = 0
    
    for i in range(1, len(STRING)+1):
        for j in range(i):
            tmp1 += STRING[j]
        for k in range(i,i*2):
            tmp2 += STRING[k]
        if(tmp1 == tmp2):
            result = i
            break
        else:
            tmp1 = ''
            tmp2 = ''
            continue
        
    print('#{} {}'.format(test_case, result))
