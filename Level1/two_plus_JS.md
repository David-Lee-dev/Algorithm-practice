# 두 개 뽑아서 더하기

---

>[문제 출처](https://programmers.co.kr/learn/courses/30/lessons/68644)

# Solution
```js
function solution(numbers) {
  var answer = [];
  for (let i = 0; i < numbers.length - 1; i++)
    for (let j = i + 1; j < numbers.length; j++)
      if (!answer.includes(numbers[i] + numbers[j]))
        answer.push(numbers[i] + numbers[j])
  return answer.sort((a, b) => a - b);
}
```