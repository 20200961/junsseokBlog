# JavaScript 5일차

**작성일**: Mon, 22 Sep 2025 16:47:39 +0900

**원문 링크**: https://junsseok.tistory.com/19

---

<p style="text-align: center;">Hoisting, Scope, Closuer, Array Function, 부트스트랩 학습</p>
<hr contenteditable="false" />
<p style="text-align: left;">1. Hoisting : 자바스크립트 엔진이 코드를 실행하기 전에 변수와 함수 선언을 메모리에 미리 등록하는 동작한다</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">- var는&nbsp;선언과&nbsp;동시에&nbsp;undefined로&nbsp;초기화되므로&nbsp;선언&nbsp;전에&nbsp;접근&nbsp;가능.</p>
<pre class="bash" id="code_1758525278676"><code>console.log("선언 전 : ", name1); // undefined
var name1 = "junseok";
console.log("선언 후 : ", name1); // junseok</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>- let / const는 TDZ때문에 선언 전 접근 시 오류가 발생한다.</p>
<pre class="bash" id="code_1758525385236"><code>let name2 = "junseok";
const name3 = 'jisu';
console.log("선언 후 : ", name2); // error
console.log("선언 후 : ", name3); // error</code></pre>
<p>let, const는 TDZ 영역에 있다가 선언 시점에 메모리에 할당되므로 호이스팅이 없는 것처럼 동작</p>
<p>&nbsp;</p>
<p>- 함수 선언문은 전체가 메모리에 등록되므로 코드 어디서든 호출 가능하다.</p>
<pre class="bash" id="code_1758525834403"><code>hello(); // 정상 호출

function hello(){
    console.log("안녕하세요.");
}</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>2. Scope : 변수와&nbsp;함수가&nbsp;접근할&nbsp;수&nbsp;있는&nbsp;유효&nbsp;범위이다. <br /><br />(1)전역&nbsp;스코프:&nbsp;코드&nbsp;어디서든&nbsp;접근&nbsp;가능</p>
<pre class="bash" id="code_1758525897867"><code>// 전역 변수
var globalVar = "전역 변수";

function showGlobal() {
    console.log(globalVar); // 전역에서 접근 가능
}

showGlobal();
console.log(globalVar); // 함수 밖에서도 접근 가능</code></pre>
<p>함수&nbsp;내부에서&nbsp;변수가&nbsp;있으면&nbsp;그&nbsp;값을&nbsp;사용,&nbsp;없다면&nbsp;전역을&nbsp;참조</p>
<p>&nbsp;</p>
<p><br />(2)함수&nbsp;스코프:&nbsp;함수&nbsp;내부에서만&nbsp;유효&nbsp;(var)</p>
<pre class="javascript" id="code_1758526099309"><code>function funcScopeExample() {
    var funcVar = "함수 내부 변수";
    console.log(funcVar); // 함수 안에서 접근 가능
}

// console.log(funcVar); // error : 함수 밖에서는 보이지 않음
funcScopeExample();</code></pre>
<p><br />(3)블록&nbsp;스코프:&nbsp;{}&nbsp;블록&nbsp;내부에서만&nbsp;유효&nbsp;(let,&nbsp;const)</p>
<pre class="bash" id="code_1758526073059"><code>if (true) {
    let blockLet = "블록 스코프(let)";
    const blockConst = "블록 스코프(const)";
    console.log(blockLet);   // 블록 내부에서 접근 가능
    console.log(blockConst); // 블록 내부에서 접근 가능
}

// console.log(blockLet);   // 에러
// console.log(blockConst); // 에러</code></pre>
<p><br />(4)렉시컬&nbsp;스코프:&nbsp;함수가&nbsp;선언된&nbsp;위치&nbsp;기준으로&nbsp;스코프&nbsp;결정</p>
<pre class="bash" id="code_1758525925203"><code>var lexicalVar = "전역 변수";

function outer() {
    var lexicalVar = "outer 함수 변수";
    function inner() {
        console.log("inner:", lexicalVar);
    }

    return inner;
}

