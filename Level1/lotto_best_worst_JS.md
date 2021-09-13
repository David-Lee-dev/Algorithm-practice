>[문제 출처](https://programmers.co.kr/learn/courses/30/lessons/77484)

## Solution
```js
function solution(lottos, win_nums) {
  var answer = [];
  const rank = [6, 6, 5, 4, 3, 2, 1]
  let count = 0
  let zero_count = 0
  for (let num of lottos) {
    if (num === 0) {
      zero_count++
      continue
    }
    for (let win_num of win_nums) {
      if (num === win_num) {
        count++
        break
      }
    }
  }
  zero_count += count
  answer.push(rank[zero_count], rank[count])
  return answer;
}
```
``lottos``배열을 순회하면서 일치하는 번호의 개수와 0의 개수를 파악한다. 일치하는 번호의 개수가 최소로 맞춘 개수이며, 0의 개수까지 더하면 최대로 맞춘 개수가 된다.

``rank``배열의 각각 등수가 저장되어 있고 인덱스가 맞춘 번호의 개수이다.

## Clean-up
```js
function solution(lottos, win_nums) {
  var answer = [];
  const rank = [6, 6, 5, 4, 3, 2, 1]
  let count = 0

  let zero_count = lottos.filter(num => num === 0)
  lottos.forEach(num => {
    if (win_nums.includes(num)) {
      count++
    }
  })
  answer.push(rank[zero_count.length + count], rank[count])
  return answer;
}
```
1. 0의 개수를 파악하는 반복문을 ``fillter``메서드로 교체. ``zero_count``는 ``lottos``함수의 0의 개수만큼 0을 가지고 있는 배열이 된다.<br>
``fillter``메서드는 조건에 해당하는 원소가 없을 경우 빈 배열을 반환하기 때문에 ``lottos``함수에 0이 없어도 된다.

2. 당첨 번호와 일치하는 번호의 개수를 파악하는 부분을 ``forEach``와 ``includes`` 메서드를 사용했다. ``lottos``의 각 요소마다 ``win_nums``에 포함되는지 확인한다. ``includes``메서드는 true, false 형태로 반환하기 때문에 사용했다.
