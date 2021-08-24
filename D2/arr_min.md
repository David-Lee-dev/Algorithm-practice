## 배열 최소합(#4881)

```python
def min_arr(i, tmp):
    global min_num
    if min_num < tmp:
        return

    if i == len(matrix):
        if min_num > tmp:
            min_num = tmp
        return

    for j in range(len(matrix)):
        if visited[j] != 1:
            tmp += matrix[i][j]
            visited[j] = 1
            min_arr(i+1, tmp)
            visited[j] = 0
            tmp -= matrix[i][j]



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_num = 10 * N
    min_arr(0, 0)

    print("#{} {}".format(tc, min_num))
```

---

백트래킹으로 풀어야 하는 문제. DPS로 풀면 시간 초과가 발생한다.



1. 행 단위로 재귀 호출
2. 사용하지 않은 열일 경우 해당 값을  ``tmp``에 더하기
3. 가장 깊이 들어갔을 경우 최소값과 비교하여 교환
4. 끝까지 탐색하지 않더라도 최솟값보다 ``tmp``가 크면 탐색을 중단한다. (가지치기)



최솟값이 ``global`` 변수로 지정되어 있는데 도무지 방법이 떠오르지 않는다. 변수를 함수 내에서 선언하면 함수의 종료와 함께 유효 범위가 끝나기 때문에 계속해서 유지시켜줄 방법이 떠오르지 않았다. 물론 함수를 호출할 때마다 최소값을 인자로 전달해줄 수 있지만 오히려 비효율적이라고 생각했다.
