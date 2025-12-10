# JavaScript 4일차

**카테고리**: 수강 일지

**작성일**: Fri, 19 Sep 2025 17:39:35 +0900

**원문 링크**: https://junsseok.tistory.com/18

---

<p style="text-align: center;">jQuery 학습</p>
<hr contenteditable="false" />
<p style="text-align: left;">1. jQuery :</p>
<p style="text-align: left;">기존의 자바스크립트만으로 구현하기 복잡했던 구문을 간소화하기 위해 만들어진 JavaScript 기반의 라이브러리</p>
<p>-&gt; 자바스크립트로 유용한 기능을 다른 개발자가 미리 정의해둔 것</p>
<p>-&gt; 짧고 직관적인 코드로 개발 가능</p>
<p>&nbsp;</p>
<p>2. 장점 :&nbsp;</p>
<p>(1) DOM요소 제어를 쉽게 할 수 있음</p>
<p>(2) AJAX(비동기 통신) 및 이벤트 처리를 간단히 구현 가능</p>
<p>(3) 차트, 슬라이드, 캘린더, 드래그앤 드랍 등 다양한 플러그인과 확장 지원</p>
<p>&nbsp;</p>
<p>3. jQuery 라이브러리 연결</p>
<p>- 직접 다운로드 방식</p>
<pre class="bash" id="code_1758253448427"><code>&lt;script src="js/jquery-3.7.1.min.js"&gt;&lt;/script&gt;</code></pre>
<p>jQuery&nbsp;파일을&nbsp;받아서&nbsp;로컬에&nbsp;저장&nbsp;후&nbsp;연결</p>
<p>&nbsp;</p>
<p>- CDN(Content Delivery Network) 방식</p>
<pre class="bash" id="code_1758253470371"><code>&lt;script src="https://code.jquery.com/jquery-3.7.1.min.js"&gt;&lt;/script&gt;</code></pre>
<p>파일을 직접 다운로드할 필요 없이 CDN 주소를 통해 불러오기</p>
<p>&nbsp;</p>
<p>4. jQuery 실행 시점</p>
<p>jQuery&nbsp;구문은&nbsp;DOM이&nbsp;준비된&nbsp;이후&nbsp;실행</p>
<pre class="bash" id="code_1758253571723"><code>// JS 방식
window.onload = function(){
    console.log("js 로딩 완료");
}

// jQuery 방식
$(document).ready(function(){
    console.log("document 로딩 완료");
})</code></pre>
<p>&nbsp;</p>
<p>5. 태그 선택자</p>
<pre class="bash" id="code_1758253596163"><code>&lt;p&gt;java&lt;/p&gt;
&lt;p&gt;oracle&lt;/p&gt;
&lt;p&gt;html&lt;/p&gt;

&lt;button class="btn"&gt;1&lt;/button&gt;
&lt;button class="btn"&gt;2&lt;/button&gt;
&lt;button class="btn"&gt;3&lt;/button&gt;</code></pre>
<pre class="bash" id="code_1758253602291"><code>$(function(){
    // 모든 &lt;p&gt; 태그 글씨 빨간색
    $("p").css("color","red");

    // 버튼 클릭 이벤트
    $(".btn").click(function(){
        alert("클릭됨");
    });
});</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>6. 요소 제어</p>
<pre class="bash" id="code_1758253614964"><code>&lt;h5 id="css-box"&gt;css&lt;/h5&gt;
&lt;ul id="ul-area"&gt;
    &lt;li&gt;1&lt;/li&gt;&lt;li&gt;2&lt;/li&gt;&lt;li&gt;3&lt;/li&gt;
