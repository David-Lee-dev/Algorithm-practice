# K번째 수

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/42748)

## Solution
```js
function solution(array, commands) {
  var answer = [];
  commands.forEach(element => {
    answer.push(
      array.slice(element[0] - 1, element[1])
      .sort((a, b) => a - b)[element[2] - 1])
  });
  return answer;
}
```
