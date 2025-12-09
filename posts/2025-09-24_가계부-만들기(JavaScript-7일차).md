# 가계부 만들기(JavaScript 7일차)

**작성일**: Wed, 24 Sep 2025 16:27:15 +0900

**원문 링크**: https://junsseok.tistory.com/21

---

<p style="text-align: center;">가계부 만들기</p>
<p style="text-align: center;">JavaScript와 LocalStorage를 이용해서 간단한 가계부</p>
<hr contenteditable="false" />
<p style="text-align: left;">1. 기술<br />-&nbsp;HTML&nbsp;:&nbsp;앱의&nbsp;뼈대&nbsp;(입력창,&nbsp;버튼,&nbsp;리스트&nbsp;구조) <br />-&nbsp;CSS&nbsp;:&nbsp;디자인,&nbsp;레이아웃,&nbsp;애니메이션 <br />-&nbsp;JavaScript&nbsp;:&nbsp;기능&nbsp;구현,&nbsp;LocalStorage를&nbsp;이용한&nbsp;데이터&nbsp;저장</p>
<hr contenteditable="false" />
<p style="text-align: left;">2. 주요 기능<br />-&nbsp;수입/지출&nbsp;내역&nbsp;추가&nbsp;(입력&nbsp;검증&nbsp;포함:&nbsp;금액은&nbsp;숫자만&nbsp;허용) <br />-&nbsp;내역&nbsp;목록&nbsp;출력 <br />-&nbsp;수입/지출/전체&nbsp;필터링&nbsp;기능 <br />-&nbsp;총&nbsp;수입,&nbsp;총&nbsp;지출,&nbsp;잔액&nbsp;계산&nbsp;및&nbsp;실시간&nbsp;반영 <br />-&nbsp;내역&nbsp;삭제&nbsp;기능 <br />-&nbsp;로컬스토리지&nbsp;저장&nbsp;및&nbsp;불러오기</p>
<hr contenteditable="false" />
<p>3. 코드<br />(1).&nbsp;index.html</p>
<pre class="bash" id="code_1758698571010"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;account&lt;/title&gt;

    &lt;link rel="preconnect" href="https://fonts.googleapis.com"&gt;
    &lt;link rel="preconnect" href="https://fonts.gstatic.com" crossorigin&gt;
    &lt;link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100..900&amp;display=swap" rel="stylesheet"&gt;

    &lt;link rel="stylesheet" href="./style.css"&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="container"&gt;
        &lt;header&gt;
            &lt;h1&gt;가계부&lt;/h1&gt;
            &lt;div class="head"&gt;현재 잔액&lt;/div&gt;
            &lt;div class="show"&gt;
                &lt;span id="money"&gt;&lt;/span&gt;
            &lt;/div&gt;
        &lt;/header&gt;
        
        &lt;div class="list-input"&gt;
            &lt;input type="text" id="product" placeholder="내용을 입력하세요(예: 점심값, 월급)"&gt;
            &lt;input type="number" id="price" placeholder="금액을 입력하세요"&gt;
        &lt;/div&gt;
        &lt;div class="input-buttons"&gt;
            &lt;button class="btn-income"&gt;수입&lt;/button&gt;
            &lt;button class="btn-expense"&gt;지출&lt;/button&gt;&lt;br&gt;
        &lt;/div&gt;
        &lt;button id="list-add-btn" class="btn-add"&gt;추가하기&lt;/button&gt;

        &lt;div class="list-buttons"&gt;
            &lt;button data-filter="all" class="active"&gt;전체&lt;/button&gt;
            &lt;button data-filter="income"&gt;수입&lt;/button&gt;
            &lt;button data-filter="expense"&gt;지출&lt;/button&gt;
            
        &lt;/div&gt;
        &lt;div class="summary"&gt;
            &lt;div&gt;
                &lt;p&gt;총 수입&lt;/p&gt;
                &lt;span id="add-text" class="income"&gt;&lt;/span&gt;
            &lt;/div&gt;
            &lt;div&gt;
                &lt;p&gt;총 지출&lt;/p&gt;
                &lt;span id="lost-text" class="expense"&gt;&lt;/span&gt;
            &lt;/div&gt;
            &lt;div&gt;
                &lt;p&gt;잔액&lt;/p&gt;
                &lt;span id="money-text" class="balance"&gt;&lt;/span&gt;
            &lt;/div&gt;
        &lt;/div&gt;

        &lt;ul id="account-list" class="account-list"&gt;&lt;/ul&gt;
    &lt;/div&gt;

    &lt;script src="./script.js"&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p style="text-align: left;">&nbsp;</p>
<p>&nbsp;</p>
<p>(2). script.js</p>
<pre class="bash" id="code_1758698592002"><code>let accounts = JSON.parse(localStorage.getItem('accounts')) || [];
let filterState = 'all';

