## 최빈수 구하기(#1204)

```python
T = int(input())

for test_case in range(1, T + 1):
    N = input()
    student_score = list(map(int, input().split()))
    scores = []
    for i in range(101):
        scores.append(0)
    max_count_index = 0
    max_count = 0
    result = 0

    for student in student_score:
        scores[student] += 1
    for score in scores:
        if max_count <= score:
            max_count = score
    for score in scores:
        if max_count == score:
            result = max_count_index
        max_count_index += 1

    print("#{} {}".format(test_case, result))

```

