# 나머지가 1이 되는 수 찾기

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/87389)

## Solution
function solution(n) {
  var answer = 1
  while(n % answer != 1){
    answer += 1
  }
  return answer
}
```
