# 예산

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/12982)

## Solution
```js
function solution(d, budget) {
  var answer = 0;
  let tmp = 0
  d.sort((a, b) => a - b)
  for (let num of d) {
    tmp += num
    answer++;
    if (tmp === budget) break
    else if (tmp > budget) {
      tmp -= num
      answer--;
    }
  }
  return answer
}
```
<br>

## Cleanup
```js
function solution(d, budget) {
  var answer = 0;
  let tmp = 0
  d.sort((a, b) => a - b).forEach(num => {
    tmp += num
    if (tmp <= budget) answer++;
  })
  return answer
}
}
```