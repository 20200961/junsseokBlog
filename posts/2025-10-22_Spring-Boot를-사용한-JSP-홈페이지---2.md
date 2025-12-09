# Spring Boot를 사용한 JSP 홈페이지 - 2

**작성일**: Wed, 22 Oct 2025 17:42:05 +0900

**원문 링크**: https://junsseok.tistory.com/35

---

<p style="text-align: center;">Spring Boot 필터, 인터셉터</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">Filter<span>&nbsp;</span></h3>
<h3 style="text-align: center;">&nbsp;</h3>
<p style="text-align: center;"><b>&nbsp;요청, 응답 전체를 감시하는 필터</b></p>
<p style="text-align: center;">모든&nbsp;HTTP&nbsp;요청에&nbsp;대해&nbsp;요청부터&nbsp;응답까지&nbsp;걸린&nbsp;시간(Log)을&nbsp;측정 <br />요청/응답&nbsp;전체&nbsp;흐름을&nbsp;감시할&nbsp;수&nbsp;있음&nbsp;(DispatcherServlet&nbsp;이전&nbsp;실행)</p>
<p style="text-align: center;">&nbsp;</p>
<pre class="bash" id="code_1761120971256"><code>@Slf4j
@Component
public class RequestTimeFilter implements Filter {

    @Override
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
            throws IOException, ServletException {

        HttpServletRequest request = (HttpServletRequest) req;
        HttpServletResponse response = (HttpServletResponse) res;

        long startTime = System.currentTimeMillis(); // 요청 시작 시간
        String method = request.getMethod();
        String fullUrl = request.getRequestURI() +
                         (request.getQueryString() != null ? "?" + request.getQueryString() : "");

        try {
            chain.doFilter(req, res); // 다음 필터 또는 컨트롤러 실행
        } finally {
            long endTime = System.currentTimeMillis();
            log.info("[{}] {} - Status: {} - duration: {}ms",
                     method, fullUrl, response.getStatus(), (endTime - startTime));
        }
    }
}</code></pre>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">-&gt; 실행 시점 &nbsp;: DispatcherServlet(스프링 컨트롤러) 호출 전 <br /><span style="color: #333333; text-align: left;">-&gt;<span>&nbsp;</span></span> 목적&nbsp;:&nbsp;요청&nbsp;시간&nbsp;측정,&nbsp;공통&nbsp;로깅,&nbsp;인코딩&nbsp;처리&nbsp;등 <br /><span style="color: #333333; text-align: left;">-&gt;<span>&nbsp;</span></span> 로그&nbsp;예시&nbsp;:&nbsp;[GET]&nbsp;/login.me&nbsp;-&nbsp;Status:&nbsp;200&nbsp;-&nbsp;duration:&nbsp;15ms <br /><span style="color: #333333; text-align: left;">-&gt;<span>&nbsp;</span></span> 등록&nbsp;방식&nbsp;:&nbsp;FilterRegistrationBean&nbsp;또는&nbsp;@Component <br /><span style="color: #333333; text-align: left;">-&gt;<span>&nbsp;</span></span> 우선순위 :&nbsp;setOrder(1)&nbsp;로&nbsp;조절&nbsp;가능&nbsp;(숫자&nbsp;작을수록&nbsp;먼저&nbsp;실행)</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">Interceptor&nbsp;</h3>
<p style="text-align: center;"><b>컨트롤러&nbsp;접근&nbsp;전/후&nbsp;제어</b></p>
<p style="text-align: center;">로그인&nbsp;여부를&nbsp;검사하여&nbsp;비로그인&nbsp;사용자의&nbsp;접근을&nbsp;차단 <br />컨트롤러&nbsp;진입&nbsp;전(preHandle)에&nbsp;세션을&nbsp;확인 <br />인증&nbsp;실패&nbsp;시&nbsp;-&gt;&nbsp;메인페이지로&nbsp;리다이렉트</p>
<p style="text-align: center;">&nbsp;</p>
<pre class="bash" id="code_1761121176864"><code>@Slf4j
public class LoginCheckInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
            throws Exception {

        HttpSession session = request.getSession(false); // 기존 세션만 가져오기

        if (session == null || session.getAttribute("loginMember") == null) {
            log.warn("미인증 사용자 요청 : {}", request.getRequestURI());
            response.sendRedirect(request.getContextPath()); // 메인페이지로
            return false; // 컨트롤러 접근 차단
        }

        log.info("인증된 사용자 요청 - URL : {}", request.getRequestURI());
        return true; // 컨트롤러로 진행
    }
}</code></pre>
<p>&nbsp;</p>
<p>-&gt; 실행 시점 : DispatcherServlet 이후, Controller 실행 전/후 <br /><span style="color: #333333; text-align: start;">-&gt;<span>&nbsp;</span></span> 주요&nbsp;메서드&nbsp;:&nbsp;preHandle()&nbsp;(가장&nbsp;자주&nbsp;사용) <br /><span style="color: #333333; text-align: start;">-&gt;<span>&nbsp;</span></span> 사용&nbsp;목적 &nbsp;:&nbsp;로그인,&nbsp;권한&nbsp;체크,&nbsp;접근&nbsp;제한&nbsp;등 <br /><span style="color: #333333; text-align: start;">-&gt;<span>&nbsp;</span></span> 등록&nbsp;위치 &nbsp;:&nbsp;WebConfig&nbsp;&rarr;&nbsp;registry.addInterceptor(new&nbsp;LoginCheckInterceptor()) <br /><span style="color: #333333; text-align: start;">-&gt;<span>&nbsp;</span></span> 예외&nbsp;경로&nbsp;:&nbsp;/login.me,&nbsp;/insert.me,&nbsp;/static/&nbsp;등은&nbsp;제외&nbsp;처리</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">Filter VS Interceptor&nbsp;</h3>
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>위치</td>
<td>DispatcherServlet <b>이전</b></td>
<td>DispatcherServlet <b>이후</b>, Controller <b>이전/이후</b></td>
</tr>
<tr>
<td>설정 클래스</td>
<td>FilterConfig</td>
<td>WebConfig</td>
</tr>
<tr>
<td>등록 방식</td>
<td>FilterRegistrationBean 또는 @Component</td>
<td>WebMvcConfigurer의 addInterceptors()</td>
</tr>
<tr>
<td>주요 용도</td>
<td>요청/응답 전체 처리 (인코딩, 로깅, 보안 등)</td>
<td>Controller 진입 전/후 처리 (인증, 권한, 로깅 등)</td>
</tr>
<tr>
<td>예시</td>
<td>요청 시간 측정, XSS 필터, 인코딩 필터</td>
<td>로그인 체크, 세션 검증, 권한 관리</td>
</tr>
</tbody>
</table>
<hr contenteditable="false" />
<p style="text-align: center;">중요한거 배웠다. 필터랑 인터페이스를 잘 활용해야 유연하고 확장 가능한 구조를 만들 수 있다. 내일도 열심히 해야지!!</p>