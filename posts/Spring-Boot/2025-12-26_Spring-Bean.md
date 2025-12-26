# Spring Bean

**카테고리**: Spring Boot

**작성일**: Fri, 26 Dec 2025 14:49:48 +0900

**원문 링크**: https://junsseok.tistory.com/69

---

<p style="text-align: center;">Spring Bean</p>
<hr contenteditable="false" />
<p style="text-align: center;">Spring Bean이란 <b>Spring 컨테이너가 생성하고 관리하는 객체(Object)</b>를 의미합니다.</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">우리가 new로 직접 만드는 객체가 아니라 Spring이 대신 생성하고, 의존성 주입(DI)과 생명주기를</p>
<p style="text-align: center;">관리해주는 객체가 Bean입니다.</p>
<hr contenteditable="false" />
<h3 style="text-align: left;">사용하는 이유</h3>
<p>(1) 객체 관리의 일관성</p>
<p>- 객체 생성, 초기화, 소멸을 Spring이 담당</p>
<p>- 개발자는 비즈니스 로직에만 집중</p>
<p>&nbsp;</p>
<p>(2) 의존성 주입(DI) 가능</p>
<p>- 객체간 결합도 감소</p>
<p>- 테스트, 유지보수 용이</p>
<p>&nbsp;</p>
<p>(3) 싱글톤 관리 자동</p>
<p>- 기본적으로 한 개의 객체만 생성하여 사용</p>
<hr contenteditable="false" />
<h3>Spring Bean 등록 방법</h3>
<p>(1) 어노테이션 기반(가장 많이 사용)</p>
<pre class="bash" id="code_1766726286461"><code>@Component
public class MemberService {
}</code></pre>
<p>&nbsp;</p>
<p>-&gt; Bean 등록 어노테이션</p>
<p>- @Component : 일반적인 Bean</p>
<p>- @Service : 비즈니스 로직 계층</p>
<p>- @Repository : 데이터 접근 계층(예외 변환 기능 포함)</p>
<p>- @Controller : 웹 요청 처리</p>
<p>&nbsp;</p>
<p>--&gt; 내부적으로는 전부 @Component 기반</p>
<p>&nbsp;</p>
<p>(2) Java Config 방식</p>
<pre class="bash" id="code_1766726308060"><code>@Configuration
public class AppConfig {

    @Bean
    public MemberService memberService() {
        return new MemberService();
    }
}</code></pre>
<p>-&gt; 외부 라이브러리 객체를 Bean으로 등록할 때 유용</p>
<p>&nbsp;</p>
<p>(3) Spring Bean 생명주기</p>
<p>&nbsp;</p>
<p><figure class="imageblock alignCenter"><span><img height="483" src="https://blog.kakaocdn.net/dn/M1dUQ/dJMcaiWcAYw/RpbZnLpQWW6vvOwpugYyr1/img.png" width="725" /></span></figure>
</p>
<p><b>Bean Instantiation</b><br />&rarr; Spring이 Bean 객체를 생성한다.</p>
<p><b>Dependency Injection(DI)</b><br />&rarr; 필요한 의존 객체들을 자동으로 주입한다.</p>
<p><b>Aware Interfaces (Optional)</b><br />&rarr; Bean이 Spring 컨테이너 정보를 인식한다.</p>
<p><b>BeanPostProcessor (Before Init)</b><br />&rarr; 초기화 전에 공통 처리 로직이 실행된다.</p>
<p><b>Initialization</b><br />&rarr; Bean 사용을 위한 초기 설정을 수행한다.</p>
<p><b>BeanPostProcessor (After Init)</b><br />&rarr; AOP 프록시 등 확장 기능이 적용된다.</p>
<p><b>Bean Ready for Use</b><br />&rarr; 비즈니스 로직에서 Bean이 사용된다.</p>
<p><b>Destruction</b><br />&rarr; 컨테이너 종료 시 자원을 정리하며 Bean이 소멸된다.</p>
<p>&nbsp;</p>
<p>(4) Bean Scope&nbsp;</p>
<p>- Singleton : 기본값, 컨테이너당 1개</p>
<p>- prototype : 요청시마다 새 객체</p>
<p>- request : HTTP 요청당 1개</p>
<p>- session : HTTP 세션당 1개</p>
<p>&nbsp;</p>
<p>(5) Bean vs 일반 객체 차이</p>
<p><figure class="imageblock alignCenter"><span><img height="218" src="https://blog.kakaocdn.net/dn/cTXrlF/dJMcagRECg7/kdpXSy6P8R1m1UkOa7ifzk/img.png" width="598" /></span></figure>
</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">면접한줄요약</h3>
<p style="text-align: center;">Spring Bean이란 Spring 컨테이너에 의해 생성, 관리되며, 의존성 주입과 생명주기를 관리받는 객체입니다.</p>