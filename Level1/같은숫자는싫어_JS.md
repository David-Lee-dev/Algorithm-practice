# 같은 숫자는 싫어

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/12906)

## Solution
```js
function solution(arr)
{
  const answer = [arr[0]];
  arr.forEach(element => {
    if(answer[answer.length-1] !== element) answer.push(element)
  });

  return answer
}
```