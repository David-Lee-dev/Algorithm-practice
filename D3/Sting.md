## String(#1213)

```python
T = 10
for test_case in range(1, T+1):
    case = int(input())
    target = input()
    string = input()
    result = 0

    for idx in range(len(string) - len(target)+1):
        if string[idx:idx + len(target)] == target:
            result += 1

    print("#{} {}".format(test_case, result))
```

