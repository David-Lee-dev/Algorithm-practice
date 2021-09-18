# 키패드 누르기

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/67256?language=javascript)

## Solution
```js
function solution(numbers, hand) {
  var answer = '';
  let left = [3, 0];
  let right = [3, 2];
  const btns = {
    1: 'L',
    4: 'L',
    7: 'L',
    3: 'R',
    6: 'R',
    9: 'R',
  }
  const btns_keys = Object.keys(btns)
  for (let number of numbers) {
    // 행동이 정해진 버튼 입력
    if (btns_keys.includes(String(number))) {
      let tmp = btns[number]
      answer += tmp
      if (tmp === 'L') {
        left = [parseInt((number - 1) / 3), 0]
      } else {
        right = [parseInt((number - 1) / 3), 2]
      }
    }
    // 행동이 정해지지 않은 버튼 입력
    else {
      let btn = null
      // 가운데 열 버튼 위치
      if (number === 0) {
        btn = [3, 1]
      } else {
        btn = [parseInt((number - 1) / 3), 1]
      }
      // 이동량 계산
      const left_cnt = [Math.abs(btn[0] - left[0]), Math.abs(btn[1] - left[1])].reduce((acc, cur) => acc + cur, 0)
      const right_cnt = [Math.abs(btn[0] - right[0]), Math.abs(btn[1] - right[1])].reduce((acc, cur) => acc + cur, 0)
      console.log(btn)
      console.log(left_cnt, left, right_cnt, right)
      // 위치 이동
      if (left_cnt < right_cnt) {
        answer += 'L'
        left = btn
      } else if (left_cnt > right_cnt) {
        answer += 'R'
        right = btn
      } else {
        if (hand === 'left') {
          answer += 'L'
          left = btn
        } else {
          answer += 'R'
          right = btn
        }
      }
    }
  }

  return answer;
}
```
>[
>[1, 2, 3],
>[4, 5, 6],
>[7, 8, 9],
>['*', 0, '#'],
>]

위와 같은 이차원 배열이 있다는 가정하에 해결했다.
1, 4, 7, 3, 6, 9는 정해진 규칙이 있으므로 객체에 key:value 형태로 저장해서 해당 규칙을 지킬수 있게 했다.

버튼의 위치에 해당하는 행과 열, ``left`` 혹은 ``right``에 해당하는 행과 열의 각각 차이를 더하면 이동량이 된다. 이동량을 기준으로 ``left``에 변화를 줄지 ``right``에 변화를 줄지 결정한다.

행을 결정하는 방식은 ``parseInt((number - 1) / 3)``이고 열을 결정하는 방식은 숫자별로 고정되어 있다.

1. 먼저 객체 메서드인 ``keys()`` 를 이용해서 key 값을 저장한 배열(``btns_keys``)을 만들었다. 이 메서드는 **배열 안에 요소를 문자열 형태로 저장한다.**
2. ``number``가 ``btns_keys``에 포함될 경우 ``btns[number]``값을 ``answer``에 추가해준다.
3. ``number``가 ``btns_keys``에 포함되지 않을 경우, ``btn``의 위치를 0 혹은 2,5,8의 경우로 나눠 결정한다.
4. ``left``, ``right``와 ``btn``의 행의 차이, 열의 차리를 더하여 각각의 이동량을 계산한다.
5. 이동량을 기준으로 규칙에 맞는 문자를 answer에 추가한다.

이동량 계산을 할 때 ``reduce``메서드를 사용했다. ``reduce``는 배열의 각 요소끼리 콜백 함수를 호출하여 하나의 값을 반환하는 메서드이다.

>[reduce 참고](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)
