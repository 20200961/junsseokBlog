# JavaScript 1일차

**작성일**: Tue, 16 Sep 2025 17:30:50 +0900

**원문 링크**: https://junsseok.tistory.com/15

---

<p>1. JavaScript 변수</p>
<p>- var <br />오래된 방식, 중복 선언 가능 &rarr; 오류의 원인이 되므로 지금은 사용하지 않음<br />- let <br />블록 단위 스코프, 중복 선언 불가 &rarr; 일반 변수 선언에 사용<br />- const <br />상수,&nbsp;한&nbsp;번&nbsp;할당하면&nbsp;변경&nbsp;불가</p>
<p>&nbsp;</p>
<p>- 변수이름 규칙 <br />1)&nbsp;문자,&nbsp;숫자&nbsp;모두&nbsp;가능&nbsp;(단,&nbsp;숫자로&nbsp;시작&nbsp;X) <br />2)&nbsp;특수문자는&nbsp;_&nbsp;,&nbsp;$&nbsp;만&nbsp;가능 <br />3)&nbsp;키워드&nbsp;사용&nbsp;불가&nbsp;(예:&nbsp;let,&nbsp;const,&nbsp;var) <br /><br />일반적으로 <br />-&nbsp;변수명,&nbsp;함수명&nbsp;&rarr;&nbsp;camelCase <br />-&nbsp;HTML&nbsp;속성명,&nbsp;CSS&nbsp;class/id&nbsp;&rarr;&nbsp;kebab-case</p>
<p>&nbsp;</p>
<p>여섯&nbsp;개의&nbsp;원시타입(Primitive)&nbsp;+&nbsp;하나의&nbsp;Object&nbsp;타입 <br />1)&nbsp;Number <br />2)&nbsp;String <br />3)&nbsp;Boolean <br />4)&nbsp;undefined <br />5)&nbsp;null <br />6)&nbsp;Symbol <br />7) Object (Array, Function, Object 등)</p>
<p>&nbsp;</p>
<p>2. Number</p>
<pre class="bash" id="code_1758010976580"><code>const age2 = 55;
const temp = -10.5;
const pi = 3.14;

console.log(age2, temp, pi);
console.log(typeof age2); // number
console.log(typeof temp); // number
console.log(typeof pi);   // number

console.log(typeof Infinity);   // number
console.log(typeof -Infinity);  // number</code></pre>
<p>== : 값만 비교(자동형 변환)<br />===&nbsp;:&nbsp;값&nbsp;+&nbsp;타입&nbsp;비교&nbsp;(자동&nbsp;형&nbsp;변환&nbsp;X)</p>
<p>&nbsp;</p>
<p>3. String &amp; 비교 연산</p>
<pre class="bash" id="code_1758010991324"><code>const name3 = "최지원 66살";
const age3 = 55;

console.log(typeof name3);  // string
console.log(age3 == "55");  // true (값만 비교)
console.log(age3 === "55"); // false (타입까지 비교)</code></pre>
<p>&nbsp;</p>
<p>4. Boolean</p>
<pre class="bash" id="code_1758011009012"><code>const isTrue2 = true;
const isFalse = false;
console.log(typeof isTrue2); // boolean</code></pre>
<p>&nbsp;</p>
<p>5. undefined</p>
<pre class="bash" id="code_1758011021388"><code>let num2;
console.log(num2);        // undefined
console.log(typeof num2); // undefined</code></pre>
<p>변수를&nbsp;선언만&nbsp;하고&nbsp;값을&nbsp;할당하지&nbsp;않으면&nbsp;자동으로&nbsp;undefined</p>
<p>&nbsp;</p>
<p>6. null</p>
<pre class="bash" id="code_1758011102284"><code>let init = 10;
init = null;
console.log(init);</code></pre>
<p>null은 값이 없음을 표시할 때 사용</p>
<p>&nbsp;</p>
<p>7. Symbol</p>
<pre class="bash" id="code_1758011125724"><code>const tmp1 = '1';
const tmp2 = '1';
console.log("tmp1 === tmp2 : ", tmp1 === tmp2); // true

