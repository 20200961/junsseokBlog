# Spring Boot를 사용한 JSP 홈페이지 - 1

**카테고리**: 수강 일지

**작성일**: Tue, 21 Oct 2025 17:19:01 +0900

**원문 링크**: https://junsseok.tistory.com/34

---

<p style="text-align: center;">Spring Boot를 활용하여 이전에 만들었던 JSP 홈페이지 재구현(회원가입, 로그인까지 구현)</p>
<hr contenteditable="false" />
<p style="text-align: center;">MVC</p>
<p style="text-align: center;">MVC는&nbsp;애플리케이션을&nbsp;세&nbsp;가지&nbsp;역할로&nbsp;분리하여&nbsp;구성하는&nbsp;소프트웨어&nbsp;설계&nbsp;패턴으로&nbsp;사용자의&nbsp;요청을&nbsp;받아&nbsp;-&gt;&nbsp;로직&nbsp;처리하고</p>
<p style="text-align: center;">&nbsp;-&gt; 결과 화면을 보여주는 역할을 나눈다 기본적으로 Controller, Model, View 형식</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">스프링 MVC 패턴 구조</p>
<table border="1" id="278435fc-bd9d-81fe-b1f7-e5ac2d0e8325" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr id="278435fc-bd9d-8186-9c78-f02fbfd98c87">
<td id="sO&lt;="><b>Controller</b></td>
<td id="@zzy">@Controller, @RestController</td>
<td id="^OvL">사용자 요청 처리</td>
</tr>
<tr id="278435fc-bd9d-8165-be88-d6b536298102">
<td id="sO&lt;="><b>Model</b></td>
<td id="@zzy">@Service, @Repository, @Entity</td>
<td id="^OvL">로직 및 데이터 계층</td>
</tr>
<tr id="278435fc-bd9d-8132-b868-f75968e7dfe1">
<td id="sO&lt;="><b>View</b></td>
<td id="@zzy">Thymeleaf, JSP, JSON</td>
<td id="^OvL">사용자에게 보여질 화면</td>
</tr>
</tbody>
</table>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">스프링 MVC 구동 방식</p>
<p><figure class="imageblock alignCenter"><span><img height="526" src="https://blog.kakaocdn.net/dn/zTtam/dJMb8WZKPOa/EvUlmW7sYLBf5lZgM1NbHk/img.png" width="792" /></span></figure>
</p>
<table border="1" id="278435fc-bd9d-812f-b0ce-cb5ec38ddf08" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr id="278435fc-bd9d-81ec-8de7-d9032570057f">
<td id="n{k]">  파란색</td>
<td id="pY&#96;^">Spring 프레임워크가 제공하는 컴포넌트</td>
</tr>
<tr id="278435fc-bd9d-8128-b47b-c66ec3aa7921">
<td id="n{k]">  보라색</td>
<td id="pY&#96;^">개발자가 구현해야 하는 컴포넌트 (Controller 등)</td>
</tr>
<tr id="278435fc-bd9d-8175-a29b-f6887a3be45d">
<td id="n{k]">  초록색</td>
<td id="pY&#96;^">View (템플릿 파일 포함) &ndash; 일부는 Spring 제공, 일부는 개발자 구현</td>
</tr>
</tbody>
</table>
<hr contenteditable="false" />
<h3 style="text-align: center;">스프링 부트 프로젝트</h3>
<p style="text-align: center;">이번 스프링 부트 프로젝트 DB연결은 이전과 같이 Mybatis를 활용하여 한다.</p>
<p style="text-align: center;">webapp/WEB-INF/views폴더 안에 있는 JSP 페이지들은 이전 <a href="https://junsseok.tistory.com/26" rel="noopener&nbsp;noreferrer" target="_blank">https://junsseok.tistory.com/26</a> 과 같다</p>
<p style="text-align: center;">이전 servlet으로 사용했을때는 controller dao service 모두 다 반복하여 작성하였지만 spring boot를 사용하면 코드도</p>
<p style="text-align: center;">간략해지고 훨씬 더 편리하게 개발할 수 있다</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">스프링 부트 중요한 부분</h3>
<p style="text-align: center;">&nbsp;</p>
<h4 style="text-align: center;">Controller 부분</h4>
<p style="text-align: left;"><b>1. @Controller</b></p>
<p style="text-align: left;">Bean에&nbsp;class등록하는&nbsp;방법으로&nbsp;@Component를&nbsp;클래스에&nbsp;부여한다. <br />@Controller -&gt; @Component + Controller객체가 가질 수 있는 예외처리등의 기능을 포함하는 어노테이션이다.</p>
<pre class="bash" id="code_1761034514108"><code>@Controller
public class MemberController {
}</code></pre>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><b>2. DI(의존성&nbsp;주입)</b></p>
<p style="text-align: left;">기존 객체 직접 생성방식 -&gt; 결합도가 높음 <br />DI(Dependancy Injection) 사용 -&gt; 스프링이 관리하는 객체를 주입받음</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><b>3. @Autowired 관련</b></p>
<p style="text-align: left;">스프링컨테이너가&nbsp;관리하는&nbsp;객체(Bean에&nbsp;등록)를&nbsp;주입받아&nbsp;사용할&nbsp;수&nbsp;있게&nbsp;해줌. <br />필드&nbsp;주입방식&nbsp;/&nbsp;생성자&nbsp;주입방식</p>
<pre class="bash" id="code_1761034497483"><code>@Autowired
    public MemberController(MemberService memberService,  BCryptPasswordEncoder bCryptPasswordEncoder) {
        this.memberService = memberService;
        this.bCryptPasswordEncoder = bCryptPasswordEncoder;
    }</code></pre>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><b>4. 필드&nbsp;주입방식&nbsp;/&nbsp;생성자&nbsp;주입방식&nbsp;설명</b></p>
