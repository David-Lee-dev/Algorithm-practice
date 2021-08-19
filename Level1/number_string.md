## 숫자 문자열과 영단어

```python
def solution(s):
    numbers = {
        '0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', 
        '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine',
    }
    
    answer = ''
    tmp = ''
    list_s = list(s)
    
    for i in list_s:
        if i in numbers.keys():
            answer += i
        else:
            tmp += i
            if tmp in numbers.values():
                for key, value in numbers.items():
                    if tmp == value:
                        tmp = key
                        break;
                answer += tmp
                tmp = ''

    return int(answer)
```

