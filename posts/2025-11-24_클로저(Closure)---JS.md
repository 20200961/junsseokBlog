# 클로저(Closure) - JS

**작성일**: Mon, 24 Nov 2025 17:47:47 +0900

**원문 링크**: https://junsseok.tistory.com/41

---

<p style="text-align: center;">학습하던중 클로저란 중요한 부분이 있어 정리하게 되었다.</p>
<hr contenteditable="false" />
<p style="text-align: center;">클로저는 함수가 선언될 때의 렉시컬 스코프(Lexical Scope)를 기억하고,<br />함수가&nbsp;스코프&nbsp;밖에서&nbsp;실행되더라도&nbsp;그&nbsp;스코프에&nbsp;접근할&nbsp;수&nbsp;있는&nbsp;기능을&nbsp;말한다.</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">한줄로</p>
<h3 style="text-align: center;"><b>함수가 만들어질 당시의 환경을 기억하는 기능!</b></h3>
<p>&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">2.&nbsp;왜&nbsp;클로저가&nbsp;생길까?&nbsp;(렉시컬&nbsp;스코프) <br /><br />자바스크립트는 렉시컬 스코프(Lexical Scope) 를 사용한다. <br />이는 함수가 어디서 선언되었는지에 따라 접근 가능한 변수가 결정된다는 의미이다.</p>
<pre class="bash" id="code_1763973803949"><code>function outer() {
    const name = "JavaScript";

    function inner() {
        console.log(name);
    }

    inner();
}

outer(); // JavaScript</code></pre>
<p>&nbsp;</p>
<p style="text-align: center;">inner&nbsp;함수는&nbsp;자신이&nbsp;선언될&nbsp;때의&nbsp;스코프인&nbsp;outer&nbsp;내부의&nbsp;변수&nbsp;name을&nbsp;계속&nbsp;기억한다.</p>
<hr contenteditable="false" />
<p style="text-align: center;">3.&nbsp;클로저의&nbsp;대표적인&nbsp;예시:&nbsp;함수&nbsp;반환 <br /><br />가장&nbsp;많이&nbsp;사용하는&nbsp;패턴은&nbsp;외부&nbsp;함수가&nbsp;내부&nbsp;함수를&nbsp;반환하는&nbsp;형태이다.</p>
<pre class="bash" id="code_1763973866037"><code>function makeCounter() {
    let count = 0;

    return function () {
        count++;
        console.log(count);
    };
}

const counter = makeCounter();

counter(); // 1
counter(); // 2
counter(); // 3</code></pre>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">여기서&nbsp;count&nbsp;변수는&nbsp;makeCounter()가&nbsp;실행된&nbsp;뒤에도&nbsp;사라지지&nbsp;않는다. <br />왜냐하면&nbsp;반환된&nbsp;내부&nbsp;함수가&nbsp;count를&nbsp;참조하고&nbsp;있기&nbsp;때문!</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><b>이것이 클로저다!!!</b></p>
<hr contenteditable="false" />
<p style="text-align: center;">4.&nbsp;클로저가&nbsp;자주&nbsp;사용되는&nbsp;상황</p>
<p style="text-align: center;"><br />(1) 상태(state) 보존<br />전역&nbsp;변수를&nbsp;쓰지&nbsp;않고&nbsp;데이터를&nbsp;은닉하면서&nbsp;상태를&nbsp;유지할&nbsp;수&nbsp;있다. <br /><br />(2) private 변수 구현<br />JavaScript에는&nbsp;기본적으로&nbsp;private&nbsp;키워드가&nbsp;없었기&nbsp;때문에,&nbsp;클로저가&nbsp;많이&nbsp;사용된다.</p>
<pre class="bash" id="code_1763973920388"><code>function BankAccount() {
    let balance = 0;

    return {
        deposit(amount) {
            balance += amount;
        },
        getBalance() {
            return balance;
        }
    };
}

const account = BankAccount();
account.deposit(1000);
console.log(account.getBalance()); // 1000</code></pre>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">balance는 외부에서 직접 접근할 수 없다</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><b>은닉된 정보!</b></p>
<hr contenteditable="false" />
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">5. 클로저가 갖는 장점</p>
<p style="text-align: center;"><br />(1) 데이터 은닉 가능 (private variable)<br />(2) 모듈 패턴 구현 가능<br />(3) 상태 유지 가능<br />(4) 캡슐화된 기능 제공</p>
<hr contenteditable="false" />
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><b>한줄 요약</b></p>
<h2 style="text-align: center;"><b>함수가 만들어질 당시의 환경을 기억하는 기능!</b></h2>
<p style="text-align: center;">&nbsp;</p>