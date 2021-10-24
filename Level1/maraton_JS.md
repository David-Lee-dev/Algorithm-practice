# 완주하지 못한 선수

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/42576)

## Solution
```js
function solution(participant, completion) {
  var answer = ''
  let part = Object()
  participant.forEach(el => {
    if (part[el] === undefined) {
      part[el] = 1
    } else {
      part[el]++
    }
  });
  completion.forEach(el => {
    part[el] -= 1
  });
  const part_key = Object.keys(part)
  const part_value = Object.values(part)
  answer = part_key[part_value.indexOf(1)]
  return answer
}
```
