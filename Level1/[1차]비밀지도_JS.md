# [1차]비밀지도

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/17681)

## Solution
```js
function solution(n, arr1, arr2) {
  bi_arr1 = [];
  bi_arr2 = [];
  combi = [];

  arr1.forEach(el => bi_arr1.push(el.toString(2).padStart(n,'0')));
  arr2.forEach(el => bi_arr2.push(el.toString(2).padStart(n,'0')));

  for(let i=0; i<n; i++) {
    let string = ""
    for(let j=0; j<n; j++) {
      string += bi_arr1[i][j] === "1" || bi_arr2[i][j] === "1" ? "#" : " "
    }
    combi.push(string);
  }

  return combi;
}
```