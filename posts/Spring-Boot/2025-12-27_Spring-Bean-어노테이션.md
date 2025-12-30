# Spring Bean 어노테이션

**카테고리**: Spring Boot

**작성일**: Sat, 27 Dec 2025 13:24:07 +0900

**원문 링크**: https://junsseok.tistory.com/70

---

<p style="text-align: center;">Spring Bean 어노테이션</p>
<hr contenteditable="false" />
<p style="text-align: center;">Spring Bean에 등록하는 방식이 두가지가 있는데 하나는 Java Config 방식, 그리고 어노테이션 기반을 사용합니다.</p>
<p style="text-align: center;">어노테이션 기반이 Bean 등록에 가장 많이 사용하는 방식입니다.</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">어노테이션 방식이 가독성이 좋고 유지보수가 쉬우며 Spring Boot의 기본방식이라고 할 수 있습니다.</p>
<p style="text-align: center;"><br />Spring Bean 어노테이션은 클래스를 자동으로 Spring 컨테이너에 등록해서</p>
<p style="text-align: center;">Bean으로 관리하게 해주는 표시입니다.</p>
<hr contenteditable="false" />
<h3 style="text-align: left;">핵심 어노테이션</h3>
<p><b>1. @Component :&nbsp;</b></p>
<p>가장 기본적인 Bean 어노테이션이입니다.</p>
<p>&nbsp;</p>
<p>역할 :&nbsp;</p>
<p>- 어떤 계층에도 속하지 않는 일반 Bean입니다.</p>
<p>- 공통 기능, 유틸성 클래스에 주로 사용됩니다.</p>
<p>&nbsp;</p>
<p>특징 :&nbsp;</p>
<p>- Spring이 자동으로 감지하여 Bean으로 등록합니다.</p>
<p>- 아래의 모든 어노테이션들의 상위 개념입니다.</p>
<pre class="bash" id="code_1766731566198"><code>@Component
public class MyComponent { }</code></pre>
<p>&nbsp;</p>
<p>사용&nbsp;예&nbsp;:&nbsp; <br />-&nbsp;공통&nbsp;로직 <br />-&nbsp;유틸&nbsp;클래스 <br />-&nbsp;특정&nbsp;계층으로&nbsp;분류하기&nbsp;애매한&nbsp;경우</p>
<hr contenteditable="false" />
<p><b>2. @Service :</b></p>
<p>비즈니스 로직을 담당하는 서비스 계층의 Bean 어노테이션입니다.</p>
<p>&nbsp;</p>
<p>역할 :&nbsp;</p>
<p>- 애플리케이션의 핵심 비즈니스 로직을 처리합니다.</p>
<p>- Controller와 Repository 사이에서 동작합니다.</p>
<p>&nbsp;</p>
<p>특징 :&nbsp;</p>
<p>- Component와 기능은 동일하지만, 의미적으로 서비스 계층임을 명확히 표현합니다.</p>
<p>- 트랜잭션, 로깅 등 AOP 적용의 주요 대상입니다.</p>
<pre class="bash" id="code_1766733240461"><code>@Service
public class UserService {

    public void register(User user) {
        // 비즈니스 로직 처리
    }
}</code></pre>
<hr contenteditable="false" />
<p><b>3. @Repository :&nbsp;</b><b></b></p>
<p>데이터 접근 계층(DAO)를 담당하는 Bean 어노테이션입니다.</p>
<p>&nbsp;</p>
<p>역할 :&nbsp;</p>
<p>- 데이터베이스와 직접 통신하는 역할을 합니다.</p>
<p>- CRUD 처리 및 쿼리 실행을 담당합니다.</p>
<p>&nbsp;</p>
<p>특징 :&nbsp;</p>
<p>- DB관련 예외를 Spring의 DataAccessException으로 변환해줍니다.</p>
<p>- 데이터 접근 계층임을 명확하게 표현합니다.</p>
<p>- DB 기술 변경시 코드 의존성이 낮아집니다.</p>
<p>- 예외처리가 일관되게 관리됩니다.</p>
<pre class="bash" id="code_1766733371741"><code>@Repository
public class UserRepository {
}</code></pre>
<hr contenteditable="false" />
<p><b>4. @Controller :&nbsp;</b></p>
<p>웹 요청을 처리하는 컨트롤러 계층의 Bean 어노테이션입니다.</p>
<p>&nbsp;</p>
<p>역할 :&nbsp;</p>
<p>- 클라이언트의 HTTP 요청을 받아 처리합니다.</p>
<p>- 처리 결과를 View 이름으로 반환합니다.</p>
<p>&nbsp;</p>
<p>특징 :&nbsp;</p>
<p>- JSP, Thymeleaf 등 View 기반 MVC 구조에서 사용됩니다.</p>
<p>- Model 객체를 통해 데이터를 전달합니다.</p>
<pre class="bash" id="code_1766733464917"><code>@Controller
public class UserController {

    @GetMapping("/login")
    public String loginPage() {
        return "login";
    }
}</code></pre>
<hr contenteditable="false" />
<p><b> 5. @RestController :</b></p>
<p>REST API 전용 컨트롤러 어노테이션입니다.</p>
<p>&nbsp;</p>
<p>역할 :&nbsp;</p>
<p>- HTTP 요청을 처리하고 데이터를 JSON 형태로 반환합니다.</p>
<p>&nbsp;</p>
<p>특징 :</p>
<p>- View를 반환하지 않고 데이터만 응답합니다.</p>
<pre class="bash" id="code_1766733649173"><code>@RestController
public class UserApiController {

    @GetMapping("/users")
    public List&lt;User&gt; users() {
        return userService.findAll();
    }
}</code></pre>
<p>사용 예 :&nbsp;</p>
<p>- REST API 서버</p>
<p>- 프론트엔드와 JSON 기반 통신</p>
<hr contenteditable="false" />
<h3>정리</h3>
<p>모든 어노테이션은 Spring Bean으로 등록됩니다.</p>
<p>- 기능적인 차이는 없으며, 역할과 의도를 명확히 구분 하기 위해서입니다.</p>
<pre class="bash" id="code_1766733730293"><code>@Component
 ├─ @Service
 ├─ @Repository
 └─ @Controller
      └─ @RestController</code></pre>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><b>- @Component</b><br />-&gt; 특정 계층에 속하지 않는 일반적인 Spring 관리 객체입니다.</p>
<p>- <b>@Service</b><br /><span style="color: #333333; text-align: start;">-&gt;<span>&nbsp;</span></span> 비즈니스 로직을 담당하는 서비스 계층의 Bean입니다.</p>
<p><b>- @Repository</b><br /><span style="color: #333333; text-align: start;">-&gt;<span>&nbsp;</span></span> 데이터베이스 접근을 담당하며, DB 예외를 Spring 예외로 변환해주는 Bean입니다.</p>
<p><b>- @Controller</b><br /><span style="color: #333333; text-align: start;">-&gt;<span>&nbsp;</span></span> HTTP 요청을 받아 View를 반환하는 웹 컨트롤러 Bean입니다.</p>
<p><b>- @RestController</b><br /><span style="color: #333333; text-align: start;">-&gt;<span>&nbsp;</span></span> HTTP 요청을 처리하고 데이터를 JSON 형태로 반환하는 REST API 전용 컨트롤러입니다.</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">면접한줄정리</h3>
<p style="text-align: center;">Spring Bean 어노테이션은 각 클래스의 역할과 계층을 명확히 표현하기 위한 설계 도구입니다.</p>