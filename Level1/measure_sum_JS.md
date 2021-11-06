# 약수의 개수와 덧셈

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/77884)

## Solution
```js
function solution(left, right) {
  var answer = 0;
  for (let num = left; num <= right; num++) {
    let tmp = []
    for (let i = 1; i <= num; i++)
      if (num % i === 0) tmp.push(i)
    answer += tmp.length % 2 === 0 ? num : -num
  }
  return answer;
}
```
