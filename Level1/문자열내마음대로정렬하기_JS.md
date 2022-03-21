# 문자열 내 마음대로 정렬하기

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/12915)

## Solution
```js
function solution(strings, n) {
  return strings.sort((a, b) => {
      if(a[n] < b[n]) return 1
      else if(a[n] === b[n]) {
        return a > b ? 1 : -1
      }
      else return -1
  })
}
```