const accountList = document.getElementById('account-list');
const productInput = document.getElementById('product');
const priceInput = document.getElementById('price');
const filterBtns = document.querySelectorAll('.list-buttons button');
const btnIncome = document.querySelector('.btn-income');
const btnExpense = document.querySelector('.btn-expense');

let currentType = true;

btnIncome.addEventListener('click', function() {
    currentType = true; 
    btnIncome.classList.add('active');
    btnExpense.classList.remove('active');
});

btnExpense.addEventListener('click', function() {
    currentType = false; 
    btnExpense.classList.add('active');
    btnIncome.classList.remove('active');
});

function init(){
    bindEvents();
    render();
}

function bindEvents(){
    const addbtn = document.getElementById('list-add-btn');
    addbtn.addEventListener('click',addAccount);

    filterBtns.forEach(function(btn){
        btn.addEventListener('click',function(ev){
            setFilter(ev.target.dataset.filter);
        })
    })
}

function addAccount() {
    const description = productInput.value.trim();
    const amount = Number(priceInput.value);

    if (!description || !amount) return;

    const account = {
        id: Date.now(),
        description: description,
        amount: amount,
        type: currentType,
        date: new Date().toLocaleDateString(),
        completed: false
    };

    accounts.push(account);

    productInput.value = "";
    priceInput.value = "";

    saveAccounts();
    render();
}

function deleteAccount(id){
    const newAccount = [];
    for (let account of accounts){
        if(account.id === id)
            continue;

        newAccount.push(account);
    }
    accounts = newAccount;
    saveAccounts();
    render();
}

function getFilteredAccounts(){
    const filteredAccounts = [];
    if(filterState === 'income'){
        for(let account of accounts){
            if(account.type == true){
                filteredAccounts.push(account);
            }
        }
    } else if(filterState === 'expense'){
        for(let account of accounts){
            if(account.type === false){
                filteredAccounts.push(account);
            }
        }
    } else{
        return accounts;
    }

    return filteredAccounts;
}

function saveAccounts(){
    localStorage.setItem('accounts',JSON.stringify(accounts));
}

function render(){
    accountList.innerHTML = "";

    const filteredAccounts = getFilteredAccounts();

    if(filteredAccounts.length === 0){
        emptyStateRender();
    } else{
        filteredAccounts.forEach(function (account){
            accountItemRender(account);
        })
    }

    updateCount();
    updateClearButton();
}

function emptyStateRender(){
    const emptyEl = document.createElement('div');
    emptyEl.className = 'empty-state';
    emptyEl.innerHTML = '가계부가 없습니다';
    accountList.appendChild(emptyEl);
}

function accountItemRender(account){
    const accountItem = document.createElement('li');
    const sign = account.type ? '+' : '-';
    const amountClass = account.type ? 'income-amount' : 'expense-amount';
    accountItem.className = 'account-item' + (account.completed ? 'completed' : '');

    accountItem.innerHTML = `&lt;div class="account-info"&gt;
            &lt;span class="date"&gt;${account.date}&lt;/span&gt;
            &lt;span class="description"&gt;${account.description}&lt;/span&gt;
            &lt;/div&gt;
            &lt;span class="${amountClass}"&gt;${sign}${account.amount.toLocaleString()}원&lt;/span&gt;
            &lt;button class="delete-btn"&gt;삭제&lt;/button&gt;`;

    const deleteBtn = accountItem.querySelector('.delete-btn');

    if (deleteBtn) {
        deleteBtn.addEventListener('click', function() {
            deleteAccount(account.id);
        });
    }

    accountList.appendChild(accountItem);

}

function setFilter(filter){
    filterState = filter;

    filterBtns.forEach(function(btn){
        btn.className = (btn.dataset.filter === filter ? "active" : "");
    })

    render();
}

function updateCount() {
    const filteredAccounts = getFilteredAccounts();
    
    let totalIncome = 0;
    let totalExpense = 0;

    for (let account of accounts) {
        if (account.type) { 
            totalIncome += account.amount;
        } else {           
            totalExpense += account.amount;
        }
    }

    const balance = totalIncome - totalExpense;

    document.getElementById('add-text').textContent = totalIncome.toLocaleString() + "원";
    document.getElementById('lost-text').textContent = totalExpense.toLocaleString() + "원";
    document.getElementById('money').textContent = balance.toLocaleString() + "원";
    document.getElementById('money-text').textContent = balance.toLocaleString() + "원";
}




