# 신규 아이디 추천

>>[문제출처](https://programmers.co.kr/learn/courses/30/lessons/72410)
>
>## Solution
>```js
>function solution(new_id) {
>  var answer = ''
>  let answer_tmp = ''
>  //step 1, step 2
>  for (let word of new_id) {
>    let check = false
>    for (let sw of '-_.0123456789') {
>      if (word === sw) {
>        check = true
>      }
>    }
>    if (word.charCodeAt(0) >= 97 && word.charCodeAt(0) <= 122) {
>      answer_tmp += word
>    } else if (word.charCodeAt(0) >= 65 && word.charCodeAt(0) <= 90) {
>      answer_tmp += String.fromCharCode(word.charCodeAt(0) + 32)
>    } else if (check) {
>      answer_tmp += word
>    }
>  }
>  answer = answer_tmp
>  answer_tmp = ''
>  //step 3
>
>  let tmp = ''
>  for (let word of answer) {
>    if (word === '.') {
>      tmp = word
>    } else {
>      answer_tmp += tmp + word
>      tmp = ''
>    }
>  }
>  if (tmp === '.') {
>    answer = answer_tmp + tmp
>  } else {
>    answer = answer_tmp
>  }
>  answer_tmp = ''
>  //step 4
>  if (answer[0] === '.') {
>    for (let i = 1; i < answer.length; i++) {
>      answer_tmp += answer[i]
>    }
>    answer = answer_tmp
>    answer_tmp = ''
>  }
>  if (answer[answer.length - 1] === '.') {
>    for (let i = 0; i < answer.length - 1; i++) {
>      answer_tmp += answer[i]
>    }
>    answer = answer_tmp
>    answer_tmp = ''
>  }
>  //step 5, step 6
>  if (answer.length === 0) {
>    answer = 'a'
>  } else if (answer.length > 15) {
>    for (let i = 0; i < 15; i++) {
>      answer_tmp += answer[i];
>    }
>  }
>  if (answer_tmp !== '') {
>    answer = answer_tmp
>    answer_tmp = ''
>  }
>  //step 7
>  if (answer.length < 3) {
>    while (answer.length < 3) {
>      answer += answer[answer.length - 1]
>    }
>  }
>  if (answer[0] === '.') {
>    for (let i = 1; i < answer.length; i++) {
>      answer_tmp += answer[i]
>    }
>    answer = answer_tmp
>    answer_tmp = ''
>  }
>  if (answer[answer.length - 1] === '.') {
>    for (let i = 0; i < answer.length - 1; i++) {
>      answer_tmp += answer[i]
>    }
>    answer = answer_tmp
>    answer_tmp = ''
>  }
>  return answer;
>}
>solution("abcdefghijklmn.p")
>```
>>
>- 1단계 : new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
>- 2단계 : new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
>- 3단계 : new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
>- 4단계 : new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
>- 5단계 : new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
>- 6단계 : new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
>     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
>- 7단계 : new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
>
>위의 단계를 하나씩 차례대로 만들었고, 처음과 끝에는 ``.``를 사용할 수 없다는 제약 사항을 지키기 위해 마지막에 4단계 과정을 한 번더 진행했다.
>
><br>
>
>## Clean-up
>```js
>function solution(new_id) {
>  var answer = ''
>  let answer_tmp = ''
>  //step 1  
>  new_id = new_id.toLowerCase()
>  
>  //step 2
>  new_id = new_id.match(/\w|[._-]/g).join('')
>
>  //step 3
>  new_id = new_id.split(/\.{2,}/).join('.')
>
>  //step 4
>  new_id = new_id.replace(/^\./, '')
>  new_id = new_id.replace(/\.$/, '')
>
>  //step 5, step 6
>  if (new_id.length === 0) {
>    new_id = 'a'
>  } else if (new_id.length > 15) {
>    new_id = new_id.slice(0, 15)
>  }
>  new_id = new_id.replace(/\.$/, '')
>  //step 7
>  if (answer.length < 3) {
>    while (answer.length < 3) {
>      answer += answer.slice(-1)
>    }
>  }
>  return answer;
>}
>```
>JS에서 제공하는 메서드를 적극적으로 활용하면 지나치게 복잡한 코드가 훨씬 간결하게 정리된다.
>
>### step 1
>- ``toLowerCase()``메서드는 문자열에서 대문자 알파벳에 해당하는 문자를 전부 소문자로 바꾸어 새로운 문자열을 반환하는 메서드이다.
>
>>[``toLowerCase()`` 참고](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
>
>### step 2
>- ``match``메서드는 정규표현식에 해당하는 문자들을 모아 배열로 반환해준다.
>- ``match``를 통해 제약사항에 해당하는 모든 문자들을 배열에 담은뒤
>- ``join``메서드는 배열의 항목 사이사이에 원하는 문자열을 삽입하여 문자열로 반환하는 메서드이다.
>
>>[``match`` 참고](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
>>[``join`` 참고](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
>>[``정규 표현식`` 참고](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
>
>### step 3
>- ``split``메서드는 정규표현식에 해당하는 문자열을 기준으로 분리해서 배열로 반환해주는 메서드이다.
>- 입력이 ``"...!@BaT#*..y.abcdefghijklm"``일 때, 앞의 과정을 거쳐 ``"...bat..y.abcdefghijklm"``와 같이 된다. ``split``메서드를 사용하면 아래와 같은 배열을 반환한다.
>>![](https://images.velog.io/images/main_string/post/237ee8ea-a2ca-42fa-ba3b-7b582cc8b2ee/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202021-09-14%20212656.png)
>
>
>- 정규표현식은 ``.``이 두 개이상 반복되는 문자열을 의미하며, 그대로 ``join``하게 되면 중복된 ``.``을  하나로 만드는 것이 아닌 제거하게 되므로 ``.``을 기준으로 ``join``을 사용한다.
>
>>[``split`` 참고](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
>
>### step 4
>- ``replace``메서드는 정규표현식에 해당하는 문자열을 다른 문자열로 치환하여 반환해주는 메서드이다.
>- 정규표현식은 맨 앞과 맨 뒤에 ``.``이 있는 것을 의미한다.
>
>>[``replace`` 참고](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
>
>### step 6
>- ``slice``메서드는 배열이나 문자열과 같이 indexing이 가능한 데이터를 인덱스를 기준으로 잘라서 반환해준다. 두 개의 인자를 가지고 있는데 **앞에 있는 인덱스는 포함, 뒤에 있는 인덱스는 미포함한다. 즉, 이상, 미만을 의미**
>
>>[``문자열 slice`` 참고](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
>
>### step 7
>- 6단계와 마찬가지로 ``slice``메서드를 사용했다. ``-1``만 인자로 사용하여 맨 뒤의 글자부터 끝까지 해당되게 했다. 즉 맨 뒤의 글자만 잘라온다.

