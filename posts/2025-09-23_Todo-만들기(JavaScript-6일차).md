# Todo 만들기(JavaScript 6일차)

**작성일**: Tue, 23 Sep 2025 17:07:26 +0900

**원문 링크**: https://junsseok.tistory.com/20

---

<p style="text-align: center;">Todo 웹 사이트 실습<br />JavaScript와 LocalStorage를 이용해서 간단한 Todo List</p>
<hr contenteditable="false" />
<p style="text-align: left;">1. 기술</p>
<p style="text-align: left;">- HTML : 앱의 뼈대 (입력창, 버튼, 리스트 구조) <br />- CSS : 디자인, 레이아웃, 애니메이션 <br />- JavaScript : 기능 구현, LocalStorage를 이용한 데이터 저장</p>
<p>&nbsp;</p>
<hr contenteditable="false" />
<p>2. 주요 기능</p>
<p>- 할 일 추가 : 입력 후 버튼 클릭 또는 엔터 키로 새로운 할 일을 등록 <br />- 완료/미완료 토글 : 체크박스를 클릭하면 상태 변경 <br />- 필터링 : 전체 / 진행중 / 완료 항목만 선택적으로 확인 <br />- 로컬스토리지 저장 : 브라우저 새로고침이나 종료 후에도 데이터 유지 <br />- 완료 항목 삭제 : 완료된 항목만 한 번에 삭제</p>
<hr contenteditable="false" />
<p>3. 코드</p>
<p>(1). index.html</p>
<pre class="bash" id="code_1758614548643"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Todo List App&lt;/title&gt;

    &lt;!-- 외부라이브러리 --&gt;
    &lt;!-- google web font --&gt;
    &lt;link rel="preconnect" href="https://fonts.googleapis.com"&gt;
    &lt;link rel="preconnect" href="https://fonts.gstatic.com" crossorigin&gt;
    &lt;link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100..900&amp;display=swap" rel="stylesheet"&gt;

    &lt;!-- 내부import --&gt;
    &lt;link rel="stylesheet" href="./style.css"&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="container"&gt;
        &lt;!-- 헤더영역 --&gt;
         &lt;header&gt;   
            &lt;h1&gt;Todo List&lt;/h1&gt;
         &lt;/header&gt;

         &lt;div class="todo-input"&gt;
            &lt;input id="todo-input" type="text" placeholder="새로운 할일을 입력하세요."&gt;
            &lt;button id="todo-add-btn"&gt;추가&lt;/button&gt;
         &lt;/div&gt;

         &lt;div class="filter-buttons"&gt;
            &lt;button data-filter="all" class="active"&gt;전체&lt;/button&gt;
            &lt;button data-filter="active"&gt;진행중&lt;/button&gt;
            &lt;button data-filter="completed"&gt;완료&lt;/button&gt;
         &lt;/div&gt;

         &lt;ul id="todo-list" class="todo-list"&gt;&lt;/ul&gt;

         &lt;div class="todo-footer"&gt;
            &lt;span id="todo-count"&gt;1개 남음&lt;/span&gt;
            &lt;button class="delete-btn" id="clear-completed-btn"&gt;완료된 항목 삭제&lt;/button&gt;
         &lt;/div&gt;
    &lt;/div&gt;

    &lt;script src="./script.js"&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>&nbsp;</p>
<p>(2). script.js</p>
<pre class="bash" id="code_1758614576122"><code>/*
    localStorage
    - 브라우저에 key-value형태로 데이터를 저장할 수 있는 공간.
    - 저장된 데이터는 브라우저를 껐다 켜도 유지가되며, 도메인별로 저장이 된다.
    - 최대 저장용량은 5MB(브라우저별로 다를 수 있음)

    localStorage.setItem(key, value); - 데이터를 저장
    localStorage.getItem(key); - 데이터를 불러올 때
    localStorage.removeItem(key); - 데이터를 삭제할 때
    localStorage.clear(); - 모든 데이터 삭제
    * 문자열만 저장하고 가져올 수 있다.

    JSON.stringify(js객체) -&gt; JSON 문자열로 변환
    JSON.parse(문자열) -&gt; JS객체로 복원
*/