document.addEventListener('DOMContentLoaded', init);</code></pre>
<p>&nbsp;</p>
<p>(3). style.css</p>
<pre class="bash" id="code_1758698624066"><code>*{
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
    background: linear-gradient(135deg, #764ba2, #667eea);
    padding: 20px;
}

button{
    border: none;
    outline: none;
}

.container{
    max-width: 600px;
    margin: 0 auto;
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(255, 245, 245, 0.336);
}

header {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    text-align: center;
    padding: 30px 0;
}

header h1{
    font-size: 40px;
    font-weight: 300;
    letter-spacing: 2px;
}

.list-input{
    display: flex;
    padding: 20px;
    border-bottom: 1px solid rgb(224, 224, 224);
}

.list-input input{
    flex: 1;
    padding: 15px;
    border: 2px solid rgb(224, 224, 224);
    border-radius: 8px;
    font-size: 16px;
    outline: none;
    transition: border-color 0.3s ease;
}

.list-input input:focus{
    border-color: #5D688A;
}

.input-buttons {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 10px;
}

.input-buttons button {
    padding: 8px 20px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    border: 2px solid transparent;
    transition: all 0.3s ease;
    background: white;
}

.btn-income {
    background: white; 
    color: #4CAF50; 
    border: 1px solid #4CAF50 !important;
    
}

.btn-expense {
    background: white;
    color: #e46464;
    border: 1px solid #e46464 !important;
}

.btn-expense:hover {
    background: white;
}

.btn-add {
    width: 90%;
    padding: 14px;
    margin: 15px auto 0;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 700;
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    cursor: pointer;
    transition: opacity 0.3s ease;
    display: block;
}

.btn-add:hover {
    opacity: 0.9;
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

.empty-state{
    text-align: center;
    padding: 40px 20px;
    color: #667eea;
    font-size: 16px;
    font-weight: 600;
}

.list-buttons{
    display: flex;
    justify-content: center;
    padding: 20px;
    border-bottom: 1px solid rgb(224, 224, 224);
    gap: 10px;
}

.list-buttons button{
    padding: 8px 16px;
    border: 2px solid rgb(224, 224, 224);
    background: white;
    border-radius: 20px;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.3s ease;
}

.list-buttons button:hover,
.list-buttons button.active{
    background: #667eea;
    color: white;
    border-color: #667eea;
}

.summary {
    display: flex;
    justify-content: space-around; 
    text-align: center;
    background: rgb(236, 236, 236);
    padding: 20px 0;
    border-radius: 10px;
}

.summary p {
    margin: 0;
    font-weight: 600;
    color: #555;
}

.summary span {
    font-size: 18px;
    font-weight: bold;
    display: block;
    margin-top: 5px;
}

.income {
    color: green;
}

.expense {
    color: red;
}

.balance {
    color: green;
}
.income-amount {
    color: green;
    font-weight: bold;
}

.expense-amount {
    color: red;
    font-weight: bold;
}

.account-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #ddd;
}

.account-info {
    display: flex;
    flex-direction: column;
}

.btn-income.active {
    background: #4CAF50;
    color: white;
    border: 2px solid #4CAF50;
}

.btn-expense.active {
    background: #f44336;
    color: white;
    border: 2px solid #f44336;
}

.show {
    font-size: 23px;
    color: rgb(103, 209, 103);
    font-weight: bold;
}</code></pre>
<hr contenteditable="false" />
<p>4. 페이지</p>
<p>(1). 메인 페이지</p>
<p><figure class="imageblock alignCenter"><span><img height="681" src="https://blog.kakaocdn.net/dn/nTHFG/btsQMpvaQba/wlSGNzn7uvgEh4MPnOJLpk/img.png" width="621" /></span></figure>
</p>
<p>&nbsp;</p>
<p>(2). 수입 추가</p>
<p><figure class="imageblock alignCenter"><span><img height="648" src="https://blog.kakaocdn.net/dn/V4DDP/btsQMGXRv6l/WdLFSymusg5yL39JPVVLK1/img.png" width="615" /></span></figure>
</p>
<p>(3). 지출 추가</p>
<p><figure class="imageblock alignCenter"><span><img height="715" src="https://blog.kakaocdn.net/dn/wswCw/btsQMpomiWv/DOT0nC050ym9IvW5riZREK/img.png" width="617" /></span></figure>
</p>
<p>(4) 수입만 출력</p>
<p><figure class="imageblock alignCenter"><span><img height="645" src="https://blog.kakaocdn.net/dn/bmvX1r/btsQLyTDjKi/sa7EAdWMyDjG3uCvqbzH51/img.png" width="617" /></span></figure>
</p>
<p>(5) 지출만 출력</p>
<p><figure class="imageblock alignCenter"><span><img height="644" src="https://blog.kakaocdn.net/dn/l32Nl/btsQMOnXtCb/VRXkCnWuKS7oI026Kn17Vk/img.png" width="617" /></span></figure>
</p>
<p>&nbsp;</p>