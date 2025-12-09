# 자바의 예외 처리(Exception) 구조

**카테고리**: 면접대비

**작성일**: Sat, 29 Nov 2025 15:33:50 +0900

**원문 링크**: https://junsseok.tistory.com/47

---

<p style="text-align: center;">자바의 예외처리 구조</p>
<hr contenteditable="false" />
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><b>자바의 예외는 Throwable 클래스를 최상위로 하여 Error와 Exception으로 구분된다</b></p>
<hr contenteditable="false" />
<h3 style="text-align: left;">1. ERROR</h3>
<p style="text-align: left;">&nbsp;</p>
<p>시스템 레벨의 심각한 오류이며 개발자가 할 수 없는 오류이다.</p>
<p>예: OutOfMemoryError, StackOverflowError</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<h3 style="text-align: left;">2. Exception</h3>
<p>프로그램 실행 중 발생하는 예외 상황이며 개발자가 처리 가능하다.<br />두&nbsp;종류로&nbsp;나뉜다. <br /><br />(1) Checked Exception<br />컴파일&nbsp;시점에&nbsp;처리를&nbsp;강제하며&nbsp;반드시&nbsp;try-catch&nbsp;또는&nbsp;throws&nbsp;필요 <br />예:&nbsp;IOException,&nbsp;SQLException <br /><br />(2) Unchecked Exception<br />실행&nbsp;시점(Runtime)에&nbsp;발생하며&nbsp;처리를&nbsp;강제&nbsp;하지&nbsp;않아도&nbsp;된다. <br />(주로 개발자 실수)<br />예:&nbsp;NullPointerException,&nbsp;ArrayIndexOutOfBoundsException</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">예외처리 방법</h3>
<p>1. try - catch - finally</p>
<pre class="bash" id="code_1764316125364"><code>try {
    int a = 10 / 0;   // 예외 발생
    System.out.println("실행 안 됨");
} catch (ArithmeticException e) {
    System.out.println("0으로 나눌 수 없습니다.");
} finally {
    System.out.println("예외 발생 여부와 상관없이 실행");
}

// 실행결과
//0으로 나눌 수 없습니다.
//예외 발생 여부와 상관없이 실행</code></pre>
<p>&nbsp;</p>
<p>-&gt; 예외를&nbsp;직접&nbsp;처리하고,&nbsp;finally에서&nbsp;자원&nbsp;해제</p>
<p>&nbsp;</p>
<p>- try : 예외 발생 가능 코드</p>
<p>- catch : 예외 발생 시 처리</p>
<p>- finally : 무조건 실행 (파일 닫기, DB 연결 해제)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>2. throws</p>
<pre class="bash" id="code_1764316211332"><code>public static void readFile() throws Exception {
    FileReader fr = new FileReader("test.txt"); // 예외 가능
}</code></pre>
<p>-&gt; 예외를&nbsp;직접&nbsp;처리하지&nbsp;않고&nbsp;호출한&nbsp;쪽으로&nbsp;넘김</p>
<p>-&gt; 주로 상위 로직에서 한 번에 처리할 때 사용</p>
<p>&nbsp;</p>
<p>3. throw</p>
<pre class="bash" id="code_1764317118821"><code>public static void checkAge(int age) {
    if (age &lt; 19) {
        throw new IllegalArgumentException("미성년자는 접근 불가");
    }
    System.out.println("접근 허용");
}</code></pre>
<p>-&gt; 예외를&nbsp;개발자가&nbsp;직접&nbsp;발생시킴</p>
<p>-&gt; 조건 검사, 비즈니스 로직 검증에 자주 사용</p>
<p>&nbsp;</p>
<p>4. finally 단독 의미</p>
<pre class="bash" id="code_1764317156699"><code>try {
    System.out.println("try 실행");
} catch (Exception e) {
    System.out.println("catch 실행");
} finally {
    System.out.println("finally 실행");
}</code></pre>
<p>-&gt; 예외 발생 여부와 관계없이 반드시 실행</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">면접 한줄 요약</h3>
<p style="text-align: center;">자바의&nbsp;예외는&nbsp;Throwable을&nbsp;최상위로&nbsp;Error와&nbsp;Exception으로&nbsp;나뉘며,&nbsp;Exception은&nbsp;컴파일&nbsp;시점에&nbsp;처리&nbsp;여부가&nbsp;</p>
<p style="text-align: center;">검사되는&nbsp;Checked&nbsp;예외와&nbsp;검사되지&nbsp;않는&nbsp;Unchecked(Runtime)&nbsp;예외로&nbsp;구분됩니다.</p>