const symbol1 = Symbol('1');
const symbol2 = Symbol('1');
console.log("symbol1 === symbol2 : ", symbol1 === symbol2); // false</code></pre>
<p>Symbol&nbsp;은&nbsp;고유한&nbsp;값을&nbsp;만들&nbsp;때&nbsp;사용.&nbsp;(중복&nbsp;X)</p>
<p>&nbsp;</p>
<p>8. Object 객체</p>
<pre class="bash" id="code_1758011192884"><code>const jun = {
    name: "공준석",
    age: 25,
    address: "경기도 성남시",
    job: "학생",
}

console.log(jun.name);     // 공준석
console.log(jun.address);  // 경기도 성남시
jun.age = 15;              // 값 수정 가능
console.log(jun.age);      // 15
console.log(typeof jun);   // object</code></pre>
<p>key : value 구조</p>
<p>&nbsp;</p>
<p>9. Array 배열</p>
<pre class="bash" id="code_1758011222084"><code>const arr = ["초록색", "노란색"];
arr.push("빨간색");
arr.push("파란색");
arr.push(50);
console.log(arr);

console.log(arr.pop()); // 마지막 요소 제거 (50)
console.log(arr);       // [ '초록색', '노란색', '빨간색', '파란색' ]

console.log(arr[0]);  // 초록색
console.log(arr[2]);  // 빨간색
console.log(arr[10]); // undefined</code></pre>
<p>배열은 인덱스(0부터 시작)로 접근</p>
<p>&nbsp;</p>
<p>10. 함수(Function)</p>
<pre class="bash" id="code_1758011250020"><code>// 함수 선언식
function test1() {
    console.log("test1 함수 실행");
}

// 함수 표현식
const test3 = function() {
    console.log("test2 함수 실행");
}

test1();
test3();</code></pre>
<p>&nbsp;</p>
<p>- 매개변수 &amp; arguments</p>
<pre class="bash" id="code_1758011274836"><code>let test4 = function(name){
    console.log(arguments); // 전달받은 모든 인자
    console.log("test4 함수 실행");
    console.log(name);
}

test4();
test4("공준석");
test4("공준석", 25, "경기도 성남시");</code></pre>
<p>JS는&nbsp;오버로딩을&nbsp;지원&nbsp;X&nbsp;&rarr;&nbsp;매개변수&nbsp;개수가&nbsp;달라도&nbsp;동일한&nbsp;함수로&nbsp;인식</p>
<p>&nbsp;</p>
<p>11. 화살표&nbsp;함수&nbsp;(Arrow&nbsp;Function)</p>
<pre class="bash" id="code_1758011323524"><code>let test5 = () =&gt; 200;
console.log(test5()); // 200</code></pre>
<p>짧고 간결한 함수 표현식. 콜백 함수 작성 시 자주 사용</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<p>배운점 &amp; 느낀점 :&nbsp;</p>
<p>이번에&nbsp;JavaScript&nbsp;기초를&nbsp;정리하면서&nbsp;var,&nbsp;let,&nbsp;const의&nbsp;차이와&nbsp;자료형의&nbsp;특성을&nbsp;다시&nbsp;확인할&nbsp;수&nbsp;있었다.&nbsp;특히&nbsp;==와&nbsp;===의&nbsp;차이가&nbsp;중요하다는&nbsp;걸&nbsp;느꼈고,&nbsp;null과&nbsp;undefined의&nbsp;의미도&nbsp;확실히&nbsp;구분할&nbsp;수&nbsp;있었다.&nbsp;객체와&nbsp;배열이&nbsp;데이터를&nbsp;다루는&nbsp;데&nbsp;얼마나&nbsp;유용한지도&nbsp;알게&nbsp;되었고,&nbsp;함수가&nbsp;1급&nbsp;객체라는&nbsp;점이&nbsp;인상&nbsp;깊었다.&nbsp;전반적으로&nbsp;JavaScript가&nbsp;자유롭고&nbsp;유연한&nbsp;언어라서&nbsp;주의할&nbsp;점도&nbsp;많지만,&nbsp;잘&nbsp;활용하면&nbsp;굉장히&nbsp;편리하다는&nbsp;걸&nbsp;느꼈다.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>