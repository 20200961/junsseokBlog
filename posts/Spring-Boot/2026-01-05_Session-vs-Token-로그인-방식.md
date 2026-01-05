# Session vs Token 로그인 방식

**카테고리**: Spring Boot

**작성일**: Mon, 5 Jan 2026 17:44:36 +0900

**원문 링크**: https://junsseok.tistory.com/74

---

<p style="text-align: center;">session로그인방식과 token로그인 방식</p>
<hr contenteditable="false" />
<p style="text-align: center;">웹 개발을 하다 보면 반드시 마주치게 되는 인증(Authentication) 방식, Session과 Token입니다.</p>
<p style="text-align: center;">두 방식의 차이점과 각각의 장단점을 실제 동작 방식과 함께 알아보겠습니다.</p>
<hr contenteditable="false" />
<h3 style="text-align: left;">Session 기반 인증</h3>
<p><b>동작 원리</b></p>
<p>서버가 사용자 정보를 직접 저장하고 관리하는 방식입니다.</p>
<p>로그인하면 서버가 세션을 만들어 저장하고, 클라이언트에게는 세션 ID만 쿠키로 전달합니다.</p>
<p>&nbsp;</p>
<p><b>동작 흐름</b></p>
<p>1. 로그인시</p>
<p>- 사용자가 ID/PW 전송</p>
<p>- 서버가 검증 후 세션 생성 -&gt; 서버 메모리/DB에 저장</p>
<p>- 세션 ID를 쿠키로 클라이언트에 전달</p>
<p>&nbsp;</p>
<p>2. 이후 요청 시</p>
<p>- 클라이언트가 쿠키의 세션ID를 자동으로 전송</p>
<p>- 서버가 세션 ID로 저장소에서 사용자 정보 조회</p>
<p>- 인증 완료 후 응답</p>
<p>&nbsp;</p>
<p><b>예시</b></p>
<pre class="bash" id="code_1767602043289"><code>// 로그인
app.post('/login', (req, res) =&gt; {
  const user = validateUser(req.body);
  req.session.userId = user.id; // 세션에 저장
  res.json({ message: '로그인 성공' });
});

// 인증 필요한 API
app.get('/mypage', (req, res) =&gt; {
  if (!req.session.userId) {
    return res.status(401).json({ error: '로그인 필요' });
  }
  res.json({ userId: req.session.userId });
});</code></pre>
<p>&nbsp;</p>
<p><b>특징</b></p>
<p>-&nbsp;Stateful&nbsp;:&nbsp;서버가&nbsp;세션&nbsp;정보를&nbsp;보관 <br />-&nbsp;저장소&nbsp;필요&nbsp;:&nbsp;Redis,&nbsp;메모리,&nbsp;DB&nbsp;등 <br />-&nbsp;쿠키&nbsp;사용&nbsp;:&nbsp;브라우저가&nbsp;자동으로&nbsp;쿠키&nbsp;전송</p>
<p>&nbsp;</p>
<p><b>장점</b></p>
<p>-&nbsp;즉시&nbsp;무효화&nbsp;가능&nbsp;:&nbsp;서버에서&nbsp;세션&nbsp;삭제하면&nbsp;즉시&nbsp;로그아웃 <br />-&nbsp;보안성&nbsp;우수&nbsp;:&nbsp;민감한&nbsp;정보는&nbsp;서버에만&nbsp;존재 <br />-&nbsp;세밀한&nbsp;제어&nbsp;:&nbsp;특정&nbsp;세션만&nbsp;무효화,&nbsp;동시&nbsp;로그인&nbsp;제한&nbsp;등</p>
<p>&nbsp;</p>
<p><b>단점</b></p>
<p>-&nbsp;서버&nbsp;리소스&nbsp;사용&nbsp;:&nbsp;사용자&nbsp;수만큼&nbsp;세션&nbsp;저장&nbsp;필요 <br />-&nbsp;확장성&nbsp;문제&nbsp;:&nbsp;여러&nbsp;서버&nbsp;운영&nbsp;시&nbsp;세션&nbsp;공유&nbsp;복잡 <br />-&nbsp;CORS&nbsp;제약&nbsp;:&nbsp;다른&nbsp;도메인에서&nbsp;쿠키&nbsp;전송&nbsp;제한</p>
<hr contenteditable="false" />
<h3 style="text-align: left;">Token 기반 인증(JWT)</h3>
<p>서버가&nbsp;암호화된&nbsp;토큰을&nbsp;발급하고,&nbsp;이후에는&nbsp;토큰의&nbsp;유효성만&nbsp;검증하는&nbsp;방식입니다.&nbsp; <br />서버는&nbsp;토큰을&nbsp;저장하지&nbsp;않으며,&nbsp;토큰&nbsp;자체에&nbsp;사용자&nbsp;정보가&nbsp;포함되어&nbsp;있습니다.</p>
<p><b>JWT 구조</b></p>
<p>JWT는 세 부분으로 구성됩니다</p>
<p>-&nbsp;Header&nbsp;:&nbsp;토큰&nbsp;타입,&nbsp;암호화&nbsp;알고리즘 <br />-&nbsp;Payload&nbsp;:&nbsp;사용자&nbsp;정보,&nbsp;만료&nbsp;시간&nbsp;등 <br />-&nbsp;Signature&nbsp;:&nbsp;위변조&nbsp;방지&nbsp;서명</p>
<p>&nbsp;</p>
<p><b>동작 흐름</b></p>
<p>1. 로그인시</p>
<p>-&nbsp;사용자가&nbsp;ID/PW&nbsp;전송 <br />-&nbsp;서버가&nbsp;검증&nbsp;후&nbsp;JWT&nbsp;생성&nbsp;(사용자&nbsp;정보&nbsp;포함) <br />-&nbsp;JWT를&nbsp;클라이언트에&nbsp;전달&nbsp;(서버는&nbsp;저장&nbsp;X)</p>
<p>&nbsp;</p>
<p>2. 이후 요청 시</p>
<p>-&nbsp;클라이언트가&nbsp;요청&nbsp;헤더에&nbsp;JWT&nbsp;포함 <br />-&nbsp;서버가&nbsp;JWT&nbsp;서명&nbsp;검증&nbsp;및&nbsp;만료&nbsp;확인 <br />-&nbsp;유효하면&nbsp;토큰&nbsp;내&nbsp;정보로&nbsp;사용자&nbsp;식별</p>
<p>&nbsp;</p>
<p><b>예시</b></p>
<pre class="bash" id="code_1767602295226"><code>const jwt = require('jsonwebtoken');
const SECRET = 'my-secret-key';

