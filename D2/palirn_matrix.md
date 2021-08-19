## 회문(#4861)

```python
def palin(string):
    for idx in range(len(string)//2):
        if string[idx] != string[len(string)-1-idx]:
            return False
    return True


T = int(input())
for test_cass in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    result = ''

    for i in range(N):
        garo = ''
        sero = ''

        for idx in range(N - M + 1):
            garo = matrix[i][idx:idx+M]
            sero = ''
            for j in range(idx, idx + M):
                sero += matrix[j][i]

            if palin(garo):
                result = garo
                break
            elif palin(sero):
                result = sero
                break
        if result:
            break

    print("#{} {}".format(test_cass, result))

```