//====== 전역 변수 ========
//할일 목록을 저장하는 배열 - 여러 함수에서 공유해야 하기 떄문에 전역 선언
let todos = JSON.parse(localStorage.getItem('todos')) || [];
let filterState = 'all';

// ====== DOM 요소 ========
const todoList = document.getElementById('todo-list'); //할일목록 ul
const clearCompletedBtn = document.getElementById('clear-completed-btn'); //완료목록삭제버튼
const todoInput = document.getElementById('todo-input'); //todo입력창
const filterBtns = document.querySelectorAll('.filter-buttons button'); //필터 버튼 목록


// ===== 초기화 함수 ========
//웹이 시작될 때 실행되는 기본함수
//이벤트 등록과 화면 렌더링을 담당
function init() {
    bindEvents();
    render();
}

function bindEvents() {
    const addBtn = document.getElementById('todo-add-btn');
    addBtn.addEventListener('click', addTodo);

    todoInput.addEventListener('keydown', function(e){
        if(e.key === 'Enter'){
            addTodo();
        }
    })

    clearCompletedBtn.addEventListener('click', clearCompletedTodos);

    //필터 버튼들을 가져와서 이벤트를 등록
    filterBtns.forEach(function(btn){
        btn.addEventListener('click', function(ev){
            setFilter(ev.target.dataset.filter);
        })
    })
}

//=========== 데이터 조작 함수 =======================
function clearCompletedTodos(){
    let newTodos = [];

    for(let todo of todos){
        if(!todo.completed) {
            newTodos.push(todo); //완료되지 않은 목록만 추가
        }
    }

    todos = newTodos;
    saveTodos();
    render(); //화면 업데이트
}

//새로운 할일을 추가하는 함수
function addTodo() {
    const text = todoInput.value.trim();
    if (!text) return; //빈문자열이면 함수 종료

    const todo = {
        id: Date.now(), //현재시간을 ms단위로 변환 -&gt; 고유한 ID로 사용
        content: text,
        completed: false,
        createdAt: new Date().toLocaleString(), //생성시간
    }

    todos.push(todo); //새로운 할일을 목록에 추가
    todoInput.value = "";
  
    saveTodos();
    render(); //할일목록을 기준으로 UI에 적용
}

function deleteTodo(id){
    //해당 ID를 목록에서 제거.
    let newTodo = [];
    for(let todo of todos){
        if(todo.id === id)
            continue;

        newTodo.push(todo);
    }

    todos = newTodo;
    saveTodos();
    render(); //할일목록을 기준으로 UI에 적용
}

function toggleTodo(id){
    //해당 ID를 통해서 할일을 찾아 완료상태 -&gt; 미완료, 미완료 -&gt; 완료 변경.
    for(let todo of todos){
        if(todo.id === id) {
            todo.completed = !todo.completed;
            break;
        }
    }

    saveTodos();
    render();
}

//현재 필터에 따라서 할일 목록을 필터링하여 반환하는 함수
function getFilteredTodos(){
    const filteredTodos = [];
    if(filterState === 'active'){
        //미완료목록만 filteredTodos에 담김
        for(let todo of todos){
            if(!todo.completed){
                filteredTodos.push(todo);
            }
        }
    } else if(filterState === 'completed'){
        //완료목록만 filteredTodos에 담김
        for(let todo of todos){
            if(todo.completed){
                filteredTodos.push(todo);
            }
        }
    } else{
        return todos;
    }

    return filteredTodos;
}

//할일목록을 로컬스토리지영역에 저장하는 함수
function saveTodos(){
    localStorage.setItem('todos', JSON.stringify(todos));
}

//=========== 화면 렌더링을 위한 함수 ====================
//메인 렌더링 함수
function render() {
    todoList.innerHTML = ""; //기존 UI 제거

    //현재 필터에 맞는 할일만 목록으로 가져오기
    const filteredTodos = getFilteredTodos();

    if (filteredTodos.length === 0) { //할일목록이 비어있다면
        emptyStateRender();
    } else { //할일 목록이 있는 경우
        filteredTodos.forEach(function (todo) {
            todoItemRender(todo);
        })
    }

    updateCount();
    updateClearButton();
}