// 로그인
app.post('/login', (req, res) =&gt; {
  const user = validateUser(req.body);
  const token = jwt.sign(
    { userId: user.id },
    SECRET,
    { expiresIn: '1h' }
  );
  res.json({ token });
});

// 인증 필요한 API
app.get('/mypage', (req, res) =&gt; {
  const token = req.headers.authorization?.split(' ')[1];
  try {
    const decoded = jwt.verify(token, SECRET);
    res.json({ userId: decoded.userId });
  } catch (error) {
    res.status(401).json({ error: '유효하지 않은 토큰' });
  }
});</code></pre>
<p>&nbsp;</p>
<p><b>특징</b></p>
<p>-&nbsp;Stateless&nbsp;:&nbsp;서버가&nbsp;토큰&nbsp;저장&nbsp;안&nbsp;함 <br />-&nbsp;자가&nbsp;포함&nbsp;:&nbsp;토큰&nbsp;자체에&nbsp;필요한&nbsp;정보&nbsp;포함 <br />-&nbsp;헤더&nbsp;전송&nbsp;:&nbsp;Authorization&nbsp;헤더&nbsp;사용</p>
<p>&nbsp;</p>
<p><b>장점</b></p>
<p>-&nbsp;확장성&nbsp;우수&nbsp;:&nbsp;여러&nbsp;서버에서&nbsp;동일하게&nbsp;검증&nbsp;가능 <br />-&nbsp;서버&nbsp;부담&nbsp;적음&nbsp;:&nbsp;별도&nbsp;저장소&nbsp;불필요 <br />-&nbsp;모바일&nbsp;친화적&nbsp;:&nbsp;쿠키&nbsp;없이도&nbsp;동작 <br />-&nbsp;MSA&nbsp;적합&nbsp;:&nbsp;마이크로서비스&nbsp;간&nbsp;인증&nbsp;공유&nbsp;용이</p>
<p>&nbsp;</p>
<p><b>단점</b></p>
<p>-&nbsp;즉시&nbsp;무효화&nbsp;어려움&nbsp;:&nbsp;토큰&nbsp;만료&nbsp;전까지&nbsp;유효 <br />-&nbsp;토큰&nbsp;크기&nbsp;:&nbsp;세션&nbsp;ID보다&nbsp;크고&nbsp;매&nbsp;요청마다&nbsp;전송 <br />-&nbsp;XSS&nbsp;취약&nbsp;:&nbsp;localStorage&nbsp;저장&nbsp;시&nbsp;스크립트로&nbsp;탈취&nbsp;가능</p>
<hr contenteditable="false" />
<h3>Session vs Token(JWT)</h3>
<p><figure class="imageblock alignLeft"><span><img height="403" src="https://blog.kakaocdn.net/dn/bHefxi/dJMcahJRSX0/xAzUHA9FXrJx6x2gQsjd4K/img.png" width="650" /></span></figure>
</p>
<hr contenteditable="false" />
<h3>선택 가이드</h3>
<p><b>Session 추천 상황</b><br />- 전통적인 서버 렌더링(SSR) 웹사이트 <br />- 보안이 최우선인 서비스 (금융, 관리자) <br />- 실시간 세션 제어가 필요한 경우 <br />- 단일 서버 환경 <br /><br /><b>Token 추천 상황</b><br />- React, Vue 등 SPA 개발 <br />- 모바일 앱 (iOS, Android) <br />- 마이크로서비스 아키텍처 <br />- 여러 도메인에서 인증 공유 <br />- RESTful API 서버</p>
<hr contenteditable="false" />
<h3>마무리</h3>
<p>Session과&nbsp;Token&nbsp;중&nbsp;무엇이&nbsp;더&nbsp;좋다고&nbsp;단정지을&nbsp;수&nbsp;없습니다.&nbsp; <br />최근&nbsp;트렌드는&nbsp;JWT&nbsp;+&nbsp;Refresh&nbsp;Token&nbsp;(HttpOnly&nbsp;Cookie)&nbsp;방식이&nbsp;가장&nbsp;균형잡힌&nbsp;선택으로&nbsp;평가받고&nbsp;있으므로&nbsp;</p>
<p>각각의 장단점을 이해하고, 프로젝트의 요구사항에 맞춰 선택하는 것이 중요합니다!</p>