const innerFunc = outer();
innerFunc(); // 실행</code></pre>
<p>&nbsp;</p>
<p>(5) var&nbsp;vs&nbsp;let&nbsp;(for문)</p>
<pre class="bash" id="code_1758526163722"><code>var i = 1000;
for (var i = 0; i &lt; 10; i++) {
    console.log(i);
}
console.log("i = " + i);

let j = 1000;
for (let j = 0; j &lt; 10; j++) {
    console.log(j);
}
console.log("j = " + j);</code></pre>
<p>var는 함수 스코프 &rarr; for문 안에서 새 변수가 안 생기고 전역 i가 변경<br />let은 블록 스코프 &rarr; for문 안에서만 유효한 j를 생성하고, 전역 j는 유지</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>3.&nbsp;Closure&nbsp;:&nbsp;외부&nbsp;함수의&nbsp;변수를&nbsp;내부&nbsp;함수가&nbsp;기억해서&nbsp;사용하는&nbsp;것이다.</p>
<p>&nbsp;</p>
<p>예시)</p>
<pre class="bash" id="code_1758526476890"><code>function getCounter(){
    let count = 0; // 외부 함수 변수

    function increase(){
        count++;
        return count;
    }

    return increase;
}

const run = getCounter();
console.log(run()); // 1
console.log(run()); // 2
console.log(run()); // 3</code></pre>
<p>count는 외부에서 직접 접근 불가<br />하지만 increase()를 통해서만 접근 가능 &rarr; 캡슐화, 상태 유지</p>
<p>&nbsp;</p>
<p>예시)</p>
<pre class="bash" id="code_1758526511362"><code>function out(outValue){
    function inner(innerValue){
        console.log("outValue : " + outValue);
        console.log("innerValue : " + innerValue);
    }
    return inner;
}

const printer = out("외부함수");
printer("내부함수");
--------------------------결과-------------------------
// outValue : 외부함수
//innerValue : 내부함수</code></pre>
<p>outValue는 out() 실행이 끝난 후에도 inner()가 기억</p>
<p>&nbsp;</p>
<p>이벤트 핸들러)</p>
<pre class="bash" id="code_1758526589697"><code>function attachOnce(el, msg){
    let clicked = false;

    el.addEventListener("click", function(){
        if(clicked) return;
        clicked = true;
        console.log(msg);
    });
}</code></pre>
<p>버튼을&nbsp;여러&nbsp;번&nbsp;눌러도&nbsp;처음&nbsp;한&nbsp;번만&nbsp;실행되는&nbsp;이벤트&nbsp;핸들러</p>
<p>&nbsp;</p>
<p>4. 배열, 객체, 반복문</p>
<p>&nbsp;</p>
<p>배열 메서드)</p>
<pre class="bash" id="code_1758526666513"><code>let members = ["최지원","김지원","이지원","박지원","정지원","황지원"];

members.push("신지원");  // 끝에 추가
console.log(members);

console.log(members.splice(1, 3)); // 인덱스 1부터 3개 삭제
console.log(members);

console.log(members.slice(0, 3)); // 복사 (원본 영향 X)</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>스프레드 연산자)</p>
<pre class="bash" id="code_1758526692986"><code>let members2 = [...members, "신지원"];
console.log(members2);

let choi = { name: "jiwon", age: 24, gender: "남" };

// 값 수정
choi = { ...choi, gender: "여" };

// 값 추가
choi = { ...choi, address: "경기도 광명시" };</code></pre>
<p>&nbsp;</p>
<p>비구조화 할당)</p>
<pre class="bash" id="code_1758526709339"><code>const [cho, kim, lee] = members;
console.log(cho, kim, lee);

const {name, age} = choi;
console.log(name, age);

const {name: userName, age: userAge} = choi;
console.log(userName, userAge);</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>반복문)</p>
<pre class="bash" id="code_1758526770706"><code>let stdList = [
    {name: "최지원", java: 75, db: 80, front: 90},
    {name: "최지투", java: 80, db: 90, front: 80},
];

// for문
for(let i=0; i&lt;stdList.length; i++){
    console.log(stdList[i]);
}

// for..of (값 중심)
for(const std of stdList){
    console.log(std);
}

// for..in (인덱스 / 객체 key)
for(const i in stdList){
    console.log(i + "번째 : ", stdList[i]);
}

