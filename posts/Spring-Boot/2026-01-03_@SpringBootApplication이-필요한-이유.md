# @SpringBootApplication이 필요한 이유

**카테고리**: Spring Boot

**작성일**: Sat, 3 Jan 2026 20:39:35 +0900

**원문 링크**: https://junsseok.tistory.com/72

---

<p style="text-align: center;">@SpringBootApplication이 필요한 이유</p>
<hr contenteditable="false" />
<p style="text-align: center;">Spring Boot로 프로젝트를 시작하면 메인 클래스에 항상 @SpringBootApplication이 붙어있는 걸 볼 수 있습니다.</p>
<p style="text-align: center;">다음과 같은 이유에서 사용합니다.</p>
<hr contenteditable="false" />
<h3 style="text-align: left;">기본 구조</h3>
<p>처음 Spring Boot 프로젝트를 생성하면 이런 코드를 볼 수 있습니다.</p>
<p>단순해 보이지만 @SpringBootApplication 하나로 많은 설정이 자동 처리됩니다.</p>
<pre class="bash" id="code_1767439274687"><code>@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}</code></pre>
<p>&nbsp;</p>
<p><span style="color: #333333; text-align: start;">@SpringBootApplication은 사실 세개의 어노테이션을 합친 것입니다.</span></p>
<hr contenteditable="false" />
<h3>세가지 핵심 기능</h3>
<p><b> 1. @SpringBootConfiguration</b><b></b></p>
<p>&nbsp;</p>
<p>이 어노테이션은 @Configuration의 대안으로, 해당 클래스가 Spring의 설정 클래스임을 나타냅니다.</p>
<p>여기서 Bean을 정의하고 애플리케이션의 설정을 관리할 수 <span style="color: #000000;">있습니다.</span></p>
<p>&nbsp;</p>
<p>- 왜 @Configuration이 아니라 @SpringBootConfiguration일까?</p>
<p>기술적으로는 거의 동일하지만, Spring Boot는 애플리케이션 전체에서 딱 하나의 @SpringBootConfiguration만 가지도록 권장합니다. 이를 통해 Spring Boot는 테스트 시 설정 클래스를 자동으로 찾을 수 있고, 애플리케이션의 루트 설정을 명확하게 식별할 수 있습니다.</p>
<pre class="bash" id="code_1767439636851"><code>@SpringBootApplication
public class MyApplication {
    
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
    
    @Bean
    public ObjectMapper objectMapper() {
        return new ObjectMapper();
    }
}</code></pre>
<p>-&gt; 이렇게 정의한 Bean들은 애플리케이션 전체에서 주입받아 사용할 수 있습니다.</p>
<p>&nbsp;</p>
<p><b><span style="color: #383a42;">2. @EnableAutoConfiguration</span> </b></p>
<p>Spring Boot의 핵심 기능입니다. 클래스패스에 있는 라이브러리를 분석해서 필요한 설정을 자동으로 구성해줍니다.</p>
<p>동작 방식:</p>
<p>Spring Boot는 spring-boot-autoconfigure 라이브러리 안에 있는 수많은 자동 설정 클래스들을 가지고 있습니다. 이 클래스들은 조건부로 활성화됩니다.</p>
<p>&nbsp;</p>
<p><b>예를 들어:</b><br />(1) spring-boot-starter-web 의존성이 있으면 -&gt; WebMvcAutoConfiguration이 실행되어</p>
<p>DispatcherServlet, ViewResolver 등을 자동 설정<br />(2) spring-boot-starter-data-jpa 의존성이 있으면 -&gt; HibernateJpaAutoConfiguration이 실행되어 EntityManagerFactory, DataSource, TransactionManager 등을 자동 설정</p>
<pre class="bash" id="code_1767439689281"><code>@ConditionalOnClass(DataSource.class) // DataSource 클래스가 있을 때만
@ConditionalOnMissingBean(DataSource.class) // 이미 정의된 Bean이 없을 때만
public class DataSourceAutoConfiguration {
    // 자동 설정 로직
}</code></pre>
<p><span style="color: #383a42;"> <span><span>이런 조건들로 인해 필요한 것만 자동으로 설정되고</span><span style="color: #383a42;">,</span><span> 개발자가 직접 정의한 설정은 우선권을 가집니다</span><span style="color: #383a42;">.</span><span>&nbsp;</span></span></span></p>
<p>&nbsp;</p>
<p><b><span style="color: #383a42;">3. <span style="color: #383a42;">@ComponentScan</span><span> </span> </span></b></p>
<p><span style="color: #333333;"> 이 어노테이션이 붙은 클래스가 위치한 패키지를 기준으로 하위 패키지들을 스캔합니다. @Component, @Service, @Repository, @Controller 같은 어노테이션이 붙은 클래스들을 찾아서 자동으로 Bean으로 등록해줍니다.</span><span style="color: #333333;"></span></p>
<pre class="bash" id="code_1767439886218"><code>com.example.myapp
├── MyApplication.java (@SpringBootApplication)
├── controller
│   └── UserController.java (@Controller)
├── service
│   └── UserService.java (@Service)
└── repository
    └── UserRepository.java (@Repository)</code></pre>
<p>- 이런 구조에서 MyApplication을 실행하면 하위의 모든 컴포넌트들이 자동으로 스캔되어 등록됩니다.</p>
<hr contenteditable="false" />
<h3>필요한 이유</h3>
<p><b>편의성</b></p>
<p>과거 Spring에서는 XML 설정 파일에 수많은 Bean 정의와 설정을 작성해야 했습니다. 하지만 @SpringBootApplication 하나로 대부분의 기본 설정이 자동화됩니다.</p>
<p>&nbsp;</p>
<p><b>일관성</b></p>
<p>모든 Spring Boot 프로젝트가 같은 시작점을 가지게 됩니다. 팀원들과 협업할 때나 새로운 프로젝트를 시작할 때 익숙한 구조로 바로 작업을 시작할 수 있습니다.</p>
<p>&nbsp;</p>
<p><b>빠른 개발</b></p>
<p>설정에 시간을 쓰는 대신 비즈니스 로직 개발에 집중할 수 있습니다. 필요한 라이브러리만 추가하면 대부분의 설정이 자동으로 처리됩니다.</p>
<hr contenteditable="false" />
<h3>개인화 가능</h3>
<p>기본 동작이 마음에 들지 않으면 조정할 수 있습니다.</p>
<pre class="bash" id="code_1767439969171"><code>@SpringBootApplication(
    scanBasePackages = "com.example.custom",
    exclude = DataSourceAutoConfiguration.class
)
public class MyApplication {
    // ...
}</code></pre>
<p>-&gt; 이런식으로 특정 패키지만 스캔하거나, 특정 자동 설정을 제외할 수 있습니다.</p>
<hr contenteditable="false" />
<h3>마무리</h3>
<p>@SpringBootApplication은 단순한 어노테이션처럼 보이지만, Spring Boot의 철학을 담고 있습니다. 개발자가 설정보다는 개발에 집중할 수 있도록 도와주는 강력한 도구입니다. Spring Boot를 사용한다면 이 어노테이션의 역할을 이해하고 있는 것이 중요합니다.</p>
<p>&nbsp;</p>