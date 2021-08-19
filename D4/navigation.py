for _ in range(1, 11):
    matrix = [[] for _ in range(100)]
    tc, pairs = map(int, (input().split()))
    numbers = list(map(int, input().split()))

    for i in range(0, len(numbers), 2):
        matrix[numbers[i]] += [numbers[i+1]]

    visited = [0] * 100
    stack = [0]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = 1
            for i in range(len(matrix[vertex])):
                if not visited[matrix[vertex][i]]:
                    stack.append(matrix[vertex][i])

    print("#{} {}".format(tc, visited[-1]))
