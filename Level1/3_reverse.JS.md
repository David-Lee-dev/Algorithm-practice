# 3진법 뒤집기

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/68935)

## Solution
```js
function solution(n) {
  var answer = 0;
  let num3 = []
  while (n > 2) {
    num3.push(n % 3)
    n = parseInt(n / 3)
  }
  num3.push(n)
  num3.reverse()
  answer = num3.reduce((acc, cur, idx) => acc + cur * Math.pow(3, idx))

  return answer;
}
```
<br>

## Cleanup
```js
const solution = (n) => {
    return parseInt([...n.toString(3)].reverse().join(""), 3);
}
```
- toString을 이용해 n을 3진법 문자열로 변경
> [toString 참고](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)

- 변경된 문자열을 전개 연산자를 이용해 각 문자를 분리해 배열로 저장
- 변경된 배열을 뒤집은 뒤 10진 parseInt로 10진법으로 변경
> [parseInt 참고](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
