# JavaScript 2일차

**작성일**: Wed, 17 Sep 2025 17:49:49 +0900

**원문 링크**: https://junsseok.tistory.com/16

---

<p style="text-align: center;">DOM, 함수, 객체, 이벤트</p>
<hr contenteditable="false" />
<p style="text-align: left;">1. DOM(Document Object Model) 요소 접근하기<br />-&gt; HTML 요소를 자바스크립트에서 다루려면 요소 객체를 가져와야 함 <br /><br />-&nbsp;아이디로&nbsp;가져오기</p>
<pre class="bash" id="code_1758098719272"><code>document.getElementById("id명");</code></pre>
<p style="text-align: left;"><br />단일&nbsp;요소&nbsp;반환 <br /><br />-&nbsp;태그명으로&nbsp;가져오기</p>
<pre class="bash" id="code_1758098724383"><code>document.getElementsByTagName("li");</code></pre>
<p style="text-align: left;"><br />여러&nbsp;개의&nbsp;요소를&nbsp;HTMLCollection으로&nbsp;반환 <br /><br />-&nbsp;클래스로&nbsp;가져오기</p>
<pre class="bash" id="code_1758098728400"><code>document.getElementsByClassName("클래스명");</code></pre>
<p style="text-align: left;"><br /><br />-&nbsp;네임(name&nbsp;속성)으로&nbsp;가져오기</p>
<pre class="bash" id="code_1758098731871"><code>document.getElementsByName("이름");</code></pre>
<p style="text-align: left;"><br /><br />-&nbsp;CSS&nbsp;선택자로&nbsp;가져오기</p>
<pre class="bash" id="code_1758098737128"><code>document.querySelector("선택자");     // 첫 번째 요소만
document.querySelectorAll("선택자");  // 모든 요소(NodeList)</code></pre>
<p>&nbsp;</p>
<p>2.&nbsp;함수(Function) <br />자바스크립트에서&nbsp;함수는&nbsp;코드의&nbsp;재사용&nbsp;단위입니다.</p>
<p>&nbsp;</p>
<p>- 선언적 함수</p>
<pre class="bash" id="code_1758098773895"><code>function test1() {
  console.log("선언적 함수 실행");
}</code></pre>
<p>&nbsp;</p>
<p>- 익명 함수</p>
<pre class="bash" id="code_1758098784552"><code>let test2 = function() {
  console.log("익명 함수 실행");
};</code></pre>
<p>&nbsp;</p>
<p>- 이벤트 핸들러로 사용</p>
<pre class="bash" id="code_1758098797567"><code>btn.onclick = function() {
  console.log("버튼 클릭됨");
};</code></pre>
<p>&nbsp;</p>
<p>- 매개변수</p>
<pre class="bash" id="code_1758098807351"><code>function test3(name, age, address) {
  console.log(arguments); // 전달된 모든 인자
  console.log(name, age, address);
}</code></pre>
<p>&nbsp;</p>
<p>- 콜백함수 활용</p>
<pre class="bash" id="code_1758098816951"><code>function login(info, callback) {
  setTimeout(function() {
    let user = { userId: "user01", name: "공준석" };
    callback(user);
  }, 3000);
}</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>3. 객체</p>
<p>객체는 속성(key) : 값(value) 형태로 데이터를 저장</p>
<p>&nbsp;</p>
<p>- 객체 선언 예시</p>
<pre class="bash" id="code_1758098861287"><code>const product = {
  pName: "Dry Mango",
  price: 4000,
  kind: "pickle",
  ingredient: ["mango", "sugar"],
  toString: function() {
    return this.pName + " " + this.price;
  }
};</code></pre>
<p>&nbsp;</p>
<p>- 객체 속성 접근</p>
<pre class="bash" id="code_1758098872488"><code>product.pName      // 점(.) 표기법
product["price"]   // 대괄호 표기법</code></pre>
<p>&nbsp;</p>
<p>- 객체 배열</p>
<pre class="bash" id="code_1758098881791"><code>const stdList = [
  { name: "공준석", java: 75, db: 80, front: 90 },
  { name: "공준투", java: 80, db: 90, front: 80 }
];

stdList[0].totalScore = function() {
  return this.java + this.db + this.front;
};</code></pre>
<p>&nbsp;</p>
<p>객체&nbsp;배열을&nbsp;사용하면&nbsp;다량의&nbsp;데이터를&nbsp;효율적으로&nbsp;관리할&nbsp;수&nbsp;있음.</p>
<p>&nbsp;</p>
<p>4. 이벤트</p>
<p>브라우저에서&nbsp;발생하는&nbsp;모든&nbsp;동작(click,&nbsp;keyup,&nbsp;load&nbsp;등)을&nbsp;이벤트라고&nbsp;한다. <br />이벤트가&nbsp;발생했을&nbsp;때&nbsp;실행되는&nbsp;함수를&nbsp;이벤트&nbsp;핸들러라고&nbsp;부른다.</p>
<p>&nbsp;</p>
<p>- 고전 이벤트 모델</p>
<pre class="bash" id="code_1758098934905"><code>btn1.onclick = function() {
  console.log("버튼1 클릭됨");
};
btn1.onclick = null; // 이벤트 제거</code></pre>
<p>&nbsp;</p>
<p>- 인라인 이벤트 모델</p>
<pre class="bash" id="code_1758098946704"><code>&lt;button onclick="alert('클릭됨')"&gt;버튼&lt;/button&gt;</code></pre>
<p>&nbsp;</p>
<p>3. 표준 이벤트 모델</p>
<pre class="bash" id="code_1758098955720"><code>btn.addEventListener("click", function() {
  console.log("표준 이벤트 모델 클릭");
});
btn.removeEventListener("click", handlerFunction);</code></pre>
<p>하나의&nbsp;요소에&nbsp;여러&nbsp;이벤트&nbsp;핸들러를&nbsp;등록할&nbsp;수&nbsp;있음.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>