<p style="text-align: left;">필드주입방식&nbsp;-&nbsp;코드가&nbsp;간결하지만&nbsp;테스트&nbsp;어려움,&nbsp;불변성&nbsp;보장&nbsp;안됨 <br />생성자&nbsp;주입방식&nbsp;-&nbsp;가장&nbsp;권장,&nbsp;불변성&nbsp;보장,&nbsp;테스트&nbsp;용이</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><b>5. 클라이언트&nbsp;요청&nbsp;데이터&nbsp;받는&nbsp;방법</b></p>
<p>(1)&nbsp;HttpServletRequest&nbsp;활용 <br />request.getParameter()로&nbsp;값을&nbsp;꺼냄. <br />메서드&nbsp;매개변수에&nbsp;HttpServletRequest를&nbsp;작성하면&nbsp;스프링이&nbsp;자동&nbsp;주입해줌. <br />-&gt;&nbsp;전통적인&nbsp;JSP&nbsp;방식과&nbsp;동일.&nbsp;직접&nbsp;request에서&nbsp;꺼내오는&nbsp;방법.</p>
<pre class="bash" id="code_1761034550987"><code>@PostMapping("login.me")
    public String login(HttpServletRequest request, HttpServletResponse response){
        String id = request.getParameter("userId");
        String pw = request.getParameter("userPwd");
        System.out.println(id);
        System.out.println(pw);

        return null;
}</code></pre>
<p><br /><br />(2)&nbsp;@RequestParam&nbsp;사용 <br />요청&nbsp;parameter의&nbsp;key와&nbsp;변수명이&nbsp;같으면&nbsp;생략&nbsp;가능. <br />@RequestParam("userId")&nbsp;String&nbsp;id&nbsp;처럼&nbsp;사용하면 <br />-&gt;&nbsp;HTML&nbsp;form의&nbsp;name&nbsp;속성과&nbsp;자동으로&nbsp;매핑된다.</p>
<pre class="bash" id="code_1761034565211"><code>@PostMapping("login.me")
    public String login(@RequestParam(value = "userId", defaultValue = "user01") String id, String userPwd){
        System.out.println(id);
        System.out.println(userPwd);

        return null;
}</code></pre>
<p><br /><br />(3)&nbsp;@ModelAttribute&nbsp;사용&nbsp;(생략&nbsp;가능) <br />전달값의&nbsp;key와&nbsp;객체&nbsp;필드명이&nbsp;같으면&nbsp;자동&nbsp;매핑됨. <br />-&gt;&nbsp;Member&nbsp;같은&nbsp;VO&nbsp;객체에&nbsp;form&nbsp;데이터가&nbsp;자동으로&nbsp;담긴다.</p>
<pre class="bash" id="code_1761034574211"><code>@PostMapping("login.me")
    public String login(@ModelAttribute Member member){
        System.out.println(member);
        return null;
}</code></pre>
<p>&nbsp;</p>
<p><b>6. 응답 데이터 전달 방법</b></p>
<p>(1)&nbsp;Model&nbsp;객체&nbsp;이용 <br />addAttribute()로&nbsp;데이터를&nbsp;저장하면&nbsp;requestScope에&nbsp;담김. <br />-&gt;&nbsp;JSP에서&nbsp;${}&nbsp;로&nbsp;바로&nbsp;꺼내쓸&nbsp;수&nbsp;있다. </p>
<pre class="bash" id="code_1761034594484"><code>@PostMapping("login.me")
    public String login(@ModelAttribute Member member, Model model) {
        System.out.println(member);

        model.addAttribute("memberId", member.getMemberId());
        model.addAttribute("memberPwd", member.getMemberPwd());

        return "index";
}</code></pre>
<p><br />(2)&nbsp;HttpSession&nbsp;이용 <br />세션에&nbsp;데이터를&nbsp;저장하고&nbsp;redirect로&nbsp;페이지&nbsp;이동&nbsp;가능. <br />-&gt;&nbsp;로그인&nbsp;상태&nbsp;유지&nbsp;등에&nbsp;활용됨.</p>
<pre class="bash" id="code_1761034610787"><code>@PostMapping("login.me")
    public String login(@ModelAttribute Member member, HttpSession session) {
        System.out.println(member);

        session.setAttribute("memberId", member.getMemberId());
        session.setAttribute("memberPwd", member.getMemberPwd());

        return "redirect:/";
}</code></pre>
<p><br /><br />(3)&nbsp;ModelAndView&nbsp;이용 <br />데이터와&nbsp;이동할&nbsp;페이지(View)를&nbsp;함께&nbsp;설정할&nbsp;수&nbsp;있음. <br />-&gt;&nbsp;mv.addObject()로&nbsp;데이터,&nbsp;mv.setViewName()으로&nbsp;뷰&nbsp;설정.</p>
<pre class="bash" id="code_1761034622996"><code>@PostMapping("login.me")
    public ModelAndView login(@ModelAttribute Member member, ModelAndView mv) {
        System.out.println(member);

        mv.addObject("memberId", member.getMemberId());
        mv.addObject("memberPwd", member.getMemberPwd());

        //mv.setViewName("index"); // 포워딩
        mv.setViewName("redirect:/"); //url재요청

        return mv;
}</code></pre>
<p>&nbsp;</p>
<p><b>7. 비밀번호 암호화 관련&nbsp;</b></p>
<p>평문으로&nbsp;저장하면&nbsp;보안&nbsp;위험&nbsp;&rarr;&nbsp;BCryptPasswordEncoder&nbsp;사용 <br />encode()로 암호화하고, matches()로 검증<br />-&gt;&nbsp;사용자가&nbsp;입력한&nbsp;비밀번호를&nbsp;암호화하여&nbsp;DB에&nbsp;저장하고,&nbsp;로그인&nbsp;시&nbsp;입력한&nbsp;평문&nbsp;비밀번호와&nbsp;암호문을&nbsp;matches()로&nbsp;비교한다.</p>
<pre class="bash" id="code_1761034657267"><code>@PostMapping("login.me")
    public ModelAndView login(String memberId, String memberPwd, HttpSession httpSession, ModelAndView mv) {
        Member loginMember = memberService.getMemberById(memberId);
        System.out.println(loginMember);

        //memberPwd -&gt; 암호화 되지 않은 pwd(평문)
        //loginMember.getMemberPwd() -&gt; 암호화 된 pwd
        //bCryptPasswordEncoder.matches(평문, 암호문) -&gt; 해당 비밀번호가 암호화된 비밀번호와 일치하면 true/ 아니면 false반환

        if(loginMember == null) { //ID가 잘못된 상태
            mv.addObject("errorMsg", "아이디를 찾을 수 없습니다.");
            mv.setViewName("common/error");
            //} else if(!loginMember.getMemberPwd().equals(memberPwd)){ //비밀번호 오류
        } else if(!bCryptPasswordEncoder.matches(memberPwd, loginMember.getMemberPwd())){
            mv.addObject("errorMsg", "비밀번호를 확인해 주세요.");
            mv.setViewName("common/error");
        } else {//로그인 성공
            httpSession.setAttribute("loginMember", loginMember);
            mv.setViewName("redirect:/");
        }

        return mv;
    }</code></pre>
