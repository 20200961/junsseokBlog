# Decision Log(리액트 프로젝트)

**카테고리**: React

**작성일**: Thu, 4 Dec 2025 17:30:27 +0900

**원문 링크**: https://junsseok.tistory.com/51

---

<p style="text-align: center;">Decision Log - 의사결정 기록 플랫폼 개발 회고</p>
<hr contenteditable="false" />
<h2>&nbsp;</h2>
<h2>왜 이 프로젝트를 시작했을까?</h2>
<p>개발을 하다 보면 수많은 의사결정의 순간이 찾아옵니다.</p>
<ul>
<li>"React로 갈까, Vue로 갈까?"</li>
<li>"이 기능을 지금 구현할까, 나중에 할까?"</li>
<li>"TypeScript를 도입할까?"</li>
</ul>
<p>그런데 시간이 지나면 "그때 왜 그런 선택을 했더라?"라는 생각이 들 때가 많았습니다. 또한 팀 프로젝트를 하면서 과거의 결정 과정을 되돌아보고 싶을 때가 있었는데, 그런 기록이 체계적으로 남아있지 않아 아쉬웠습니다.</p>
<p>&nbsp;</p>
<p>의사결정 과정을 기록하고, 나중에 회고할 수 있는 도구가 있으면 좋겠다는 생각에서 이 프로젝트가 시작되었습니다.</p>
<hr contenteditable="false" />
<h2>주요 기능</h2>
<h3>1. 의사결정 기록하기</h3>
<p>사용자는 결정을 내릴 때 다음과 같은 정보를 기록할 수 있습니다:</p>
<ul>
<li><b>결정 제목</b>: 무엇에 대한 결정인지</li>
<li><b>결정 유형</b>: 개인 결정인지 팀 결정인지</li>
<li><b>상황 설명</b>: 왜 이 결정을 내려야 했는지</li>
<li><b>선택지</b>: 고려했던 여러 옵션들과 각각의 장단점, 위험 요소</li>
<li><b>최종 선택</b>: 결국 어떤 선택을 했는지</li>
<li><b>결정 기준</b>: 속도, 비용, 확장성, 팀 역량 등 어떤 기준을 중요하게 봤는지</li>
</ul>
<p>&nbsp;</p>
<h3>2. 결과 회고</h3>
<p>시간이 지난 후, 해당 결정이 실제로 어떤 결과를 가져왔는지 회고할 수 있습니다:</p>
<ul>
<li>실제 결과는 어땠는지</li>
<li>그 판단이 맞았는지</li>
<li>다음에는 무엇을 개선할 것인지</li>
</ul>
<p>&nbsp;</p>
<h3>3. 통계 및 분석</h3>
<p>마이페이지에서 자신의 의사결정 패턴을 분석할 수 있습니다:</p>
<ul>
<li>전체 결정 수, 개인/팀 결정 비율</li>
<li>회고 완료율</li>
<li>주로 어떤 결정 기준을 중요하게 생각하는지 (평균 점수)</li>
<li>결정 유형 분포 차트</li>
</ul>
<p>&nbsp;</p>
<p><figure class="imagegridblock">
  <div class="image-container"><span height="400" style="width: 58.8949%; margin-right: 10px;" width="409"><img height="912" src="https://blog.kakaocdn.net/dn/lfvCf/dJMcacBBe7f/iSpCrBe4TUiY14MkuMqoQ1/img.png" width="932" /></span><span style="width: 39.9423%;"><img height="909" src="https://blog.kakaocdn.net/dn/b5pRVY/dJMcah3X5jp/vjctXBOkyjKA2IEpohpxI1/img.png" width="630" /></span></div>
</figure>
</p>
<p>&nbsp;</p>
<p>- 회고 목록이랑 상세페이지</p>
<p>&nbsp;</p>
<p><figure class="imagegridblock">
  <div class="image-container"><span height="282" style="width: 31.1772%; margin-right: 10px;" width="270"><img height="668" src="https://blog.kakaocdn.net/dn/dW2ymE/dJMcagxdOMa/GyKbku1Uk3hG8vy6kDxyIk/img.png" width="640" /></span><span height="106" style="width: 44.1071%; margin-right: 10px;" width="144"><img height="166" src="https://blog.kakaocdn.net/dn/dTVabx/dJMcadtGP1R/pwKjxoKlF432oLvNeSW1CK/img.png" width="225" /></span><span height="734" style="width: 22.3901%;" width="505"><img height="904" src="https://blog.kakaocdn.net/dn/dLjLx0/dJMcagRwqf0/iGv7NMKkVuHIOimq5IkEUK/img.png" width="622" /></span></div>
