# Garbage Collection

**작성일**: Tue, 25 Nov 2025 17:14:00 +0900

**원문 링크**: https://junsseok.tistory.com/43

---

<p style="text-align: center;">Garbage&nbsp;Collection</p>
<hr contenteditable="false" />
<p style="text-align: center;"><b> <span style="background-color: #ffffff; color: #001d35; text-align: start;">프로그래밍에서 더 이상 사용되지 않는 메모리 영역을 자동으로 찾아 삭제하고, 회수된 메모리를 재활용하는 과정</span> </b></p>
<hr contenteditable="false" />
<p style="text-align: left;"><b>Why (왜 사용하는가? 왜 중요한가?)</b><br /><b>이 개념이 실무, 설계, 면접에서 중요한 이유를 정리한다.</b></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">-&nbsp;실무&nbsp;:&nbsp;객체가&nbsp;자동으로&nbsp;해제되지&nbsp;않으면&nbsp;메모리&nbsp;누수로&nbsp;인해&nbsp;서버가&nbsp;느려지고&nbsp;OOM(OutOfMemory)&nbsp;오류가&nbsp;발생한다. <br /><br /><br />-&nbsp;구조적&nbsp;의미&nbsp;:&nbsp;JVM이&nbsp;객체&nbsp;생명주기를&nbsp;자동&nbsp;관리하여&nbsp;개발자는&nbsp;비즈니스&nbsp;로직에&nbsp;집중하고,&nbsp;GC&nbsp;알고리즘이&nbsp;효율적으로&nbsp;힙&nbsp;메모리를&nbsp;재사용하게&nbsp;해준다. <br /><br /><br />-&nbsp;면접&nbsp;의도&nbsp;:&nbsp;객체&nbsp;메모리&nbsp;구조,&nbsp;JVM&nbsp;내부&nbsp;이해도,&nbsp;튜닝&nbsp;능력,&nbsp;성능&nbsp;병목&nbsp;처리&nbsp;경험&nbsp;등을&nbsp;확인하려는&nbsp;질문이다.</p>
<hr contenteditable="false" />
<p style="color: #333333; text-align: start;">&nbsp;</p>
<p style="color: #333333; text-align: start;"><b>Core&nbsp;Concept&nbsp;(핵심&nbsp;개념&nbsp;정리)</b></p>
<table border="1" id="2b5435fc-bd9d-80ae-adfd-cec477a83abe" style="border-collapse: collapse; width: 97.4419%; height: 299px;">
<tbody>
<tr style="height: 21px;">
<td style="background-color: #2780d4; color: #ffffff; height: 21px;">요소</td>
<td style="background-color: #2780d4; color: #ffffff; height: 21px;">내용</td>
</tr>
<tr style="height: 42px;">
<td style="background-color: #efefef; height: 42px;">개념정의</td>
<td style="height: 42px;">Java에서&nbsp;더&nbsp;이상&nbsp;참조되지&nbsp;않는&nbsp;객체를&nbsp;자동으로&nbsp;탐지해&nbsp;메모리에서&nbsp;해제하는&nbsp;동작.&nbsp;JVM의&nbsp;메모리&nbsp;자동&nbsp;관리&nbsp;시스템.</td>
</tr>
<tr style="height: 84px;">
<td style="background-color: #efefef; height: 84px;">동작방식</td>
<td style="background-color: #f9f9f9; height: 84px;">(1) 새로 생성된 객체 저장 -&gt; 대부분 금방 사라져 효율적 회수 가능<br />(2) 살아남은 객체를 Survivor 영역 간에 옮기며 age 증가<br />(3) 일정 age 이상 생존 -&gt; Old로 이동 -&gt; 여기서 GC가 발생하면 Stop-the-world 시간이 길어짐<br />(4)&nbsp;GC&nbsp;Root로부터&nbsp;도달&nbsp;가능한&nbsp;객체만&nbsp;'살아있음'으로&nbsp;취급.&nbsp;(스택,&nbsp;static,&nbsp;네이티브&nbsp;레퍼런스&nbsp;등)</td>
</tr>
<tr id="2b5435fc-bd9d-8038-a986-de1faab736d2" style="height: 63px;">
<td id="BuIY" style="width: 15.9646%; height: 63px;">장점/단점</td>
<td id="tf]I" style="width: 83.9178%; height: 63px;">장점 : 개발자가 메모리 해제를 신경 쓸 필요 없음, 객체 관리 실수 감소, 안정적인 메모리 재활용<br />단점 : Old&nbsp;영역&nbsp;GC는&nbsp;시간이&nbsp;오래&nbsp;걸려&nbsp;성능&nbsp;문제로&nbsp;이어질&nbsp;수&nbsp;있음</td>
</tr>
<tr id="2b5435fc-bd9d-80bd-ba0e-fd1dd66b2a8f" style="height: 21px;">
<td id="BuIY" style="width: 15.9646%; height: 21px;">필요 조건</td>
<td id="tf]I" style="width: 83.9178%; height: 21px;">JVM&nbsp;힙&nbsp;영역&nbsp;구성(Young/Old),&nbsp;GC&nbsp;알고리즘&nbsp;선택(Serial/Parallel/G1/ZGC&nbsp;등),&nbsp;앱&nbsp;특성에&nbsp;맞는&nbsp;튜닝</td>
</tr>
<tr id="2b5435fc-bd9d-8060-8329-cf643643c56b" style="height: 23px;">
<td id="BuIY" style="width: 15.9646%; height: 23px;">예시/비교</td>
<td id="tf]I" style="width: 83.9178%; height: 23px;">C/C++의&nbsp;수동&nbsp;메모리&nbsp;관리(malloc/free)와&nbsp;대비됨.&nbsp;Java는&nbsp;자동&nbsp;관리지만&nbsp;개발자가&nbsp;구조를&nbsp;모르면&nbsp;성능&nbsp;문제가&nbsp;발생할&nbsp;수&nbsp;있음.</td>
</tr>
</tbody>
</table>
<hr contenteditable="false" />
<p style="text-align: left;"><b><span>Interview Answer Version (면접 답변식 요약)<br /></span></b></p>
<p style="text-align: left;">Java&nbsp;Garbage&nbsp;Collection은&nbsp;더&nbsp;이상&nbsp;참조되지&nbsp;않는&nbsp;객체를&nbsp;자동으로&nbsp;정리해&nbsp;메모리를&nbsp;회수하는&nbsp;JVM&nbsp;기능입니다.&nbsp;Young/Old&nbsp;Generation&nbsp;구조에서&nbsp;객체&nbsp;생존&nbsp;기간에&nbsp;따라&nbsp;Minor/&nbsp;Major&nbsp;GC가&nbsp;발생하며,&nbsp;Root&nbsp;Reachability&nbsp;분석을&nbsp;통해&nbsp;실제로&nbsp;필요한&nbsp;객체만&nbsp;남깁니다.&nbsp;자동&nbsp;메모리&nbsp;관리의&nbsp;장점이&nbsp;있지만&nbsp;GC&nbsp;시에는&nbsp;Stop-the-world가&nbsp;발생할&nbsp;수&nbsp;있어,&nbsp;성능&nbsp;최적화를&nbsp;위해&nbsp;적절한&nbsp;GC&nbsp;알고리즘&nbsp;선택과&nbsp;메모리&nbsp;구조&nbsp;이해가&nbsp;중요합니다.</p>
<hr contenteditable="false" />
<p style="text-align: left;"><b>Practical&nbsp;Tip&nbsp;(사용시&nbsp;주의할&nbsp;점&nbsp;or&nbsp;활용&nbsp;예)</b></p>
<p style="color: #333333; text-align: start;">- STW가 성능 문제의 핵심 <br />Old 영역이 꽉 차면 Major GC 발생 -&gt; 서버 응답 지연, 실시간&nbsp;애플리케이션이라면&nbsp;G1&nbsp;GC&nbsp;or&nbsp;ZGC&nbsp;사용&nbsp;고려 <br /><br />- 객체를 너무 많이 생성하는 패턴 피하기 <br />매 요청마다 String 객체 수백개 생성, Eden&nbsp;영역&nbsp;과도한&nbsp;사용&nbsp;-&gt;&nbsp;Minor&nbsp;GC&nbsp;빈번&nbsp;-&gt;&nbsp;CPU&nbsp;상승 <br /><br />- Spring Boot 환경에서 자주 겪는 문제 <br />Batch 처리나 대량 JSON 파싱 시 Old 영역 급격한 증가, 잦은&nbsp;Full&nbsp;GC&nbsp;-&gt;&nbsp;응답&nbsp;시간&nbsp;튐&nbsp;-&gt;&nbsp;모니터링&nbsp;필요</p>
<hr contenteditable="false" />
<p style="color: #333333; text-align: start;"><b>예상&nbsp;꼬리질문&nbsp;정리</b><br /><br />1. Minor GC와 Major GC의 차이점은 무엇인가요?</p>
<p style="color: #333333; text-align: start;"><br />2. Stop-the-world는 왜 발생하고, 어떻게 줄일 수 있나요?</p>
<p style="color: #333333; text-align: start;"><br />3. G1 GC와 Parallel GC의 차이점은? 실무에서는 어떤 기준으로 선택하나요?</p>
<p style="color: #333333; text-align: start;"><br />4. Java에서 메모리 누수가 발생하는 예시는?</p>
<hr contenteditable="false" />
<p style="color: #333333; text-align: start;">&nbsp;</p>
<p style="color: #333333; text-align: start;">1.&nbsp;Minor&nbsp;GC는&nbsp;Young&nbsp;영역에서&nbsp;빠르고&nbsp;가벼운&nbsp;정리,&nbsp;Major&nbsp;GC는&nbsp;Old&nbsp;영역&nbsp;중심으로&nbsp;느리고&nbsp;무거운&nbsp;STW를&nbsp;유발합니다 <br /><br />2.&nbsp;STW는&nbsp;GC의&nbsp;참조&nbsp;분석을&nbsp;안전하게&nbsp;수행하기&nbsp;위해&nbsp;모든&nbsp;스레드를&nbsp;멈추는&nbsp;과정이고,&nbsp;최신&nbsp;GC&nbsp;알고리즘&nbsp;사용과&nbsp;Heap/객체&nbsp;생성&nbsp;최적화로&nbsp;줄일&nbsp;수&nbsp;있습니다 <br /><br />3.&nbsp;Parallel&nbsp;GC는&nbsp;처리량&nbsp;중심,&nbsp;G1은&nbsp;지연시간&nbsp;중심입니다.&nbsp;API&nbsp;서버는&nbsp;G1,&nbsp;배치/고성능&nbsp;처리&nbsp;위주&nbsp;환경은&nbsp;Parallel이&nbsp;적합합니다 <br /><br />4.&nbsp;참조가&nbsp;남아&nbsp;있는&nbsp;객체는&nbsp;GC가&nbsp;절대&nbsp;지우지&nbsp;못하기&nbsp;때문에,&nbsp;static&nbsp;컬렉션&middot;ThreadLocal&middot;콜백&nbsp;누락&nbsp;등이&nbsp;대표적인&nbsp;메모리&nbsp;누수&nbsp;원인입니다 <br /><br /><br /></p>