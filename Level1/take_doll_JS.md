## 크레인 인형뽑기

```python
function solution(board, moves) {
  var answer = 0;
  let basket = []
  const N = board.length
  moves.forEach(loc => {
    for (let i = 0; i < N; i++) {
      if (board[i][loc - 1] !== 0) {
        const tmp = board[i][loc - 1]
        board[i][loc - 1] = 0
        if (basket[basket.length - 1] === tmp) {
          basket.pop()
          answer += 2
        } else {
          basket.push(tmp)
        }
        break
      }
    }
  });
  return answer;
}
```

