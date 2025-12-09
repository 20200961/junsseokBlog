# JavaScript 3일차

**카테고리**: 수강 일지

**작성일**: Thu, 18 Sep 2025 17:41:05 +0900

**원문 링크**: https://junsseok.tistory.com/17

---

<p style="text-align: center;">정규표현식, window용 객체, 연습문제</p>
<hr contenteditable="false" />
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: left;">1. 정규 표현식</p>
<p style="text-align: left;">정규표현식은&nbsp;문자열에서&nbsp;특정&nbsp;패턴을&nbsp;찾고,&nbsp;검사하고,&nbsp;치환하는&nbsp;표현식이다.&nbsp;아이디,&nbsp;비밀번호&nbsp;유효성&nbsp;검사나&nbsp;문자열&nbsp;검색,&nbsp;치환에&nbsp;자주&nbsp;쓰인다.</p>
<p style="text-align: left;">- 객체 생성</p>
<pre class="bash" id="code_1758184269531"><code>// 생성자 방식
const regExp1 = new RegExp("script");

// 리터럴 방식
const regExp2 = /script/;</code></pre>
<p>&nbsp;</p>
<p>- 주요 메서드</p>
<pre class="bash" id="code_1758184293235"><code>regExp.test(str);  // 패턴과 일치하면 true/false 반환
regExp.exec(str);  // 패턴과 일치하면 첫 번째 결과 반환, 없으면 null</code></pre>
<p>&nbsp;</p>
<p>- 예제</p>
<pre class="bash" id="code_1758184310226"><code>&lt;button onclick="test1()"&gt;실행&lt;/button&gt;
&lt;div id="area1"&gt;&lt;/div&gt;

&lt;script&gt;
function test1(){
    const area = document.getElementById('area1');
    const str1 = "javascript jquery ajax";
    const str2 = "java oracle html css";

    const regExp1 = new RegExp("script");
    const regExp2 = /script/;

    area.innerHTML += "regExp1.test(str1): " + regExp1.test(str1) + "&lt;br&gt;";
    area.innerHTML += "regExp2.test(str1): " + regExp2.test(str1) + "&lt;br&gt;";
    area.innerHTML += "regExp1.exec(str1): " + regExp1.exec(str1) + "&lt;br&gt;";
    area.innerHTML += "regExp2.exec(str2): " + regExp2.exec(str2) + "&lt;br&gt;";
}
&lt;/script&gt;</code></pre>
<p>&nbsp;</p>
<p>- 메타 문자</p>
<p>정규표현식에서 특수한 의미를 가지는 문자</p>
<pre class="bash" id="code_1758184361419"><code>^ : 문자열 시작
$ : 문자열 끝
[abc] : a 또는 b 또는 c
[^abc] : a, b, c 제외
[a-z] : 소문자 a~z
[A-Z] : 대문자 A~Z
[0-9] : 숫자 0~9
{5,12} : 5~12자</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>2. window 객체</p>
<p>window는 자바스크립트 최상위 객체, 크게 BOM과 DOM으로 나뉜다</p>
<p>&nbsp;</p>
<p>- window.open()</p>
<p>새 창을 열거나 제어할 수 있음</p>
<pre class="bash" id="code_1758184412378"><code>// 새 창 열기
window.open("https://www.naver.com", "naver", "width=500,height=500,resizable=no,location=no");

// 2초 후 닫기
let popup = window.open("https://www.naver.com", "naver", "width=500,height=500");
setTimeout(() =&gt; popup.close(), 2000);</code></pre>
<p>&nbsp;</p>
<p>- 타이머 관련 메서드</p>
<p>(1)&nbsp;setTimeout(함수,&nbsp;ms)&nbsp;:&nbsp;일정&nbsp;시간&nbsp;후&nbsp;함수&nbsp;1번&nbsp;실행 <br />(2)&nbsp;setInterval(함수,&nbsp;ms)&nbsp;:&nbsp;일정&nbsp;시간마다&nbsp;반복&nbsp;실행 <br />(3)&nbsp;clearInterval(id)&nbsp;&rarr;&nbsp;반복&nbsp;종료</p>
<p>&nbsp;</p>
<p>- 예제(시계)</p>
<pre class="bash" id="code_1758184471803"><code>&lt;button onclick="startClock()"&gt;실행&lt;/button&gt;
&lt;div id="area1"&gt;&lt;/div&gt;

