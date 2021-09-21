# 없는 숫자 더하기

---

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/86051?language=javascript)

## Solution
```js
function solution(numbers) {
  var answer = 45;
  const tmp = new RegExp(/[0-9]/)
  numbers.forEach(number => {
    if (tmp.test(String(number))) {
      console.log(number)
      answer -= number
    }
  })
  return answer;
}
```

0~9까지 존재하는 숫자를 빼면 없는 숫자를 모두 더한 것과 같다.