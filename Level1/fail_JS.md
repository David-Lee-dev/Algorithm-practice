# 실패율

>[문제 출처](https://programmers.co.kr/learn/courses/30/lessons/42889)

## Solution
```js
function solution(N, stages) {
  let tmp = []
  let nonClearPlayer = Array.from({
    length: N
  }, () => 0)
  let stageCount = Array.from({
    length: N
  }, () => 0)

  stages.forEach(playerStage => {
    if (playerStage <= N) nonClearPlayer[playerStage - 1]++
    for (let i = 1; i <= playerStage; i++) {
      if (i <= N) stageCount[i - 1]++
    }
  })

  for (let i = 0; i < N; i++) {
    const dict = {}
    dict["num"] = i + 1
    dict["rate"] = nonClearPlayer[i] / stageCount[i]
    tmp.push(dict)
  }
  return tmp.sort((a, b) => b.rate - a.rate).map(el => el["num"])
}
```

## Clean-up

```js
function solution(N, stages) {
    let result = [];
    for(let i=1; i<=N; i++){
        let reach = stages.filter((x) => x >= i).length;
        let curr = stages.filter((x) => x === i).length;
        result.push([i, curr/reach]);
    }
    result.sort((a,b) => b[1] - a[1]);
    return result.map((x) => x[0]);
}
```