</figure>
</p>
<p>&nbsp;</p>
<p>- 마이페이지랑 프로필 수정, 회고작성 부분</p>
<p>&nbsp;</p>
<p><figure class="imagegridblock">
  <div class="image-container"><span height="233" style="width: 30.0813%; margin-right: 10px;" width="219"><img height="264" src="https://blog.kakaocdn.net/dn/bbSGWd/dJMcacVTmFJ/vdnmKNpPQfW92LDUiwBCb1/img.png" width="248" /></span><span height="267" style="width: 22.3239%; margin-right: 10px;" width="186"><img height="350" src="https://blog.kakaocdn.net/dn/cboezT/dJMcacVTmFP/SnI0SKORSZugxvuwB7YQEk/img.png" width="244" /></span><span height="276" style="width: 45.2692%;" width="390"><img height="672" src="https://blog.kakaocdn.net/dn/mlkpq/dJMcaihvS0s/A3qyUnHkTh2Bkk1VVFqRpk/img.png" width="950" /></span></div>
</figure>
</p>
<p>&nbsp;</p>
<p>- 로그인/회원가입 부분 및 에러페이지</p>
<p>&nbsp;</p>
<p><figure class="imagegridblock">
  <div class="image-container"><span height="390" style="width: 49.6242%; margin-right: 10px;" width="298"><img height="809" src="https://blog.kakaocdn.net/dn/bkyJGB/dJMcab3KWsl/zuErkNjYkPz9fXpOcegcX1/img.png" width="618" /></span><span height="524" style="width: 49.213%;" width="397"><img height="825" src="https://blog.kakaocdn.net/dn/u1iZX/dJMcaaqe3En/mHOc2Iz0TbcdsCK5Xpnkxk/img.png" width="625" /></span></div>
</figure>
</p>
<p><span style="color: #000000; text-align: center;"> - 작성자만 글 수정/삭제/회고 수행 가능</span></p>
<hr contenteditable="false" />
<p>&nbsp;</p>
<h3>&nbsp;</h3>
<h3>배운 점</h3>
<p><br />1.&nbsp;useState로&nbsp;상태&nbsp;관리하기 <br />처음엔 여러 개의 state를 각각 만들어야 할지 고민이 많았는데, 관련된 데이터는 객체로 묶어서 하나의 state로 관리하는 게 훨씬 깔끔하다는 걸 배웠습니다.</p>
<p>&nbsp;</p>
<p>2. useEffect로 localStorage 연동</p>
<p>컴포넌트가 마운트될 때 localStorage에서 데이터를 불러오고, state가 변경될 때마다 저장하는 로직을 useEffect로 구현했습니다.&nbsp;</p>
<p>&nbsp;</p>
<p>3. React Router로 페이지 구성하기</p>
<p>BrowserRouter, Routes, Route를 사용해서 여러 페이지를 만드는 게 생각보다 어렵지 않았습니다. 특히 useParams로 URL에서 ID를 가져와서 상세 페이지를 만드는 부분이 신기했습니다. /decisions/:id 이런 식으로 동적 라우팅을 구현할 수 있다는 게 React의 큰 장점인 것 같습니다.</p>
<hr contenteditable="false" />
<h3>아쉬운 점</h3>
<p><br />1. 백엔드가 없음 : localStorage 사용으로 데이터가 브라우저에만 저장됨</p>
<p><br />2. 보안 취약 : 비밀번호가 평문으로 저장됨</p>
<hr contenteditable="false" />
<h3>후기</h3>
<p>Decision&nbsp;Log&nbsp;프로젝트를&nbsp;통해&nbsp;React의&nbsp;핵심&nbsp;개념들을&nbsp;깊이&nbsp;있게&nbsp;이해할&nbsp;수&nbsp;있었습니다.&nbsp;특히&nbsp;상태&nbsp;관리,&nbsp;라우팅,&nbsp;컴포넌트&nbsp;설계&nbsp;등&nbsp;실무에서&nbsp;중요한&nbsp;부분들을&nbsp;직접&nbsp;경험해볼&nbsp;수&nbsp;있어서&nbsp;좋았습니다.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>