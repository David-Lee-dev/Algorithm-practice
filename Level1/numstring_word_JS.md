# 숫자 문자열과 영단어

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/81301?language=javascript)

## Solution
```js
function solution(s) {
  var answer = 0;
  const numbers = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
  }
  const values = Object.keys(numbers)
  values.forEach(value => {
    let reg = RegExp(value)
    while (reg.test(s)) {
      s = s.replace(reg, numbers[value])
    }
  });
  answer = parseInt(s)
  return answer;
}

console.log(solution("one4seveneight"))
```
1. 일치하는 문자열을 찾았을 때 숫자로 변환하기 위해서 단어 : 숫자를 ``key`` : ``value`` 형식으로 객체를 만들었다.

2. 객체 메서드인 ``keys()``를 이용해서 ``numbers``의 ``key``를 모아서 따로 배열로 만들고 각 ``forEach``메서드를 활용해서 각 요소마다 콜백함수를 실행하도록 했다.

3. 콜백함수는 문자열에 함수 실행 시 요소에 해당하는 문자열이 포함되지 않을 때까지 ``replace``메서드를 실행한다.

3. 변환된 결과는 String 타입이므로 Int 타입으로 바꾼다.