&lt;script&gt;
function startClock(){
    const area = document.querySelector("#area1");
    setInterval(() =&gt; {
        const now = new Date();
        const time = `${now.getHours()} : ${now.getMinutes()} : ${now.getSeconds()}`;
        area.innerHTML = time;
    }, 1000);
}
&lt;/script&gt;</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>- location 객체</p>
<pre class="bash" id="code_1758184485386"><code>location.href = "https://naver.com";     // 이동
location.assign("https://naver.com");    // 이동 (뒤로가기 가능)
location.replace("https://naver.com");   // 이동 (뒤로가기 불가)
location.reload();                       // 새로고침</code></pre>
<p>&nbsp;</p>
<p>- screen, navigator, history 객체</p>
<p>(1)screen&nbsp;:&nbsp;화면&nbsp;해상도,&nbsp;색상&nbsp;정보 <br />(2)navigator&nbsp;:&nbsp;브라우저,&nbsp;OS&nbsp;정보 <br />(3)history&nbsp;:&nbsp;방문&nbsp;기록</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<p>연습문제1.</p>
<p><figure class="imageblock alignCenter"><span><img height="145" src="https://blog.kakaocdn.net/dn/cRtj7c/btsQFqfVsz3/gxjz4My5sas5BEo2nuc3L0/img.png" width="700" /></span></figure>
</p>
<pre class="bash" id="code_1758184550466"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Document&lt;/title&gt;
    &lt;style&gt;
        .area{
            border: 1px solid red;
            min-height: 200px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=""&gt;
    &lt;fieldset&gt;
        &lt;legend&gt;취미&lt;/legend&gt;
        &lt;table&gt;
            &lt;tr&gt;
                &lt;td&gt;
                    &lt;label&gt;
                        &lt;input type="checkbox" id="all-hobby-check" onchange="allCheck(this)"&gt;
                        전체선택
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                    &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="종합"&gt;
                        종합
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                      &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="소설" &gt;
                        소설
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                      &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="시/에세이"&gt;
                        시/에세이
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                      &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="경영/경제"&gt;
                        경영/경제
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                        &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="자기계발"&gt;
                        자기계발
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                    &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="아동"&gt;
                        아동
                    &lt;/label&gt;
                &lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;&lt;/td&gt;
                &lt;td&gt;
                    &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="여행"&gt;
                        여행
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                      &lt;label&gt; 
                        &lt;input type="checkbox" name="hobby" value="과학"&gt;
                        과학
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                      &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="역사/문화"&gt;
                        역사/문화
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                      &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="외국어"&gt;
                        외국어
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                    &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="컴퓨터"&gt;
                        컴퓨터
                    &lt;/label&gt;
                &lt;/td&gt;
                &lt;td&gt;
                    &lt;label&gt;
                        &lt;input type="checkbox" name="hobby" value="만화"&gt;
                        만화
                    &lt;/label&gt;
                &lt;/td&gt;
            &lt;/tr&gt;
        &lt;/table&gt;
    &lt;/fieldset&gt;
  &lt;/form&gt;  

  &lt;br&gt;

  &lt;button onclick="selectCatrgory()"&gt;카테고리 선택&lt;/button&gt;
  &lt;div class="area" id="select-result"&gt;&lt;/div&gt;

  &lt;script&gt;
    function selectCatrgory(){
        //하단 네모에 선택한 카테고리(checkbox가 checked인 것) 출력
        const hobbyCheckBoxList = document.querySelectorAll('input[name=hobby]');
        console.log(hobbyCheckBoxList);

        let str = "";
        for(let i=0; i&lt;hobbyCheckBoxList.length; i++){
            const box = hobbyCheckBoxList[i];
            if(box.checked) { //체크된 박스인지 검사
                  str += (box.value + " "); //체크된 박스의 value값을 전부 str에 더함.
            }
        }

        const resultEl = document.getElementById('select-result');
        resultEl.innerText = str;
    }

    function allCheck(_allCheckBox){
        const isChecked = _allCheckBox.checked; //전체선택 체크박스가 true(체크됨), false(체크안됨)에 따라서 나머지 체크박스의 check상태도 변경
        
        //모든 체크박스 가져오기
        const hobbyCheckBoxList = document.querySelectorAll('input[name=hobby]');
        //모든체크박스를 반복하며
        for(let i=0; i&lt;hobbyCheckBoxList.length; i++){
            //체크박스의 check상태를 전체선택 체크박스의 상태와 동일하게 적용
            hobbyCheckBoxList[i].checked = isChecked;
        }
    }

    function changeAllCheckBox(){
        //모든체크박스를 가져와서
        const hobbyCheckBoxList = document.querySelectorAll('input[name=hobby]');

        //하나라도 체크되지 않은게 있는가?
        //하나라도 체크되지않았다면 false, 모두체크상태라면 true
        let isChecked = true;
        for(let i=0; i&lt;hobbyCheckBoxList.length; i++){
            if(!hobbyCheckBoxList[i].checked){// 체크박스가 체크되지 않았다면
                isChecked = false;
                break;
            }
        }

        //체크되지않은 걸 찾지못함 -&gt; isChecked = true;
        // if(!hobbyCheckBoxList[i].checked)조건에 만족하는 결과값을 찾았다면 -&gt; isChecked = false;
        const allCheckBox = document.getElementById('all-hobby-check');
        allCheckBox.checked = isChecked;
    }

    const hobbyCheckBoxList = document.querySelectorAll('input[name=hobby]');
    for(let i=0; i&lt;hobbyCheckBoxList.length; i++){
        hobbyCheckBoxList[i].onchange = changeAllCheckBox;
    }
    
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>&nbsp;</p>
<p>실행 결과</p>
<p><figure class="imageblock alignCenter"><span><img height="406" src="https://blog.kakaocdn.net/dn/cH8exz/btsQD0P5u7C/Vok2h84sbzks77CbD40vOK/img.png" width="924" /></span></figure>
</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>연습문제 2.&nbsp;</p>
<p><figure class="imageblock alignCenter"><span><img height="207" src="https://blog.kakaocdn.net/dn/b2l7Z6/btsQCLeByjh/EPOUDF2d45h0gL4hYqowBK/img.png" width="685" /></span></figure>
</p>
<pre class="bash" id="code_1758184584323"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Document&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form action="answer"&gt;
        &lt;input type="number" id="num1" name="num1" min="0" max="100"&gt;
        &lt;select id='operator' name="operator"&gt;
            &lt;option value="plus" selected&gt;+&lt;/option&gt;
            &lt;option value="minus"&gt;-&lt;/option&gt;
            &lt;option value="multi"&gt;*&lt;/option&gt;
            &lt;option value="divide"&gt;/&lt;/option&gt;
        &lt;/select&gt;
        &lt;input type="number" id="num2" name="num2" min="0" max="100"&gt;
        &lt;input type="button" onclick="cal()" value="="&gt;
        &lt;input type="number" id="result" name="result" max="10000"&gt;
    &lt;/form&gt;
    
    &lt;script&gt;
        function cal(){
            const a = Number(num1.value); 
            const b = Number(num2.value); 
            const op = operator.value;
            const result = document.getElementById('result');

            if(operator.value== "plus"){
                result.value = a+b
            }
            if(operator.value== "minus"){
                result.value = a-b
            }
            if(operator.value== "multi"){
                result.value = a*b
            }
            if(operator.value== "divide"){
                result.value = a/b
            }

        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>&nbsp;</p>
<p>실행결과</p>
<p><figure class="imageblock alignCenter"><span><img height="43" src="https://blog.kakaocdn.net/dn/pdpou/btsQFAJh1Bq/rnaJ3q6JKauCjVpLKsSlpK/img.png" width="425" /></span></figure>
<figure class="imageblock alignCenter"><span><img height="46" src="https://blog.kakaocdn.net/dn/bMnD5g/btsQD0CBJrc/eUpAokZEVFyFLkJlHPfCK0/img.png" width="423" /></span></figure>
<figure class="imageblock alignCenter"><span><img height="47" src="https://blog.kakaocdn.net/dn/biqAOP/btsQDeOOmSP/KI9s6DcehfhdmJ4Dbf2lt0/img.png" width="430" /></span></figure>
<figure class="imageblock alignCenter"><span><img height="48" src="https://blog.kakaocdn.net/dn/nNp46/btsQDJnvOwu/LFtdgGdNejK6GKGhoqmnmK/img.png" width="426" /></span></figure>
</p>
<p>&nbsp;</p>
<p>연습문제4.</p>
<p><figure class="imageblock alignCenter"><span><img height="354" src="https://blog.kakaocdn.net/dn/Hjknr/btsQEpPf3X0/BY0nKa7w0OTlE2OtuLjgFK/img.png" width="683" /></span></figure>
</p>
<pre class="bash" id="code_1758184652715"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Document&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;
        &lt;legend&gt;회원가입&lt;/legend&gt;
        아이디 : &lt;input type="text" id="id" oninput="checkId()"&gt;&lt;span id="idMsg"&gt;&lt;/span&gt;&lt;br&gt;&lt;br&gt;
        비밀번호 : &lt;input type="password" id="pw"&gt;&lt;br&gt;&lt;br&gt;
        비밀번호 확인 : &lt;input type="password" id="rpw" oninput="checkPwd()"&gt;&lt;span id="pwMsg"&gt;&lt;/span&gt;&lt;br&gt;&lt;br&gt;
        이름 : &lt;input type="text" id="name"&gt;&lt;br&gt;&lt;br&gt;
        &lt;input type="button" value="회원가입" onclick="signup()"&gt;
    &lt;/fieldset&gt;

    &lt;script&gt; 
        const id = document.getElementById('id');
        const pw = document.getElementById('pw');
        const rpw = document.getElementById('rpw');
        const name = document.getElementById('name');
        const idMsg = document.getElementById('idMsg');
        const pwMsg = document.getElementById('pwMsg');

        function checkId(){
            if(id.value == "user02"){
                idMsg.textContent = "사용가능한 아이디입니다";
                idMsg.style.color = "green";
            }else {
                idMsg.textContent = "이미 존재하는 아이디입니다.";
                idMsg.style.color = "red";
            }
        }

        function checkPwd(){
            if(pw.value != rpw.value){
                pwMsg.textContent="비밀번호가 일치하지 않습니다.";
                pwMsg.style.color="red";
            }else {
                pwMsg.textContent="비밀번호가 일치합니다.";
                pwMsg.style.color="green";
            }
        }
        function signup(){
            if(id.value != "user02"){
                alert("아이디를 체크하세요");
                location.reload();
                return;
            }
            if(pw.value != rpw.value){
                alert("비밀번호를 체크하세요");
                location.reload();
                return;
            }
            if(id.value == "" || pw.value == "" || rpw.value == "" || name.value == ""){
                alert("모든 항목을 입력해주세요");
                location.reload();
                return;
            }
            alert(name.value+"님, 회원가입이 성공적으로 완료되었습니다^^");
            location.reload();
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>&nbsp;</p>
<p>id 중복체크는 데베 연결이 없어서 user02로 하드코딩</p>
<p>&nbsp;</p>
<p>실행결과</p>
<p><figure class="imageblock alignCenter"><span><img height="246" src="https://blog.kakaocdn.net/dn/6dKkg/btsQFpgYgSl/8OipGm6E3cckAQTZIZgKyK/img.png" width="748" /></span></figure>
</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<p>배운점 &amp; 느낀점</p>
<p>HTML과&nbsp;자바스크립트를&nbsp;활용해&nbsp;입력값을&nbsp;실시간으로&nbsp;검증하고,&nbsp;DOM&nbsp;요소와&nbsp;값을&nbsp;구분하여&nbsp;동적으로&nbsp;메시지를&nbsp;표시하는&nbsp;방법을&nbsp;배웠다.&nbsp;작은&nbsp;이벤트&nbsp;차이가&nbsp;사용자&nbsp;경험에&nbsp;큰&nbsp;영향을&nbsp;주며,&nbsp;실시간&nbsp;피드백&nbsp;구현을&nbsp;통해&nbsp;웹&nbsp;페이지&nbsp;UX를&nbsp;개선할&nbsp;수&nbsp;있음을&nbsp;느꼈다.&nbsp;연습문제를&nbsp;풀어보며&nbsp;배웠던&nbsp;것을&nbsp;응용하는&nbsp;시간을&nbsp;가질&nbsp;수&nbsp;있었고&nbsp;실력이&nbsp;점점&nbsp;늘어가는&nbsp;것을&nbsp;느낄&nbsp;수&nbsp;있었다.</p>