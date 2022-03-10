# [1차]다트게임

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/17682)

## Solution
```js
function solution(dartResult) {
  const mul = {
    'S': 1,
    'D': 2,
    'T': 3,
  }
  const answer = []

  let idx = 0
  while(idx < dartResult.length) {
    let score = ''
    while((/[0-9]+/g).test(dartResult[idx])) {
      score += dartResult[idx++]
    }
    score = Math.pow(Number(score), mul[dartResult[idx++]])
    switch(dartResult[idx]) {
      case '*':
        if(answer.length > 0) answer[answer.length - 1] *= 2
        score *= 2
        idx++;
        break;
      case '#':
        score *= -1
        idx++;
        break;
    }
    answer.push(score)
  }
  return answer.reduce((acc, cur) => acc+cur)
}
```