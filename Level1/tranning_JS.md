# 체육복

>[문제 출처](https://programmers.co.kr/learn/courses/30/lessons/42862)

## Solution
```js
function solution(n, lost, reserve) {
  let rent = [];
  const more = reserve.filter(el => !lost.includes(el)).sort((a, b) => a - b)
  const need = lost.filter(el => !reserve.includes(el)).sort((a, b) => a - b)
  need.forEach(el => {
    if (el - 1 > 0 && more.includes(el - 1) && !rent.includes(el - 1)) {
      rent.push(el - 1)
    } else if (el + 1 <= n && more.includes(el + 1) && !rent.includes(el + 1)) {
      rent.push(el + 1)
    }
  });
  return n - (need.length - rent.length);
}
```


## Clean-up
> BYUNGI님의 코드

```js
function solution(n, lost, reserve) {      
    return n - lost.filter(a => {
        const b = reserve.find(r => Math.abs(r-a) <= 1)
        if(!b) return true
        reserve = reserve.filter(r => r !== b)
    }).length
}
```