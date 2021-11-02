# 포켓몬

>[문제 출처](https://programmers.co.kr/learn/courses/30/lessons/1845)

## Solution
```js
function solution(nums) {
  var answer = 0;
  let tmp = []
  nums.forEach(el => {
    if (!tmp.includes(el)) tmp.push(el)
  })
  return answer = nums.length / 2 > tmp.length ? tmp.length : nums.length / 2;
}
```
