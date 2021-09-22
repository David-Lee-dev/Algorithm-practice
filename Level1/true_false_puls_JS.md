# 음양 더하기

---

>[문제 출처](https://programmers.co.kr/learn/courses/30/lessons/76501?language=javascript)

# Solution
```js
function solution(absolutes, signs) {
  var answer = 123456789;
  answer = absolutes.reduce((acc, cur_v, cur_i) => {
    if (signs[cur_i]) {
      return acc + cur_v
    } else {
      return acc - cur_v
    }
  }, 0)
  return answer;
}
```
![](https://images.velog.io/images/main_string/post/c1590553-4665-4e3e-ad9a-041672952163/image.png)
``reduce``메서드는 4개의 인자를 받는다.
>- accumulator : 콜백 함수의 결과를 누적
>- currentValue : 처리할 현재 요소
>- currentIndex : 처리할 현재 요소의 인덱스
>- array : 메서드를 호출한 배열
메서드 종료시 accumulator 값을 반환한다.

initialValue를 지정하지 않으면 0번 인덱스 값이 accumulator에 할당되고 1번 인덱스부터 콜백함수가 실행된다. initialValue를 지정하면 해당 값이 accumulator에 할당되고 0번 인덱스부터 콜백함수가 실행된다.

``absolute = [4, 7, 12]`` <br> ``signs = [true, false, true]``<br>위의 조건으로 코드가 실행되면 ``reduce``메서드의 동작은 다음과 같다.

| callback   | accumulator         | currentValue        | currentIndex       | 반환 값             |
| ---------- | ------------------- | ------------------- | ------------------ | ------------------- |
| 1번째 호출 | <center>0</center>  | <center>4</center>  | <center>0</center> | <center>4</center>  |
| 2번째 호출 | <center>4</center>  | <center>7</center>  | <center>1</center> | <center>-3</center> |
| 3번째 호출 | <center>-3</center> | <center>12</center> | <center>2</center> | <center>9</center>  |