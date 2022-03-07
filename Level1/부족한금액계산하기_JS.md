# 부족한 금액 계산하기

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/82612)

## Solution
```js
function solution(price, money, count) {
    var cnt = 1;
    while(cnt <= count) {
        money -= cnt++ * price
    }

    return money < 0 ? -money : 0;
}
```

<br>

## Clean up
```js
function solution(price, money, count) {
    const tmp = price * count * (count + 1) / 2 - money;
    return tmp > 0 ? tmp : 0;
}
```

<br>

가우스 공식을 이용.