# [1차]다트게임

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/12910)

## Solution
```js
function solution(arr, divisor) {
  const answer = arr.filter(el => el % divisor === 0).sort( (a, b) => a - b)
  return answer.length < 1 ? [-1] : answer
}

```