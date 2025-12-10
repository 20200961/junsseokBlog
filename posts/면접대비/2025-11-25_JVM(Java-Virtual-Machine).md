# JVM(Java Virtual Machine)

**카테고리**: 면접대비

**작성일**: Tue, 25 Nov 2025 16:49:12 +0900

**원문 링크**: https://junsseok.tistory.com/42

---

<p style="text-align: center;">JVM(Java Virtual Machine)에 대해 공부해 보았다.</p>
<hr contenteditable="false" />
<p style="text-align: center;"><b>자바 프로그램이 OS와 무관하게 실행될 수 있도록 해주는 핵심 실행 환경이자, </b></p>
<p style="text-align: center;"><b>메모리 관리, GC, 바이트코드 실행 등을 담당하는 자바 플랫폼의 핵심 컴포넌트</b></p>
<hr contenteditable="false" />
<p style="text-align: left;"><b>Why (왜 사용하는가? 왜 중요한가?)</b><br /><b>이 개념이 실무, 설계, 면접에서 중요한 이유를 정리한다.</b></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">- 실무 : JVM이 없다면 자바는 OS마다 다른 실행 파일을 만들어야 하고, 메모리 관리도 직접 수행해야 해 유지보수 비용이 폭증한다.</p>
<p style="text-align: left;"><br />- 구조적 의미 : 바이트코드 기반 실행과 JIT 최적화를 통해 플랫폼 독립성을 제공하면서도 네이티브에 가까운 성능을 확보할 수 있다.</p>
<p style="text-align: left;"><br />- 면접 의도 : JVM 구조를 이해하면 메모리 구조, GC 동작, 스레드 모델 등 자바 성능과 안정성 문제를 해결할 수 있는 역량을 확인할 수 있다.</p>
<hr contenteditable="false" />
<p>&nbsp;</p>
<p><b>Core&nbsp;Concept&nbsp;(핵심&nbsp;개념&nbsp;정리)</b></p>
<table border="1" id="2b5435fc-bd9d-80ae-adfd-cec477a83abe" style="border-collapse: collapse; width: 97.4419%; height: 307px;">
<tbody>
<tr>
<td>요소</td>
<td>내용</td>
</tr>
<tr>
<td>개념정의</td>
<td>JVM은&nbsp;자바&nbsp;바이트코드를&nbsp;해석하고&nbsp;실행하기&nbsp;위한&nbsp;가상&nbsp;머신으로,&nbsp;OS와&nbsp;자바&nbsp;프로그램&nbsp;사이의&nbsp;추상화&nbsp;계층&nbsp;역할을&nbsp;한다.</td>
</tr>
<tr>
<td>동작방식</td>
<td>(1)&nbsp;Java&nbsp;컴파일러가&nbsp;.java&nbsp;&rarr;&nbsp;.class(바이트코드)&nbsp;생성&nbsp; <br />(2)&nbsp;JVM&nbsp;Class&nbsp;Loader가&nbsp;바이트코드&nbsp;적재 <br />(3)&nbsp;Execution&nbsp;Engine이&nbsp;인터프리터/JIT을&nbsp;사용해&nbsp;실행 <br />(4)&nbsp;GC가&nbsp;자동&nbsp;메모리&nbsp;관리&nbsp;수행</td>
</tr>
<tr id="2b5435fc-bd9d-8038-a986-de1faab736d2" style="height: 63px;">
<td id="BuIY" style="width: 15.9646%; height: 63px;">장점/단점</td>
<td id="tf]I" style="width: 83.9178%; height: 63px;">장점 : 플랫폼 독립성(Write Once, Run Anywhere), 자동 메모리 관리(GC), 안정성, 풍부한 표준 라이브러리<br />단점 : 네이티브 언어(C/C++) 대비 초기 실행 속도 느림</td>
</tr>
<tr id="2b5435fc-bd9d-80bd-ba0e-fd1dd66b2a8f" style="height: 23px;">
<td id="BuIY" style="width: 15.9646%; height: 23px;">필요 조건</td>
<td id="tf]I" style="width: 83.9178%; height: 23px;">JDK/JRE&nbsp;설치,&nbsp;적절한&nbsp;JVM&nbsp;옵션&nbsp;설정(-Xmx,&nbsp;-Xms&nbsp;등)</td>
</tr>
<tr id="2b5435fc-bd9d-8060-8329-cf643643c56b" style="height: 23px;">
<td id="BuIY" style="width: 15.9646%; height: 23px;">예시/비교</td>
<td id="tf]I" style="width: 83.9178%; height: 23px;">Node.js처럼 JS를 실행하는 런타임과 유사하나, JVM은 GC 튜닝, 여러 언어(Kotlin, Scala 등)를 지원하는 "멀티랭귀지 플랫폼"이라는 점이 다르다.</td>
</tr>
</tbody>
</table>
<hr contenteditable="false" />
<p style="text-align: left;"><b> <span>Interview Answer Version (면접 답변식 요약)<br /></span> </b></p>
<p style="text-align: left;"><span>JVM은 자바 바이트코드를 OS와 상관없이 실행하도록 해주는 가상 머신입니다. 내부적으로 Class Loader, Execution Engine, GC로 구성되어 바이트코드를 로드하고 실행하며 메모리를 자동으로 관리합니다. 특히 JIT 컴파일러를 통해 인터프리팅 기반임에도 네이티브에 가까운 성능을 제공합니다. JVM 구조를 이해하면 GC 튜닝, 메모리 구조 분석, 성능 최적화 등 실무 필수 문제를 해결할 수 있기 때문에 중요한 개념이라고 생각합니다.</span></p>
<hr contenteditable="false" />
<p style="text-align: left;"><b>Practical&nbsp;Tip&nbsp;(사용시&nbsp;주의할&nbsp;점&nbsp;or&nbsp;활용&nbsp;예)</b></p>
<p>- GC 방식 선택도 중요하다. <br />예:&nbsp;Spring&nbsp;Boot&nbsp;서버에서&nbsp;CMS&nbsp;대신&nbsp;G1GC를&nbsp;적용하면&nbsp;대규모&nbsp;트래픽에서도&nbsp;STW&nbsp;시간을&nbsp;획기적으로&nbsp;줄일&nbsp;수&nbsp;있다. <br /><br />- 메모리 누수는 자바에서도 발생할 수 있다. <br />Singleton에서&nbsp;컬렉션을&nbsp;계속&nbsp;누적하는&nbsp;패턴&nbsp;등은&nbsp;GC가&nbsp;접근하지&nbsp;못해&nbsp;누수가&nbsp;발생한다. <br /><br />- 실무에서는 모니터링 도구(JConsole, VisualVM, Prometheus + Grafana) 를 통해 Heap, GC Time, 스레드 상태를 수시로 체크해 안정성을 유지한다.</p>
<hr contenteditable="false" />
<p><b>예상&nbsp;꼬리질문&nbsp;정리</b> <br /><br />1. JVM 메모리 구조(Heap, Stack, Metaspace)의 역할을 설명해보세요. <br /><br />2. JIT Compiler는 언제, 왜 사용되는가? <br /><br />3. JVM 기준으로 스레드는 어떻게 관리되는가? <br /><br />4. JVM과 JRE/JDK의 차이를 정확히 설명해보세요.</p>
<hr contenteditable="false" />
<p>&nbsp;</p>
<p>1.&nbsp;Heap은&nbsp;객체&nbsp;저장,&nbsp;Stack은&nbsp;스레드별&nbsp;실행&nbsp;정보&nbsp;저장,&nbsp;Metaspace는&nbsp;클래스&nbsp;메타정보&nbsp;저장&nbsp;영역입니다.&nbsp;Heap은&nbsp;GC가&nbsp;관리하지만&nbsp;Stack은&nbsp;호출&nbsp;시&nbsp;자동&nbsp;관리됩니다 <br /><br />2.&nbsp;JIT&nbsp;컴파일러는&nbsp;자주&nbsp;실행되는&nbsp;코드를&nbsp;런타임에&nbsp;기계어로&nbsp;변환해&nbsp;성능을&nbsp;올리기&nbsp;위한&nbsp;기술입니다.&nbsp;인터프리터의&nbsp;느린&nbsp;실행을&nbsp;보완하는&nbsp;역할을&nbsp;합니다 <br /><br />3.&nbsp;JVM&nbsp;스레드는&nbsp;OS&nbsp;스레드와&nbsp;1:1로&nbsp;매핑되며&nbsp;각&nbsp;스레드는&nbsp;독립된&nbsp;스택을&nbsp;갖습니다.&nbsp;스레드&nbsp;스케줄링은&nbsp;OS가&nbsp;수행하고,&nbsp;Heap과&nbsp;Metaspace는&nbsp;스레드&nbsp;간에&nbsp;공유됩니다 <br /><br />4.&nbsp;JVM은&nbsp;바이트코드를&nbsp;실행하는&nbsp;엔진이고,&nbsp;JRE는&nbsp;JVM에&nbsp;표준&nbsp;라이브러리를&nbsp;더한&nbsp;&lsquo;실행&nbsp;환경&rsquo;이며,&nbsp;JDK는&nbsp;컴파일러까지&nbsp;포함된&nbsp;&lsquo;개발&nbsp;키트&rsquo;입니다</p>