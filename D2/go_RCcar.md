## 가랏! RC카!(#1940)

```python
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    commends = []
    for i in range(N):
        commends.append(list(map(int, input().split())))

    distance = 0
    speed = 0
    mean = [0, 1, -1]
    for commend in commends:
        if commend[0] != 0:
            speed += mean[commend[0]]*commend[1]
            if speed < 0:
                speed = 0
            distance += speed
        else:
            distance += speed

    print("#{} {}".format(test_case, distance))

```

