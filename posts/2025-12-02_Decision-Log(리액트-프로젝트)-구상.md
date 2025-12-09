# Decision Log(리액트 프로젝트) 구상

**작성일**: Tue, 2 Dec 2025 15:28:07 +0900

**원문 링크**: https://junsseok.tistory.com/49

---

<p style="text-align: center;">Decision Log</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">결과가 아닌, 결정의 이유를 저장하는 서비스</p>
<hr contenteditable="false" />
<h2>1. 문제 정의</h2>
<h3>- 현재 문제</h3>
<ul>
<li>우리는 대부분 <b>결과만 기록</b></li>
<li>하지만 진짜 중요한 건:
<ul>
<li>&nbsp;왜 그 선택을 했는지</li>
<li>&nbsp;어떤 정보와 가정 위에서 결정했는지</li>
</ul>
</li>
<li>결과가 나쁘면 &rarr; &ldquo;내 선택이 틀렸다&rdquo;로 끝남<br /><b>판단 과정은 남지 않음</b></li>
</ul>
<p>좋은 결정 &ne; 좋은 결과</p>
<p>나쁜 결과 &ne; 나쁜 결정</p>
<p><b>결정의 맥락과 논리를 기록해야 성장 가능</b></p>
<hr />
<h2>2. 서비스 한 줄 정의</h2>
<h2><b>'결정의 근거와 사고 과정을 기록하는 의사결정 히스토리 서비스'</b></h2>
<hr />
<h2>3. 타겟 유저</h2>
<h3>(1) 1차 타겟 (MVP)</h3>
<ul>
<li>스타트업 실무자</li>
<li>기획자 / PM</li>
<li>개발자 (기술 선택 기록)</li>
</ul>
<h3>(2)&nbsp; 2차 확장</h3>
<ul>
<li>창업가</li>
<li>학생 (진로&middot;선택 기록)</li>
<li>기업 팀 단위</li>
</ul>
<hr />
<h2>4. 핵심 기능 구조 (MVP)</h2>
<h3>(1) 의사결정 생성 (Create)</h3>
<div>
<div>필드설명
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>결정 제목</td>
<td>&ldquo;React를 선택한 이유&rdquo;</td>
</tr>
<tr>
<td>결정 날짜</td>
<td>자동</td>
</tr>
<tr>
<td>결정 유형</td>
<td>개인 / 팀</td>
</tr>
<tr>
<td>상황 설명</td>
<td>왜 이 선택을 해야 했는지</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
</div>
</div>
<h3>(2) 선택지 기록 (A/B 구조)</h3>
<div>
<div>항목내용
<table border="1" style="border-collapse: collapse; width: 100%;">
<tbody>
<tr>
<td>선택지 A</td>
<td>예: React 사용</td>
</tr>
<tr>
<td>선택지 B</td>
<td>예: Vue 사용</td>
</tr>
<tr>
<td>(옵션) C</td>
<td>추가 가능</td>
</tr>
</tbody>
</table>
</div>
</div>
<p>각 선택지별로:</p>
<ul>
<li>장점</li>
<li>단점</li>
<li>위험 요소</li>
</ul>
<p>-&gt; <b>결과가 아니라 &lsquo;고민 과정&rsquo; 중심</b></p>
<p>&nbsp;</p>
<h3>(3) 결정 이유 (핵심)</h3>
<ul>
<li>최종 선택한 옵션</li>
<li>결정 기준 (비중)
<ul>
<li>속도</li>
<li>비용</li>
<li>확장성</li>
<li>팀 역량</li>
</ul>
</li>
</ul>
<hr />
<h3>4. 결과 회고 (Retrospective)</h3>
<p><b>결정 당시엔 비어 있음</b></p>
<p>나중에:</p>
<ul>
<li>실제 결과는 어땠는가?</li>
<li>판단이 맞았는가?</li>
<li>다음에 바꿀 점은?</li>
</ul>
<p>-&gt;<b> 결과가 안 좋아도 '판단은 합리적이었다'를 증명 가능</b></p>
<hr />
<h2>5. 주요 페이지 구성 (SPA 라우트)</h2>
<div>
<div>
<div>
<pre class="bash" id="code_1764656286787"><code>/                 &rarr; 랜딩 페이지
/login            &rarr; 로그인
/signup           &rarr; 회원가입
/logs             &rarr; 결정 로그 리스트
/logs/new         &rarr; 새 결정 작성
/logs/:id         &rarr; 결정 상세
/logs/:id/edit    &rarr; 결정 수정
/mypage           &rarr; 내 결정 모아보기
/not-found        &rarr; 404</code></pre>
</div>
</div>
</div>
<hr />
<h2>6. 컴포넌트 구조 예시</h2>
<pre class="bash" id="code_1764656443331"><code>src/
├── context/
│   └── DecisionContext.jsx
├── components/
│   ├── Decision/
│   │   └── DecisionForm.jsx
│   └── Layout/
│       ├── Header.jsx
│       ├── Layout.jsx
│       └── Layout.styled.js
├── pages/
│   ├── DecisionListPage.jsx
│   └── DecisionDetailPage.jsx
├── routes/
│   └── routes.jsx
├── App.jsx
├── App.css
├── index.css
└── main.jsx</code></pre>
<p>&nbsp;</p>
<hr />
<h2>8. 사업성 확장 시나리오</h2>
<h3>-&nbsp; B2C</h3>
<ul>
<li>개인 성장 기록</li>
<li>커리어 브랜딩</li>
</ul>
<h3>-&nbsp; B2B</h3>
<ul>
<li>팀 단위 Decision Log</li>
<li>회의 기록 대체</li>
<li>레퍼런스 자산화</li>
</ul>