<hr contenteditable="false" />
<h4 style="text-align: center;">Config 부분</h4>
<p>&nbsp;</p>
<pre class="bash" id="code_1761033763435"><code>@Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.csrf(AbstractHttpConfigurer::disable)
                .httpBasic(AbstractHttpConfigurer::disable)
                .formLogin(AbstractHttpConfigurer::disable);
        return http.build();
}</code></pre>
<p style="text-align: left;">-&gt; 스프링 시큐리티 사용시 보안모드가 전부 활성화되기 때문에 기본 로그인, 보안설정을 모두 비활성화하고 내가 직접 하겠다는 설정</p>
<p>&nbsp;</p>
<pre class="bash" id="code_1761033775387"><code>@Bean
    public BCryptPasswordEncoder bCryptPasswordEncoder() {
        return new BCryptPasswordEncoder();
}</code></pre>
<p>-&gt;&nbsp;메서드&nbsp;단위로&nbsp;특정&nbsp;객체를&nbsp;만들어&nbsp;반환하는&nbsp;형태의&nbsp;빈&nbsp;등록&nbsp;어노테이션이다. <br />-&gt;&nbsp;BCryptPasswordEncoder객체를&nbsp;스프링&nbsp;빈에&nbsp;등록해서&nbsp;사용하고&nbsp;싶다. <br />-&gt;&nbsp;다만&nbsp;외부객체이므로&nbsp;class에&nbsp;직접&nbsp;@Component를&nbsp;기술할&nbsp;수&nbsp;없어서&nbsp;해당&nbsp;객체를&nbsp;만들어&nbsp;반환하는&nbsp;함수자체를&nbsp;Bean에&nbsp;등록하여&nbsp;필요시&nbsp;스프링이&nbsp;만들어&nbsp;전달할&nbsp;수&nbsp;있게&nbsp;함.</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<h4 style="text-align: center;">Service 부분</h4>
<p>&nbsp;</p>
<p>- MyBatis를 spring없이 단독으로 사용할 때에는 수동으로 커밋또는 롤백을 해줘야한다. spring과 함께 사용할 때에는 트랜잭션처리를 스프링이 자동으로 관리한다.</p>
<hr contenteditable="false" />
<p style="text-align: center;">지금 껏 긴 코드를 작성해오다가 갑자기 짧아지니까 너무 편리하고 행복하다. 구조는 이전에 했던 servlet과 비슷하여 이해하는데 크게 어렵지 않으며 앞으로 배울 내용이 기대된다. 앞으로는 어려워지겠지.............</p>