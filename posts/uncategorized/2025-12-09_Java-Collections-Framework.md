# Java Collections Framework

**카테고리**: uncategorized

**작성일**: Tue, 9 Dec 2025 17:30:48 +0900

**원문 링크**: https://junsseok.tistory.com/56

---

<p style="text-align: center;">Java&nbsp;Collections&nbsp;Framework</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">Java Collections Framework란?</h3>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><b> 여러 데이터를 효율적으로 저장, 검색, 삭제, 정렬하기 위한 </b><br /><b>표준&nbsp;인터페이스&nbsp;+&nbsp;구현&nbsp;클래스들의&nbsp;집합이다.</b></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">-&gt; 배열보다 유연하고, 공통 API로 자료구조를 다룰 수 있게 해준다.</p>
<hr contenteditable="false" />
<h3>전체 구조</h3>
<pre class="bash" id="code_1765267851702"><code>Iterable
 └ Collection
    ├ List
    ├ Set
    └ Queue
Map (Collection 상속 X)</code></pre>
<p>&nbsp;</p>
<p>Collection Framework는 크게 Collection과 Map으로 나눌 수 있다.</p>
<p>Collection&nbsp;인터페이스를&nbsp;상속하는&nbsp;자료구조들은 <br />데이터를&nbsp;단일&nbsp;요소(Object)&nbsp;단위로&nbsp;관리한다는&nbsp;공통점을&nbsp;가진다. <br /><br />Collection&nbsp;계열은&nbsp;다시&nbsp;List,&nbsp;Set,&nbsp;Queue로&nbsp;나뉜다.</p>
<hr contenteditable="false" />
<h2 style="text-align: center;">Collection 계열</h2>
<h3>1. List</h3>
<p>List는&nbsp;저장&nbsp;순서를&nbsp;유지하며,&nbsp;중복&nbsp;데이터를&nbsp;허용하는&nbsp;자료구조이다. <br />인덱스를&nbsp;통해&nbsp;특정&nbsp;위치의&nbsp;데이터를&nbsp;직접&nbsp;접근할&nbsp;수&nbsp;있다. <br /><br />대표 구현체로는&nbsp;<br />(1)&nbsp;ArrayList <br />내부적으로&nbsp;배열을&nbsp;사용하며,&nbsp;조회&nbsp;성능이&nbsp;빠르다. <br />다만&nbsp;중간에&nbsp;데이터를&nbsp;삽입&middot;삭제할&nbsp;경우&nbsp;비용이&nbsp;크다. <br /><br />(2)&nbsp;LinkedList <br />노드&nbsp;기반&nbsp;구조로,&nbsp;삽입&middot;삭제가&nbsp;빈번한&nbsp;경우에&nbsp;유리하다. <br />반면&nbsp;특정&nbsp;요소를&nbsp;조회하는&nbsp;성능은&nbsp;상대적으로&nbsp;느리다. <br /><br />--&gt;&gt;&nbsp;순서가&nbsp;중요하고,&nbsp;조회가&nbsp;많을&nbsp;때&nbsp;주로&nbsp;사용된다.</p>
<hr contenteditable="false" />
<h3>2. Set (순서 X, 중복 X)</h3>
<p><br />Set은&nbsp;중복&nbsp;데이터를&nbsp;허용하지&nbsp;않는&nbsp;자료구조이다. <br />저장&nbsp;순서는&nbsp;보장되지&nbsp;않으며,&nbsp;인덱스를&nbsp;통한&nbsp;접근이&nbsp;불가능하다. <br /><br />대표&nbsp;구현체&nbsp;:&nbsp; <br />(1)&nbsp;HashSet <br />가장&nbsp;많이&nbsp;사용되며,&nbsp;빠른&nbsp;검색&nbsp;성능을&nbsp;제공한다. <br />내부적으로&nbsp;hashCode()와&nbsp;equals()를&nbsp;사용해&nbsp;중복을&nbsp;판단한다. <br /><br />(1)&nbsp;LinkedHashSet <br />입력된&nbsp;순서를&nbsp;유지하는&nbsp;Set <br /><br />TreeSet <br />데이터가&nbsp;자동으로&nbsp;정렬되며,&nbsp;내부적으로&nbsp;Red-Black&nbsp;Tree&nbsp;구조를&nbsp;사용한다. <br /><br />--&gt;&gt;&nbsp;중복&nbsp;제거가&nbsp;목적일&nbsp;때&nbsp;주로&nbsp;사용된다. </p>
<hr contenteditable="false" />
<h3>3.&nbsp;Queue&nbsp;(FIFO&nbsp;구조)</h3>
<p><br />Queue는&nbsp;먼저&nbsp;들어온&nbsp;데이터가&nbsp;먼저&nbsp;나가는(FIFO)&nbsp;구조를&nbsp;가진다. <br />작업&nbsp;대기열,&nbsp;이벤트&nbsp;처리&nbsp;등&nbsp;순차&nbsp;처리가&nbsp;필요한&nbsp;상황에서&nbsp;사용된다. <br /><br />Queue&nbsp;:&nbsp;단방향&nbsp;입&middot;출력 <br /><br />Deque&nbsp;:&nbsp;앞뒤&nbsp;양쪽에서&nbsp;삽입&middot;삭제&nbsp;가능 <br /><br />대표&nbsp;구현체&nbsp;: <br />(1)&nbsp;ArrayDeque <br /><br />(2)&nbsp;PriorityQueue&nbsp;(우선순위&nbsp;기반&nbsp;처리)</p>
<hr contenteditable="false" />
<h2 style="text-align: center;">Map&nbsp;계열</h2>
<p><br />Map은&nbsp;Collection을&nbsp;상속하지&nbsp;않으며, <br />Key&nbsp;-&nbsp;Value&nbsp;쌍&nbsp;형태로&nbsp;데이터를&nbsp;관리하는&nbsp;자료구조이다. <br /><br />Key는&nbsp;중복이&nbsp;허용되지&nbsp;않고, <br />Value는&nbsp;중복이&nbsp;허용된다. <br /><br />대표 구현체 :<br />(1) HashMap <br />가장&nbsp;많이&nbsp;사용되며,&nbsp;빠른&nbsp;검색이&nbsp;가능하다.&nbsp;(순서&nbsp;보장&nbsp;X) <br /><br /><span style="color: #333333; text-align: start;">(2)<span>&nbsp;</span></span> LinkedHashMap <br />입력&nbsp;순서를&nbsp;유지하는&nbsp;Map <br /><br /><span style="color: #333333; text-align: start;">(3)<span>&nbsp;</span></span> TreeMap <br />Key&nbsp;기준으로&nbsp;자동&nbsp;정렬된다.</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">면접한줄요약</h3>
<p style="text-align: center;">Java&nbsp;Collections&nbsp;Framework는&nbsp;다양한&nbsp;자료구조를&nbsp;표준&nbsp;인터페이스로&nbsp;제공해&nbsp;데이터를&nbsp;일관되고&nbsp;효율적으로&nbsp;저장&middot;관리할&nbsp;수&nbsp;있게&nbsp;해주는&nbsp;프레임워크입니다</p>