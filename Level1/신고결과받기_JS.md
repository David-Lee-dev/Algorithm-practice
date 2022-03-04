# 신고 결과 받디

>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/92334)

## Solution
```js
function solution(id_list, report, k) {
	const report_obj = {}
	for(const cont of report) {
		const tmp = cont.split(" ");
		if(report_obj[tmp[1]] !== undefined) {
			if(!report_obj[tmp[1]].includes(tmp[0]))
				report_obj[tmp[1]].push(tmp[0])
		}
		else report_obj[tmp[1]] = [tmp[0]]
	}

	const id_list_obj = {}
	id_list.forEach(id => {
		id_list_obj[id] = 0
	});

	for(const key in report_obj) {
		const arr = report_obj[key]
		if(arr.length >= k) {
			arr.forEach(el => id_list_obj[el]++)
		}
	}
	const answer = id_list.map(el => id_list_obj[el])
	return answer;
}
```
<br>

## Cleanup
```js
function solution(id_list, report, k) {
	const reports = [... new Set(report)].map(el => el.split(" "));
	const counts = new Map();
	for(const r of reports) {
		counts.set(r[1], counts.get(r[1])+1||1)
	}
	const mailing = new Map();
	for(const r of reports) {
		if(counts.get(r[1]) >= k) {
			mailing.set(r[0], mailing.get(r[0])+1||1)
		}
	}
	return id_list.map(el => mailing.get(el)||0);
}
```