// forEach (콜백 기반)
stdList.forEach(function(v, i, a){
    console.log(v, i, a);
});</code></pre>
<hr contenteditable="false" />
<p>&nbsp;</p>
<p>5. 부트 스트랩(Bootstrap) : Bootstrap은&nbsp;CSS,&nbsp;JS를&nbsp;따로&nbsp;작성하지&nbsp;않아도&nbsp;기본&nbsp;제공되는&nbsp;클래스와&nbsp;컴포넌트를&nbsp;활용해&nbsp;쉽게&nbsp;UI를&nbsp;꾸밀&nbsp;수&nbsp;있다.</p>
<p>&nbsp;</p>
<p>- 기본 구조 (HTML + Bootstrap 불러오기) : 공식 CDN을 이용하면 설치 없이 Bootstrap의 CSS와 JS 라이브러리를 불러올 수 있다.</p>
<pre class="bash" id="code_1758527045969"><code>&lt;!-- Latest compiled and minified CSS --&gt;
&lt;link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"&gt;

&lt;!-- Latest compiled JavaScript --&gt;
&lt;script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"&gt;&lt;/script&gt;</code></pre>
<p>&nbsp;</p>
<p>-&nbsp;게시판&nbsp;테이블&nbsp;만들기 <br />게시판은&nbsp;table&nbsp;태그와&nbsp;Bootstrap의&nbsp;table,&nbsp;table-striped,&nbsp;table-active&nbsp;클래스를&nbsp;활용한다</p>
<pre class="bash" id="code_1758527076833"><code>&lt;table class="table table-striped pp-table"&gt;
    &lt;thead class="table-active"&gt;
        &lt;tr&gt;
            &lt;th&gt;글번호&lt;/th&gt;
            &lt;th&gt;제목&lt;/th&gt;
            &lt;th&gt;작성자&lt;/th&gt;
            &lt;th&gt;조회수&lt;/th&gt;
            &lt;th&gt;작성일&lt;/th&gt;
        &lt;/tr&gt;
    &lt;/thead&gt;
    &lt;tbody&gt;
        &lt;tr&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;첫번째 게시글&lt;/td&gt;
            &lt;td&gt;user01&lt;/td&gt;
            &lt;td&gt;124&lt;/td&gt;
            &lt;td&gt;2025-02-05&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
            &lt;td&gt;2&lt;/td&gt;
            &lt;td&gt;두번째 게시글&lt;/td&gt;
            &lt;td&gt;user01&lt;/td&gt;
            &lt;td&gt;124&lt;/td&gt;
            &lt;td&gt;2025-07-12&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
            &lt;td&gt;3&lt;/td&gt;
            &lt;td&gt;세번째 게시글&lt;/td&gt;
            &lt;td&gt;user02&lt;/td&gt;
            &lt;td&gt;11&lt;/td&gt;
            &lt;td&gt;2025-02-23&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
            &lt;td&gt;4&lt;/td&gt;
            &lt;td&gt;네번째 게시글&lt;/td&gt;
            &lt;td&gt;user05&lt;/td&gt;
            &lt;td&gt;423&lt;/td&gt;
            &lt;td&gt;2025-05-18&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
            &lt;td&gt;5&lt;/td&gt;
            &lt;td&gt;다섯번째 게시글&lt;/td&gt;
            &lt;td&gt;user06&lt;/td&gt;
            &lt;td&gt;23&lt;/td&gt;
            &lt;td&gt;2025-03-18&lt;/td&gt;
        &lt;/tr&gt;
    &lt;/tbody&gt;
&lt;/table&gt;</code></pre>
<p>줄무늬 효과가 들어간 게시판</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>3.&nbsp;로그인&nbsp;버튼&nbsp;&amp;&nbsp;모달창&nbsp;구현하기 <br />버튼에&nbsp;data-bs-toggle="modal"과&nbsp;data-bs-target="#모달ID"&nbsp;속성을&nbsp;추가</p>
<pre class="bash" id="code_1758527133641"><code>&lt;button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#login-modal"&gt;
    로그인
