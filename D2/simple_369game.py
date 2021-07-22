def change(i):
    result = ''
    for j in i:
        if (j == '3' or j == '6' or j == '9'):
            j = '-'
            result += j
        
    return result

N = int(input())

for i in range(1, int(N)+1):
    for j in str(i):
        if (j == '3' or j == '6' or j == '9'):
            i = change(str(i))
            break
        i = str(i)
    print(i, end=' ')
    