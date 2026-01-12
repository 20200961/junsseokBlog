# spring MVC

**카테고리**: Spring Boot

**작성일**: Mon, 12 Jan 2026 20:23:40 +0900

**원문 링크**: https://junsseok.tistory.com/77

---

<p style="text-align: center;">spring MVC</p>
<hr contenteditable="false" />
<p style="text-align: center;">Spring MVC는 Spring Framework에서 제공하는 웹 애플리케이션 개발을 위한 MCV 기반 프레임워크입니다.</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">주로 Java로 웹서비스(웹페이지, REST API)를 만들 때 사용됩니다.</p>
<hr contenteditable="false" />
<h3 style="text-align: left;">MVC 패턴</h3>
<p>Spring MVC를 이해하려면 먼저 MVC 패턴을 알아야 합니다.</p>
<p>&nbsp;</p>
<p>MVC 패턴은 애플리케이션을 개발할 때 사용하는 디자인 패턴으로,</p>
<p>애플리케이션 개발 영역을 MVC로 구분하여 각 역할에 맞게 코드를 작성하는 개발 방식이다.</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><b>Model</b> : 비즈니스 로직, 데이터 처리(Service, DAO, Entity 등)</p>
<p style="text-align: left;">&gt; 애플리케이션의 핵심 규칙과 데이터를 관리하는 영역</p>
<p style="text-align: left;"><b>View</b> : 사용자에게 보여지는 화면(JSP, JSON 등)</p>
<p style="text-align: left;">- 사용자에게 결과를 전달하는 출력 영역</p>
<p style="text-align: left;"><b>Controller</b> : 요청을 받아 처리하고 Model과 View를 연결</p>
<p style="text-align: left;">- Model과 View를 연결하는 중간 제어자 역할</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><b>MVC 패턴의 장점</b></p>
<p style="text-align: left;">- 역할 분리를 통해 유지보수성 향상</p>
<p style="text-align: left;">- 각 계층이 독립적이어서 확장성과 테스트 용이</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: center;"><b>역할 분리를 통해 유지보수성과 확장성을 높입니다.</b></p>
<hr contenteditable="false" />
<h3 style="text-align: left;">Spring MVC</h3>
<p>Spring MVC는 MVC 패턴을 Spring Framework 차원에서 구현한 웹 프레임워크입니다.</p>
<p>요청부터 응답까지의 흐름을 체계적으로 관리하여 개발자가 비즈니스 로직에 집중할 수 있도록 구조를 제공합니다.</p>
<p>&nbsp;</p>
<p>모든 클라이언트의 요청은 하나의 진입점으로 모이고, 그 이후에 적절한 Controller로 분기되어 처리됩니다.</p>
<p>동작 흐름은 다음과 같습니다.</p>
<p><figure class="imageblock alignCenter"><span><img height="477" src="https://blog.kakaocdn.net/dn/Oe8we/dJMcagRLnPY/wQDHs470tFqH6RTIKMFkwk/img.png" width="716" /></span></figure>
</p>
<p style="text-align: left;"><b> Spring MVC의 요청 처리 흐름</b><b></b></p>
<p style="text-align: left;">1. 클라이언트가 <b>요청(Request)</b> 전송</p>
<p style="text-align: left;">2. <b>DispatcherServlet</b>이 요청 수신</p>
<p style="text-align: left;">&nbsp; &nbsp; -&gt; 모든 요청의 진입점(Front Controller)</p>
<p style="text-align: left;">3. <b>HandlerMapping</b>을 통해 요청 URL에 매핑된 Controller 탐색</p>
<p style="text-align: left;">&nbsp; &nbsp; -&gt; @RequestMapping, @GetMapping 등의 정보를 기반으로 어떤 Controller 메서드가 이 요청을 처리할지 결정</p>
<p style="text-align: left;">4. <b>HandlerAdapter</b>가 <b>Controller</b>메서드 실행</p>
<p style="text-align: left;">&nbsp; &nbsp; -&gt; 선택된 Controller를 실제로 호출</p>
<p style="text-align: left;">5. <b>Controller</b> 메서드 실행</p>
<p style="text-align: left;">&nbsp; &nbsp; -&gt; 요청 파라미터 처리</p>
<p style="text-align: left;">&nbsp; &nbsp; -&gt; Service 계층 호출</p>
<p style="text-align: left;">6. <b>Service</b> -&gt; <b>Repository</b> -&gt; <b>DB 처리</b></p>
<p style="text-align: left;">7. 처리 결과 반환(Model 또는 데이터)</p>
<p style="text-align: left;">8. <b>View Resolver</b>가 <b>View</b> 결정</p>
<p style="text-align: left;">&nbsp; &nbsp; -&gt; JSP 또는 JSON 응답</p>
<p style="text-align: left;">9. <b>응답(Response)</b> 반환</p>
<hr contenteditable="false" />
<p style="text-align: left;"><b>DisptcherServlet</b></p>
<p style="text-align: left;">Spring MVC에서 모든 요청의 시작점은 DispatcherServlet입니다.</p>
<p style="text-align: left;">-&nbsp;클라이언트의&nbsp;모든&nbsp;HTTP&nbsp;요청을&nbsp;가장&nbsp;먼저&nbsp;받음 <br />-&nbsp;요청&nbsp;URL에&nbsp;맞는&nbsp;Controller를&nbsp;찾음 <br />-&nbsp;Controller&nbsp;실행&nbsp;결과를&nbsp;View로&nbsp;전달 <br />-&nbsp;최종&nbsp;응답(Response)을&nbsp;생성하여&nbsp;반환</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><b>=&gt; 요청 처리의 전체 흐름을 제어하는 중앙 컨트롤러 역할</b></p>
<hr contenteditable="false" />
<p style="text-align: left;"><b> Controller 처리 과정 </b></p>
<p style="text-align: left;">-&nbsp;요청&nbsp;파라미터&nbsp;수신 <br />-&nbsp;Service&nbsp;호출 <br />-&nbsp;처리&nbsp;결과를&nbsp;반환</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><b>=&gt; 흐름&nbsp;제어&nbsp;역할에만&nbsp;집중하고,&nbsp;비즈니스&nbsp;로직은&nbsp;Model&nbsp;영역에서&nbsp;관리됩니다.</b></p>
<hr contenteditable="false" />
<p><b> HandlerMapping</b></p>
<p>Spring MVC에서 URL과 Controller를 연결하는 핵심 컴포넌트입니다.</p>
<p>- URL을 기준으로 Controller를 직접 호출하지 않음</p>
<p>- 매핑 정보를 통해 유연한 처리 구조 제공</p>
<p>&nbsp;</p>
<p><b>=&gt; 위 코드가 동작하는 이유가 바로 HandlerMapping 덕분입니다</b></p>
<hr contenteditable="false" />
<p><b> View Resolver </b></p>
<p>-&nbsp;JSP,&nbsp;Thymeleaf&nbsp;같은&nbsp;템플릿&nbsp;View <br />-&nbsp;REST&nbsp;API의&nbsp;경우&nbsp;JSON&nbsp;형태의&nbsp;응답</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><b>=&gt; Controller가 처리 결과를 반환하면 Spring MVC는 View Resolver를 통해 실제 View를 결정합니다.</b></p>
<hr contenteditable="false" />
<h3 style="text-align: left;">Spring MVC의 특징 정리</h3>
<p style="text-align: left;">-&nbsp;MVC&nbsp;패턴&nbsp;기반의&nbsp;명확한&nbsp;구조 <br />-&nbsp;요청&nbsp;흐름의&nbsp;중앙&nbsp;집중&nbsp;관리 <br />-&nbsp;비즈니스&nbsp;로직과&nbsp;화면&nbsp;로직&nbsp;분리 <br />-&nbsp;Spring&nbsp;생태계(JPA,&nbsp;Security&nbsp;등)와의&nbsp;높은&nbsp;호환성</p>
<hr contenteditable="false" />
<h3 style="text-align: left;">마무리</h3>
<p style="text-align: left;">Spring&nbsp;MVC는&nbsp;단순히&nbsp;웹&nbsp;페이지를&nbsp;만드는&nbsp;도구가&nbsp;아니라,&nbsp;</p>
<p style="text-align: left;">유지보수성과&nbsp;확장성을&nbsp;고려한&nbsp;서버&nbsp;아키텍처를&nbsp;제공하는&nbsp;프레임워크입니다. <br /><br />Spring MVC를 이해하면 Spring Boot, REST API, 대규모 웹 서비스 구조를 더 쉽게 이해하고 설계할 수 있습니다!!</p>