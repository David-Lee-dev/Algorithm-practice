## 러시아 국기 같은 깃발(#4613)

```python
def color(index, c, N):
    result = 0
    for i in range(len(matrix[index])):
        if matrix[index][i] != c:
            result += 1
    if index == N:
        return result
    if c == 'W':
        if index == N - 1:
            result += color(index + 1, 'B', N)
        else:
            result += min(color(index + 1, 'W', N), (index + 1, 'B', N))
    elif c == 'B':
        result += min(color(index + 1, 'B', N), color(index + 1, 'R', N))
    else:
        result += color(index + 1, 'R', N)
    return result
T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    cnt = 0
    for i in range(M):
        if matrix[0][i] != 'W':
            cnt += 1
        if matrix[N-1][i] != 'R':
            cnt += 1
    cnt += min(color(1, 'W', N - 2), color(1, 'B', N - 2))

    print("#{} {}".format(tc, cnt))


```

---
모든 경우의 수를 탐색해서 최소값을 찾는다.

1. 첫번 째와 마지막 줄은 무조건 각각 흰색과 빨간색이다.
2. 1 ~ N - 1 번째 줄까지의 경우의 수를 조합해 최소값을 결정한다.
3. 흰색으로 바꿀 경우 다음 경우의 수는 흰색 또는 파란색이다. 만약 탐색 마지막 전 줄이라면 파란색만 가능하다.
4. 파란색으로 바꿀 경우 다름 경우의 수는 파란색과 빨간색이다.
5. 빨간색으로 바꿀 경우 다음 경우의 수는 빨간색 뿐이다.
6. 마지막 줄에 도달할 경우 바꾼 색의 수를 반환한다.
7. 반환 받은 값 중 작은 값을 더한다.
