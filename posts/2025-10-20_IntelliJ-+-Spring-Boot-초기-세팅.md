# IntelliJ + Spring  Boot 초기 세팅

**작성일**: Mon, 20 Oct 2025 17:10:49 +0900

**원문 링크**: https://junsseok.tistory.com/33

---

<p style="text-align: center;">Spring Boot 초기 세팅</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">IntelliJ 초기 세팅</h3>
<p>IntelliJ&nbsp;IDEA&nbsp;:&nbsp;JetBrains에서&nbsp;만든&nbsp;자바기반&nbsp;통합&nbsp;개발&nbsp;환경(IDE)이다.</p>
<p>&nbsp;</p>
<p>IntelliJ를 쓰는 이유<br />-&gt;&nbsp;빠른&nbsp;개발&nbsp;:&nbsp;코드&nbsp;자동&nbsp;완성,&nbsp;템플릿,&nbsp;리팩토링&nbsp;기능이&nbsp;강력함 <br />-&gt;&nbsp;효율적&nbsp;디버깅&nbsp;:&nbsp;오류&nbsp;원인&nbsp;찾기&nbsp;쉽고,&nbsp;코드&nbsp;흐름&nbsp;시각화&nbsp;가능 <br />-&gt;&nbsp;프로젝트&nbsp;관리&nbsp;용이&nbsp;:&nbsp;Maven,&nbsp;Gradle,&nbsp;Git&nbsp;등을&nbsp;한&nbsp;곳에서&nbsp;관리 <br />-&gt;&nbsp;스프링&nbsp;개발&nbsp;최적화&nbsp;:&nbsp;Spring,&nbsp;Spring&nbsp;Boot&nbsp;프로젝트&nbsp;생성,&nbsp;실행,&nbsp;디버깅이&nbsp;편리</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">초기 세팅</h3>
<p style="text-align: center;">밑에 있는 링크에 들어가 IntelliJ IDEA 다운로드 페이지로 들어간다.</p>
<p style="text-align: center;"><a href="https://www.jetbrains.com/ko-kr/idea/download/?section=windows" rel="noopener&nbsp;noreferrer" target="_blank">https://www.jetbrains.com/ko-kr/idea/download/?section=windows</a></p>
<figure contenteditable="false" id="og_1760946374946"><a href="https://www.jetbrains.com/ko-kr/idea/download/?section=windows" rel="noopener" target="_blank">
<div class="og-image">&nbsp;</div>
<div class="og-text">
<p class="og-title">IntelliJ IDEA 다운로드</p>
<p class="og-desc">&nbsp;</p>
<p class="og-host">www.jetbrains.com</p>
</div>
</a></figure>
<p>&nbsp;</p>
<p><figure class="imageblock alignCenter"><span><img height="387" src="https://blog.kakaocdn.net/dn/bInNXL/dJMb9OnaCVh/xDORSwMFNqKfFJV70A4Vdk/img.png" width="490" /></span></figure>
</p>
<p style="text-align: center;">&nbsp;</p>
<p><figure class="imageblock alignCenter"><span><img height="327" src="https://blog.kakaocdn.net/dn/UsD0E/dJMb862mZig/CAXwiy22p2p2HkVnHKke6k/img.png" width="491" /></span></figure>
<figure class="imageblock alignCenter"><span><img height="382" src="https://blog.kakaocdn.net/dn/CrIcv/dJMb9LRv00s/Gx52RwTq7XkUaS9Kh6eTP1/img.png" width="496" /></span></figure>
<figure class="imageblock alignCenter"><span><img height="386" src="https://blog.kakaocdn.net/dn/b3Iq91/dJMb9PfjboP/8OcZL0MP2oAWQPgbB3TBv0/img.png" width="500" /></span></figure>
</p>
<p style="text-align: center;">인스톨러를&nbsp;실행해&nbsp;기본&nbsp;옵션으로&nbsp;설치한다.&nbsp;학교이메일&nbsp;인증을&nbsp;통해&nbsp;Ultimate사용시&nbsp;편리하다. <br /><br />workspace에&nbsp;spring폴더&nbsp;생성후&nbsp;intellij로&nbsp;열기</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: left;">1. Auto Import</p>
<p><figure class="imageblock alignCenter"><span><img height="550" src="https://blog.kakaocdn.net/dn/bx7TGs/dJMb85bjYha/EypZgwfUZLkUukEqn03gxk/img.png" width="746" /></span></figure>
</p>
<p style="text-align: left;">-&nbsp;경로:&nbsp;Settings&nbsp;-&gt;&nbsp;Editor&nbsp;-&gt;&nbsp;General&nbsp;-&gt;&nbsp;Auto&nbsp;Import <br />&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Add&nbsp;unambiguous&nbsp;imports&nbsp;on&nbsp;the&nbsp;fly&nbsp;체크(클래스가&nbsp;하나로&nbsp;확정되면&nbsp;자동&nbsp;import) <br />&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Optimize&nbsp;imports&nbsp;on&nbsp;the&nbsp;fly&nbsp;체크(불필요&nbsp;import&nbsp;정리)</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">2. Code&nbsp;Completion&nbsp;&lsquo;Match&nbsp;case&rsquo;&nbsp;해제</p>
<p><figure class="imageblock alignCenter"><span><img height="570" src="https://blog.kakaocdn.net/dn/SQgDj/dJMb85bjYhn/XoAMsEVyWKH81YAylKzOo1/img.png" width="772" /></span></figure>
</p>
<p>-&nbsp;경로:&nbsp;Settings&nbsp;-&gt;&nbsp;Editor&nbsp;-&gt;&nbsp;Code&nbsp;Completion <br />&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Match&nbsp;case&nbsp;해제(대소문자&nbsp;구분&nbsp;없이&nbsp;자동완성)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>3. Annotation&nbsp;Processing&nbsp;활성화</p>
<p><figure class="imageblock alignCenter"><span><img height="574" src="https://blog.kakaocdn.net/dn/blU6ev/dJMb9Ogo7wn/8FnrE2fksMCEvHLBfTH0k0/img.png" width="777" /></span></figure>
</p>
<p>-&nbsp;경로:&nbsp;Settings&nbsp;-&gt;&nbsp;Build,&nbsp;Execution,&nbsp;Deployment&nbsp;-&gt;&nbsp;Compiler&nbsp;-&gt;&nbsp;Annotation&nbsp;Processors <br />&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Enable&nbsp;annotation&nbsp;processing&nbsp;체크 <br />&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Obtain&nbsp;processors&nbsp;from&nbsp;project&nbsp;classpath&nbsp;선택(일반적) <br />&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;이유:&nbsp;Lombok&nbsp;등&nbsp;애너테이션&nbsp;기반&nbsp;코드&nbsp;생성&nbsp;사용&nbsp;시&nbsp;컴파일&nbsp;타임&nbsp;처리&nbsp;필요</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>4. JDK 경로 지정</p>
<p><figure class="imageblock alignCenter"><span><img height="608" src="https://blog.kakaocdn.net/dn/2lN8H/dJMb9XdgIz9/o8rsTh1UsfNTTntEokWp50/img.png" width="779" /></span></figure>
</p>
<p>-&nbsp;File&nbsp;-&gt;&nbsp;Project&nbsp;Structure&nbsp;-&gt;&nbsp;Project <br />&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Project&nbsp;SDK에&nbsp;설치한&nbsp;JDK&nbsp;선택 <br />&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Project&nbsp;language&nbsp;level은&nbsp;SDK&nbsp;기본값&nbsp;사용</p>
<p>&nbsp;</p>
<p>5. 테스트</p>
<p>src/resources/static에 index.html 생성 후 다음 코드를 넣는다.</p>
<pre class="bash" id="code_1760947580439"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Title&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
Hello world
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>&nbsp;</p>
<p>이후 target/classes/com/kh/spring/application.class를 실행한 뒤 localhost:8080에 접속하면 Hello world가 출력되는것을 확인할 수 있다.</p>
<p>-&gt; Spring Boot는 내장 톰캣 서버를 사용하고, static 폴더 안의 index.html을 자동으로 서빙하기 때문에 localhost:8080에서 'Hello world'를 확인할 수 있다.</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">스프링&nbsp;부트</h3>
<p>스프링 부트 : 복잡한 설정 없이도 스프링 애플리케이션을 빠르고 쉽게 만들 수 있게 도와주는 도구</p>
<p>&nbsp;</p>
<p>쉽게 비유하면<br />- 기존 Spring Framework는<br />요리할 때 재료를 일일이 사고, 썰고, 양념 만들어야 하는 수동 방식<br /><br />- 반면 Spring Boot는<br />모든 재료와 도구가 세팅된 즉석 밀키트<br /><br />즉, 설정 파일(XML 등)을 일일이 만들지 않아도 톰캣 서버, 의존성, 설정 등을 구성</p>
<p>&nbsp;</p>
<p>스프링 부트의 목표 : 매우&nbsp;빠르고&nbsp;광범위한&nbsp;영역의&nbsp;스프링&nbsp;개발&nbsp;경험을&nbsp;제공하는&nbsp;것을&nbsp;목표로&nbsp;한다.&nbsp;개발자가&nbsp;즉시&nbsp;실무에&nbsp;적용&nbsp;가능한&nbsp;기술&nbsp;조합을&nbsp;기본으로&nbsp;제공하며,&nbsp;필요에&nbsp;따라&nbsp;유연하게&nbsp;커스터마이징할&nbsp;수&nbsp;있는&nbsp;구조를&nbsp;갖추고&nbsp;있다.&nbsp;또한,&nbsp;스프링&nbsp;부트는&nbsp;프로젝트에&nbsp;일반적으로&nbsp;필요한&nbsp;다양한&nbsp;비기능&nbsp;기술&nbsp;요소들을&nbsp;기본&nbsp;내장한다.</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">초기 세팅</h3>
<p style="text-align: center;">밑에 있는 링크에 들어가 Spring initializr 페이지로 들어간다.</p>
<p style="text-align: center;"><a href="https://start.spring.io/" rel="noopener&nbsp;noreferrer" target="_blank">https://start.spring.io/</a></p>
<p><span style="color: #333333; text-align: center;">Spring initializr<span> : 스프링 부트 프로젝트를 빠르게 세팅할 수 있게 하는 웹 도구이다.</span></span></p>
<p><figure class="imageblock alignCenter"><span><img height="902" src="https://blog.kakaocdn.net/dn/b3D94g/dJMb85I9Uqh/lPDcqutmXw39vR9amsJiW0/img.png" width="1674" /></span></figure>
</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">위와 같이 세팅후 GENERATE를 누른다.</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">압축파일로 제공되어 압축 해제후 IDE를 사용하여 spring 프로젝트를 실행한다.&nbsp;</p>
<hr contenteditable="false" />
<p style="text-align: center;">처음 배우는 Spring boot와 intelliJ라서 처음 세팅하는데 약간 힘들었지만 오늘 정리한 내용들을 토대로 나중에 다시 세팅하고 시작할 때 도움이 될 것 같다! 힘든 것이 성장통처럼 내가 성장하는 과정이라고 생각하며 더욱 열심히 할예정!!!!</p>