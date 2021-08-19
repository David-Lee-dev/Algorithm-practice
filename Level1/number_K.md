## K번째 수

```python
def solution(array, commands):
    answer = []
    for command in commands:
        tmp_array = array[command[0]-1:command[1]]
        answer += [sorted(tmp_array)[command[2]-1]]
    return answer
```

