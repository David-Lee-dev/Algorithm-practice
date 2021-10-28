# 모의고사

>[문제 출처](https://programmers.co.kr/learn/courses/30/lessons/42840)

## Solution
```js
function solution(answers) {
  var answer = []
  let result = []
  const patterns = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  ]
  patterns.forEach(pattern => {
    let idx = 0
    let count = 0
    answers.forEach(num => {
      if (num === pattern[idx]) {
        count++
      }
      idx++
      if (idx === pattern.length) {
        idx = 0
      }

    })
    answer.push(count)
  })
  max_idx = 0
  for (let i = 1; i < 3; i++)
    if (answer[max_idx] < answer[i]) max_idx = i;
  for (let i = 0; i < 3; i++)
    if (answer[i] === answer[max_idx]) result.push(i + 1)

  return result;
}

}
```


## Clean-up
```js
function solution(answers) {
    var answer = [];
    const a1 = [1, 2, 3, 4, 5];
    const a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    const a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    const a1c = answers.filter((a,i)=> a === a1[i%a1.length]).length;
    const a2c = answers.filter((a,i)=> a === a2[i%a2.length]).length;
    const a3c = answers.filter((a,i)=> a === a3[i%a3.length]).length;
    const max = Math.max(a1c,a2c,a3c);

    if (a1c === max) {answer.push(1)};
    if (a2c === max) {answer.push(2)};
    if (a3c === max) {answer.push(3)};

    return answer;
}
```