function emptyStateRender(){
   const emptyEl = document.createElement('div');
    emptyEl.className = 'empty-state';
    emptyEl.innerHTML = '할 일이 없습니다.'
    todoList.appendChild(emptyEl);
}

function todoItemRender(todo) {
    const todoItem = document.createElement('li');
    todoItem.className = 'todo-item' + (todo.completed ? ' completed' : '');

    todoItem.innerHTML = `&lt;div class="todo-checkbox ${todo.completed ? 'checked' : ''}"&gt;&lt;/div&gt;
                            &lt;span&gt;${todo.content}&lt;/span&gt;
                            &lt;button class="delete-btn"&gt;삭제&lt;/button&gt;`;

    //새로 생성된 요소들 중에서 이벤트가 필요한 부분만 가져오기.
    const checkBox = todoItem.querySelector('.todo-checkbox'); //todoItem내부에 있는 checkbox요소
    checkBox.addEventListener('click', function(){
        toggleTodo(todo.id);
    })

    const deleteBtn = todoItem.querySelector('.delete-btn'); //todoItem내부에 있는 deleteBtn요소
    deleteBtn.addEventListener('click', function(){
        deleteTodo(todo.id);
    })
    todoList.appendChild(todoItem);
}

//남은 할일의 갯수를 구해서 화면을 업데이트.
function updateCount(){
    const todoCount = document.getElementById('todo-count');
    let count = 0;
    for(let todo of todos){
       if(!todo.completed) count++;
    }

    todoCount.innerHTML = `${count}개 남음`;
}

function updateClearButton(){
    let isView = 'none';
    for(let todo of todos){
       if(todo.completed) {
            isView = 'block';
            break;
       }
    }

    //완료된 목록이 있다면 버튼 표시, 없으면 숨김
    clearCompletedBtn.style.display = isView;
}

//======== 필터관련 함수 ==============
//필터를 설정하고 UI를 업데이트
function setFilter(filter){
    filterState = filter; //전역상태에 필터상태를 변경

    //모든 필터버튼의 active클래스를 조회해서 수정
    filterBtns.forEach(function(btn){
        btn.className = (btn.dataset.filter === filter ? "active" : "");
    });

    render();
}


//========= load 이벤트 함수 ==================
// window.onload = function(){
//     init();
// }

