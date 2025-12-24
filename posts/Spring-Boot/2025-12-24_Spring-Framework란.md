# Spring Framework란?

**카테고리**: Spring Boot

**작성일**: Wed, 24 Dec 2025 14:19:50 +0900

**원문 링크**: https://junsseok.tistory.com/68

---

<p style="text-align: center;">Spring&nbsp;Framework</p>
<hr contenteditable="false" />
<p style="text-align: center;">스프링 프레임워크(Spring Framework)는</p>
<p style="text-align: center;">자바 기반 엔터프라이즈 애플리케이션을 개발하기 위한 프레임워크입니다.</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><span style="background-color: #ffffff; color: #333d42; text-align: start;">의존성 주입, MVC, Security, JDBC 등과 같은 특수 구성 요소를 포함하여 많은 기능을 제공하는 프레임워크입니다.</span></p>
<hr contenteditable="false" />
<h3 style="text-align: left;">등장 배경</h3>
<p>Spring Framework 이전에 엔터프라이즈 개발은 Java EE(EJB) 기반이었는데 문제점이 많았습니다.</p>
<p>(1) 설정이 너무 복잡함 (XML 지옥)</p>
<p><span style="color: #333333; text-align: start;">(2)<span>&nbsp;</span></span> 특정 서버(WebLogic 등)에 강하게 의존</p>
<p><span style="color: #333333; text-align: start;">(3)<span>&nbsp;</span></span> 테스트 어려움 (컨테이너 없으면 실행 불가)</p>
<p><span style="color: #333333; text-align: start;">(4)<span>&nbsp;</span></span> 객체 지향 설계가 무너짐</p>
<p>&nbsp;</p>
<p>위와 같은 문제점이 생겨 비즈니스 로직에 집중하기 어렵다는 단점이 있었습니다.</p>
<hr contenteditable="false" />
<p><span style="color: #333333; text-align: start;">Spring Framework는</span> 다음의 장점을 가지고 등장하였습니다.</p>
<p>(1)&nbsp;POJO(순수&nbsp;자바&nbsp;객체)&nbsp;중심&nbsp;개발 <br />(2)&nbsp;컨테이너&nbsp;종속성&nbsp;제거 <br />(3)&nbsp;객체&nbsp;간&nbsp;결합도&nbsp;감소 <br />(4)&nbsp;테스트&nbsp;친화적&nbsp;구조&nbsp;제공</p>
<hr contenteditable="false" />
<h3>핵심 개념</h3>
<p>Spring Framework는 몇 가지 핵심 개념을 바탕으로 동작합니다.</p>
<p>&nbsp;</p>
<p><b>1. IoC (Inversion of Control, 제어의 역전)</b></p>
<p>기존에는 개발자가 직접 객체를 생성하고 관리했습니다. 하지만 IoC 패턴에서는 Spring 컨테이너가 객체의 생성과 생명주기를 관리합니다. 개발자는 필요한 객체를 요청만 하면 되므로 객체 관리의 부담이 줄어듭니다.</p>
<p>&nbsp;</p>
<p><b>2. DI (Dependency Injection, 의존성 주입)</b></p>
<p>DI는 IoC를 구현하는 핵심 방법입니다. 객체 간의 의존 관계를 코드 내부가 아닌 외부(Spring 컨테이너)에서 설정합니다. 이를 통해 결합도가 낮아지고 코드의 재사용성과 테스트 용이성이 높아집니다.</p>
<p>&nbsp;</p>
<p><b>3. AOP (Aspect-Oriented Programming, 관점 지향 프로그래밍)</b></p>
<p>AOP는 공통 관심사(로깅, 보안, 트랜잭션 등)를 비즈니스 로직에서 분리하여 관리하는 기법입니다. 핵심 비즈니스 로직과 부가 기능을 분리함으로써 코드의 중복을 줄이고 유지보수성을 높일 수 있습니다.</p>
<p>&nbsp;</p>
<p><b>4. PSA (Portable Service Abstraction, 이식 가능한 서비스 추상화)</b></p>
<p>PSA는 환경과 세부 기술의 변화에 관계없이 일관된 방식으로 기술에 접근할 수 있게 해주는 설계 원칙입니다. 예를 들어 데이터베이스를 MySQL에서 Oracle로 변경하더라도 코드 수정을 최소화할 수 있습니다.</p>
<p><figure class="imageblock alignCenter"><span><img height="468" src="https://blog.kakaocdn.net/dn/bunNdS/dJMcaajAu38/Z1ItmkpBdKIQ8pkt7BT4M0/img.png" width="702" /></span></figure>
</p>
<hr contenteditable="false" />
<h3>Spring Framework의 주요 모듈</h3>
<p>Spring&nbsp;Framework는&nbsp;여러&nbsp;모듈로&nbsp;구성되어&nbsp;있으며,&nbsp;필요한&nbsp;모듈만&nbsp;선택하여&nbsp;사용할&nbsp;수&nbsp;있습니다.</p>
<p><br />(1) Spring Core : Spring의&nbsp;핵심&nbsp;기능인&nbsp;IoC와&nbsp;DI를&nbsp;제공하는&nbsp;모듈입니다.&nbsp;모든&nbsp;Spring&nbsp;애플리케이션의&nbsp;기반이&nbsp;됩니다. <br />(2) Spring MVC : 웹&nbsp;애플리케이션&nbsp;개발을&nbsp;위한&nbsp;Model-View-Controller&nbsp;패턴을&nbsp;지원하는&nbsp;모듈입니다.&nbsp;RESTful&nbsp;웹&nbsp;서비스&nbsp;개발에도&nbsp;활용됩니다. <br />(3) Spring Data Access/Integration : JDBC,&nbsp;ORM(Hibernate,&nbsp;JPA&nbsp;등),&nbsp;트랜잭션&nbsp;관리&nbsp;등&nbsp;데이터베이스&nbsp;연동&nbsp;기능을&nbsp;</p>
<p>제공합니다. <br />(4) Spring Security : 인증(Authentication)과&nbsp;인가(Authorization)&nbsp;기능을&nbsp;제공하여&nbsp;애플리케이션&nbsp;보안을&nbsp;강화합니다. <br />(5) Spring AOP : 관점&nbsp;지향&nbsp;프로그래밍을&nbsp;지원하는&nbsp;모듈입니다.</p>
<p><figure class="imageblock alignCenter"><span><img height="456" src="https://blog.kakaocdn.net/dn/bofDJU/dJMcagjNK6K/UIGQoEnLezjC6tHdRQa7HK/img.png" width="684" /></span></figure>
</p>
<hr contenteditable="false" />
<h3>Spring Boot와의 차이점</h3>
<p>Spring Framework를 사용하면 많은 설정 파일(XML 또는 Java Config)을 작성해야 했습니다.</p>
<p>Spring Boot는 이러한 복잡한 설정을 자동화하고 단순화한 것입니다.</p>
<p><br />(1) 자동 설정(Auto Configuration) : Spring&nbsp;Boot는&nbsp;classpath에&nbsp;있는&nbsp;라이브러리를&nbsp;기반으로&nbsp;자동으로&nbsp;설정을&nbsp;구성합니다. <br />(2) 내장 서버 : Tomcat,&nbsp;Jetty&nbsp;등의&nbsp;서버가&nbsp;내장되어&nbsp;있어&nbsp;별도의&nbsp;서버&nbsp;설치&nbsp;없이&nbsp;실행&nbsp;가능합니다. <br />(3) 독립 실행 가능 : jar&nbsp;파일&nbsp;하나로&nbsp;애플리케이션을&nbsp;실행할&nbsp;수&nbsp;있습니다.</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">면접한줄요약</h3>
<p style="text-align: center;"><b> Spring Framework는 IoC/DI 컨테이너를 제공하여 객체 지향적이고 테스트 용이한 </b></p>
<p style="text-align: center;"><b>자바 엔터프라이즈 애플리케이션 개발을 지원하는 경량 프레임워크입니다. </b></p>