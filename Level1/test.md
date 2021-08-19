## 모의고사

```python
def solution(answers):
    answer = []
    members = [
        {'id': 1, 'score' : 0, 'pattern' : (1, 2, 3, 4, 5)},
        {'id': 2, 'score' : 0, 'pattern' : (2, 1, 2, 3, 2, 4, 2, 5)},
        {'id': 3, 'score' : 0, 'pattern' : (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)},
    ]
    
    for pro_num in range(len(answers)):
        for member in (members):
            #체점
            if answers[pro_num] == member['pattern'][pro_num%len(member['pattern'])]:
                member['score'] += 1
    
    max_score = max([members[0]['score'], members[1]['score'], members[2]['score']])
    for member in members:
        if member['score'] == max_score:
            answer += [member['id']]
            
    return answer
```