&lt;/button&gt;
&lt;div class="modal" id="login-modal"&gt;
    &lt;div class="modal-dialog"&gt;
        &lt;div class="modal-content"&gt;

            &lt;!-- Modal Header --&gt;
            &lt;div class="modal-header"&gt;
                &lt;h4 class="modal-title"&gt;KH 로그인&lt;/h4&gt;
                &lt;button type="button" class="btn-close" data-bs-dismiss="modal"&gt;&lt;/button&gt;
            &lt;/div&gt;

            &lt;!-- Modal Body --&gt;
            &lt;div class="modal-body"&gt;
                &lt;form action="나의 서버 url"&gt;
                    &lt;div class="mb-3 mt-3"&gt;
                        &lt;label for="user-id" class="form-label"&gt;아이디 :&lt;/label&gt;
                        &lt;input type="text" class="form-control" id="user-id" placeholder="ID를 입력하세요." name="userId"&gt;
                    &lt;/div&gt;
                    &lt;div class="mb-3"&gt;
                        &lt;label for="pwd" class="form-label"&gt;비밀번호 :&lt;/label&gt;
                        &lt;input type="password" class="form-control" id="pwd" placeholder="비밀번호를 입력하세요." name="userPwd"&gt;
                    &lt;/div&gt;
                    &lt;div class="form-check mb-3"&gt;
                        &lt;label class="form-check-label"&gt;
                            &lt;input class="form-check-input" type="checkbox" name="remember"&gt; ID 저장하기
                        &lt;/label&gt;
                    &lt;/div&gt;
                    &lt;button type="submit" class="btn btn-primary pull-width"&gt;로그인&lt;/button&gt;
                &lt;/form&gt;
            &lt;/div&gt;

        &lt;/div&gt;
    &lt;/div&gt;
&lt;/div&gt;</code></pre>
<p>-&nbsp;modal-header&nbsp;:&nbsp;모달창&nbsp;제목과&nbsp;닫기&nbsp;버튼. <br />-&nbsp;modal-body&nbsp;:&nbsp;실제&nbsp;로그인&nbsp;폼이&nbsp;들어가는&nbsp;부분. <br />-&nbsp;form-control&nbsp;:&nbsp;Bootstrap에서&nbsp;제공하는&nbsp;입력창&nbsp;스타일. <br />-&nbsp;btn&nbsp;btn-primary&nbsp;:&nbsp;파란색&nbsp;기본&nbsp;버튼&nbsp;스타일.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<p>배운점 &amp; 느낀점</p>
<p>자바스크립트의&nbsp;Hoisting,&nbsp;Scope,&nbsp;Closure를&nbsp;공부하면서&nbsp;코드&nbsp;실행&nbsp;원리를&nbsp;이해할&nbsp;수&nbsp;있었다.&nbsp;var,&nbsp;let,&nbsp;const의&nbsp;차이와&nbsp;Closure를&nbsp;통한&nbsp;상태&nbsp;유지,&nbsp;캡슐화&nbsp;개념이&nbsp;실무에서&nbsp;유용하게&nbsp;쓰일&nbsp;수&nbsp;있다는&nbsp;점이&nbsp;인상&nbsp;깊었다.&nbsp;그리고&nbsp;배열과&nbsp;객체&nbsp;메서드,&nbsp;스프레드&nbsp;연산자,&nbsp;비구조화&nbsp;할당,&nbsp;반복문을&nbsp;연습하며&nbsp;데이터를&nbsp;효율적으로&nbsp;가공하는&nbsp;방법을&nbsp;익혔다.&nbsp;이&nbsp;과정을&nbsp;통해&nbsp;단순&nbsp;문법&nbsp;암기보다&nbsp;상황에&nbsp;맞는&nbsp;활용이&nbsp;중요하다는&nbsp;걸&nbsp;느꼈다. <br />Bootstrap을&nbsp;사용해&nbsp;테이블과&nbsp;모달을&nbsp;구현하면서&nbsp;UI를&nbsp;빠르고&nbsp;간편하게&nbsp;구성할&nbsp;수&nbsp;있다는&nbsp;장점을&nbsp;체감했다.&nbsp;이번&nbsp;학습을&nbsp;통해&nbsp;기본&nbsp;원리부터&nbsp;실전&nbsp;UI&nbsp;구현까지&nbsp;폭넓은&nbsp;경험을&nbsp;얻을&nbsp;수&nbsp;있었다.</p>