&lt;/ul&gt;</code></pre>
<pre class="bash" id="code_1758253619755"><code>$(function(){
    let h5El = $("#css-box");

    // 스타일 변경
    $(h5El).css({
        "color":"red",
        "font-size":"20px"
    });

    // 이벤트 바인딩
    $(h5El).click(function(){
        alert("실행");
    });

    // 요소 내용 변경
    $(h5El).html("&lt;span&gt;내부 변경 확인&lt;/span&gt;");
    $(h5El).text("&lt;span&gt;내부 변경 확인&lt;/span&gt;");
});</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>7. 요소제거</p>
<pre class="bash" id="code_1758253640602"><code>$(function(){
    setTimeout(function(){
        // 버튼 전부 제거
        $(".btn").remove();

        // ul 내부 요소만 비우기
        $("#ul-area").empty();
    }, 2000);
});</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>8. input 관리</p>
<pre class="bash" id="code_1758253660083"><code>&lt;input type="text"&gt; &lt;br&gt;
&lt;input type="button"&gt; &lt;br&gt;
&lt;input type="checkbox"&gt; &lt;br&gt;
&lt;input type="radio"&gt; &lt;br&gt;
&lt;input type="submit"&gt; &lt;br&gt;</code></pre>
<pre class="bash" id="code_1758253664059"><code>$(function(){
    // text 박스
    $(":text").css("background","red").val("빨간 상자");

    // 버튼 크기 변경
    $(":button").css({
        width:"100px",
        height:"100px"
    }).val("큰 버튼");

    // 체크박스 자동 체크
    $(":checkbox").attr("checked",true);

    // 라디오 버튼 체크 + 크기 조절
    $(":radio").attr("checked",true).css({
        width:"50px",
        height:"50px"
    });

    // 제출 버튼 클릭 이벤트
    $(":submit").click(function(){
        alert("제출 완료");
    });
});</code></pre>
<p>&nbsp;</p>
<hr contenteditable="false" />
<p>핵심 :&nbsp;<br />1.&nbsp;jQuery는&nbsp;DOM&nbsp;제어,&nbsp;이벤트&nbsp;처리,&nbsp;AJAX&nbsp;통신을&nbsp;간단히&nbsp;할&nbsp;수&nbsp;있는&nbsp;JS&nbsp;라이브러리 <br />2.&nbsp;선택자($)&nbsp;를&nbsp;이용해&nbsp;HTML&nbsp;요소에&nbsp;접근하고&nbsp;속성을&nbsp;변경&nbsp;가능 <br />3.&nbsp;.css(),&nbsp;.html(),&nbsp;.text(),&nbsp;.val()&nbsp;등&nbsp;다양한&nbsp;메서드&nbsp;제공 <br />4.&nbsp;.click(),&nbsp;.remove(),&nbsp;.empty()&nbsp;등을&nbsp;이용해&nbsp;이벤트&nbsp;제어&nbsp;및&nbsp;요소&nbsp;조작&nbsp;가능</p>
<hr contenteditable="false" />
<p>배운점&amp;느낀점</p>
<p>jQuery를&nbsp;사용하면&nbsp;자바스크립트보다&nbsp;훨씬&nbsp;짧고&nbsp;직관적인&nbsp;코드로&nbsp;DOM&nbsp;요소를&nbsp;제어할&nbsp;수&nbsp;있다는&nbsp;것을&nbsp;배웠다.&nbsp;선택자를&nbsp;통해&nbsp;태그,&nbsp;클래스,&nbsp;아이디&nbsp;등을&nbsp;쉽게&nbsp;가져올&nbsp;수&nbsp;있고&nbsp;css,&nbsp;html,&nbsp;val&nbsp;같은&nbsp;메서드를&nbsp;이용해&nbsp;스타일과&nbsp;내용을&nbsp;간단히&nbsp;변경할&nbsp;수&nbsp;있다.&nbsp;기존에&nbsp;자바스크립트의&nbsp;querySelector나&nbsp;getElementById를&nbsp;사용할&nbsp;때는&nbsp;코드가&nbsp;길고&nbsp;복잡했는데,&nbsp;jQuery를&nbsp;사용하니&nbsp;훨씬&nbsp;간결하고&nbsp;가독성이&nbsp;좋아졌다.&nbsp;자바스크립트와&nbsp;jQuery를&nbsp;비교해가면서&nbsp;학습하다&nbsp;보니&nbsp;차이점을&nbsp;명확히&nbsp;이해할&nbsp;수&nbsp;있었고,&nbsp;DOM&nbsp;조작의&nbsp;기본&nbsp;개념을&nbsp;익히기에는&nbsp;jQuery가&nbsp;좋은&nbsp;도구라는&nbsp;생각이&nbsp;들었다.</p>