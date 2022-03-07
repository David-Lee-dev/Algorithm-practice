# 최소직사각형

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/86491)

## Solution
```js
function solution(sizes) {
	var answer = [0, 0];
	sizes.forEach(size => {
		size.sort((a, b) => b - a)
		answer[0] = answer[0] > size[0] ? answer[0] : size[0];
		answer[1] = answer[1] > size[1] ? answer[1] : size[1];		
	});
	return answer[0] * answer[1];
}
```
<br>

## Cleanup
```js
function solution(sizes) {
    const [hor, ver] = sizes.reduce(([h, v], [a, b]) => [Math.max(h, Math.max(a, b)), Math.max(v, Math.min(a, b))], [0, 0])
    return hor * ver;
}
```