# 소수 만들기

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/12977)

## Solution
```js
function solution(nums) {
  var answer = 0;
  let set = []

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        set.push(nums[i] + nums[j] + nums[k])
      }
    }
  }

  set.forEach(el => {
    let idx = 2
    for (idx = 2; idx < el; idx++) {
      if (el % idx === 0) {
        break
      }
    }
    if (idx === el) answer++;
  })
  return answer;
}
```