//DOMContentLoaded -&gt; HTML이 전부 로드되어 DOM트리가 완성되면 실행
document.addEventListener('DOMContentLoaded', init);</code></pre>
<p>&nbsp;</p>
<p>(3). style.css</p>
<pre class="bash" id="code_1758614642090"><code>*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body{
    min-height: 100vh;
    font-family: "Noto Sans KR", sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
    font-weight: 400;
    background: linear-gradient(135deg, #F7A5A5, #5D688A);
    padding: 20px;
}

button{
    border: none;
    outline: none;
}

.container{
    max-width: 600px;
    margin: 0 auto;
    background: #FFF2EF;
    border-radius: 15px;
    box-shadow: 0 20px 40px rgba(255, 245, 245, 0.336);
}

header {
    background: linear-gradient(135deg, #F7A5A5, #5D688A);
    color: white;
    text-align: center;
    padding: 30px 0;
}

header h1{
    font-size: 40px;
    font-weight: 300;
    letter-spacing: 2px;
}

.todo-input{
    display: flex;
    padding: 20px;
    border-bottom: 1px solid rgb(224, 224, 224);
}

.todo-input input{
    flex: 1;
    padding: 15px;
    border: 2px solid rgb(224, 224, 224);
    border-radius: 8px;
    font-size: 16px;
    outline: none;
    transition: border-color 0.3s ease;
}

.todo-input input:focus{
    border-color: #5D688A;
}

.todo-input button{
    margin-left: 10px;
    padding: 15px 25px;
    background: #5d688a;
    color: white;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
    font-weight: 600;
    transition: transform 0.3s ease;
}

.todo-input button:hover{
    transform: translateY(-2px);
}

.todo-list{
    list-style: none;
    max-height: 400px;
    overflow-y: auto;
}

.todo-item{
    display: flex;
    align-items: center;
    padding: 15px 20px;
    border-bottom: 1px solid rgb(224, 224, 224);
    transition: background 0.2s ease;
}

.todo-item:hover{
    background: #fff6f4;
}

.todo-item.completed{
    opacity: 0.6;
}

.todo-item.completed &gt; span{
    text-decoration: line-through;
    color: #5D688A;
}

.todo-item &gt; span{
    flex: 1;
    font-size: 16px;
    line-height: 24px;
}

.delete-btn{
    background: #e46464;
    color: white;
    border-radius: 6px;
    padding: 8px 12px;
    cursor: pointer;
    font-size: 12px;
    transition: background 0.3s ease;
}

.delete-btn:hover{
    background: #d44d4d;
}

.todo-checkbox{
    width: 20px;
    height: 20px;
    border: 2px solid rgb(224, 224, 224);
    border-radius: 8px;
    margin-right: 15px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #ffffff;
    padding-bottom: 4px;
    transition: all 0.3s ease;
}

.todo-checkbox.checked{
    background: #5d688a;
    border-color: #5d688a;
}

/* .todo-checkbox.checked::after .todo-checkbox.checked요소에 가상의 요소를 추가하겠다.-&gt;  */
.todo-checkbox.checked::after{
    content: '✔';
    color: white;
    font-size: 12px;
    font-weight: bold;
}

.todo-footer{
    display: flex;
    justify-content: space-between;
    padding: 20px;
    background: #FFDBB6;
    color: #5D688A;
}

.todo-footer &gt; span{
    line-height: 33px;
    font-size: 18px;
    font-weight: 600; 
}

.empty-state{
    text-align: center;
    padding: 40px 20px;
    color: #5d688a;
    font-size: 16px;
    font-weight: 600;
}

.filter-buttons{
    display: flex;
    justify-content: center;
    padding: 20px;
    border-bottom: 1px solid rgb(224, 224, 224);
    gap: 10px;
}

.filter-buttons button{
    padding: 8px 16px;
    border: 2px solid rgb(224, 224, 224);
    background: white;
    border-radius: 20px;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.3s ease;
}

.filter-buttons button:hover,
.filter-buttons button.active{
    background: #5D688A;
    color: white;
    border-color: #5d688a;
}</code></pre>
<hr contenteditable="false" />
<p>4. 페이지</p>
<p>(1). 메인 페이지</p>
<p><figure class="imageblock alignCenter"><span><img height="513" src="https://blog.kakaocdn.net/dn/MA4Et/btsQMZoineX/47tbydz9WkQxA3vqxOqQr1/img.png" width="640" /></span></figure>
</p>
<p>&nbsp;</p>
<p>(2). 할일 추가</p>
<p><figure class="imageblock alignCenter"><span><img height="619" src="https://blog.kakaocdn.net/dn/bqkcTp/btsQMajJ7jF/GdhucFd5HMnKtFVZPgYzA1/img.png" width="654" /></span></figure>
</p>
<p>&nbsp;</p>
<p>(3) 체크 시</p>
<p><figure class="imageblock alignCenter"><span><img height="523" src="https://blog.kakaocdn.net/dn/dE09Ed/btsQK2fwZOP/IquW9lWPQ7K5NdqrTsGW7k/img.png" width="633" /></span></figure>
</p>
<p>(4) 진행 중</p>
<p><figure class="imageblock alignCenter"><span><img height="459" src="https://blog.kakaocdn.net/dn/drXDyl/btsQMfkThat/ikTmvMY6bGrYKpyHv7qxoK/img.png" width="629" /></span></figure>
</p>
<p>(5) 완료 시</p>
<p><figure class="imageblock alignCenter"><span><img height="455" src="https://blog.kakaocdn.net/dn/Jg0MG/btsQMSJCVGe/GjfcjRepvWS0RrefItPl10/img.png" width="622" /></span></figure>
</p>
<p>(6) 완료된 항목 삭제</p>
<p><figure class="imageblock alignCenter"><span><img height="505" src="https://blog.kakaocdn.net/dn/bjhJL9/btsQK6a8Up0/5PQ3kNQOmQD29AnruqyOW0/img.png" width="626" /></span></figure>
</p>