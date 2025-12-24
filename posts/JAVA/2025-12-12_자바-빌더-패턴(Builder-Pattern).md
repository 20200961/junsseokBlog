# 자바 빌더 패턴(Builder Pattern)

**카테고리**: JAVA

**작성일**: Fri, 12 Dec 2025 17:18:55 +0900

**원문 링크**: https://junsseok.tistory.com/60

---

<p style="text-align: center;">자바 빌더 패턴(Builder Pattern)</p>
<hr contenteditable="false" />
<h3 style="text-align: center;">자바의 빌더 패턴이란?</h3>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><b>필요한 값만 선택해서 순서와 상관없이 객체를 만들 수 있게 하는 패턴</b></p>
<hr contenteditable="false" />
<p style="text-align: left;">자바로 객체 생성하다 보면 생성자에 매개변수가 엄청 많아질 때가 있어요. 그럴 때마다 뭐가 뭔지 헷갈리고... 이거 순서 바꾸면 또 컴파일 에러나고 그러죠. 그래서 알게 된 게 빌더 패턴입니다.</p>
<hr contenteditable="false" />
<h3 style="text-align: left;">왜 필요할까?</h3>
<pre class="bash" id="code_1765526782171"><code>// 이런 클래스가 있다고 해봅시다
public class User {
    private String name;
    private int age;
    private String email;
    private String phone;
    private String address;
    
    // 생성자 1
    public User(String name) { ... }
    
    // 생성자 2
    public User(String name, int age) { ... }
    
    // 생성자 3
    public User(String name, int age, String email) { ... }
    
    // 생성자 4
    public User(String name, int age, String email, String phone) { ... }
    
    // 생성자 5 (뭐가 뭔지 모르겠음...)
    public User(String name, int age, String email, String phone, String address) { ... }
}

// 사용할 때
User user = new User("홍길동", 25, "hong@email.com", "010-1234-5678", "서울");</code></pre>
<p>&nbsp;</p>
<p>-&gt; 이런 식으로 생성자가 점점 늘어나면 :</p>
<p>&nbsp;</p>
<p>(1) 매개변수 순서 외우기 힘들어요선택적</p>
<p>(2) 매개변수 처리가 복잡해요</p>
<p>(3) 가독성이 완전 떨어져요</p>
<hr contenteditable="false" />
<h2 style="text-align: left;">빌더 패턴으로 해결</h2>
<p>빌더 패턴을 쓰면 이렇게 깔끔해집니다.</p>
<p>&nbsp;</p>
<pre class="bash" id="code_1765526950092"><code>public class User {
    // 필드들
    private String name;
    private int age;
    private String email;
    private String phone;
    private String address;
    
    // private 생성자 - 직접 생성 못하게
    private User(Builder builder) {
        this.name = builder.name;
        this.age = builder.age;
        this.email = builder.email;
        this.phone = builder.phone;
        this.address = builder.address;
    }
    
    // Builder 정적 내부 클래스
    public static class Builder {
        // 필수 매개변수
        private final String name;
        
        // 선택적 매개변수 - 기본값으로 초기화
        private int age = 0;
        private String email = "";
        private String phone = "";
        private String address = "";
        
        // 필수 매개변수는 생성자로
        public Builder(String name) {
            this.name = name;
        }
        
        // 선택적 매개변수는 메서드로 (메서드 체이닝)
        public Builder age(int age) {
            this.age = age;
            return this;
        }
        
        public Builder email(String email) {
            this.email = email;
            return this;
        }
        
        public Builder phone(String phone) {
            this.phone = phone;
            return this;
        }
        
        public Builder address(String address) {
            this.address = address;
            return this;
        }
        
        // 최종적으로 User 객체 생성
        public User build() {
            return new User(this);
        }
    }
}

// 이렇게 사용!
User user = new User.Builder("홍길동")
    .age(25)
    .email("hong@email.com")
    .phone("010-1234-5678")
    .address("서울")
    .build();

// 필요한 것만 선택적으로!
User simpleUser = new User.Builder("김철수")
    .email("kim@email.com")
    .build();</code></pre>
<hr contenteditable="false" />
<h2 style="text-align: left;">실제 사용 예시: 커피 주문</h2>
<p>좀 더 재밌는 예시로 볼까요?</p>
<pre class="bash" id="code_1765527095563"><code>public class Coffee {
    private String size;
    private boolean hasMilk;
    private boolean hasShot;
    private boolean hasWhippedCream;
    private int sugarCount;
    
    private Coffee(Builder builder) {
        this.size = builder.size;
        this.hasMilk = builder.hasMilk;
        this.hasShot = builder.hasShot;
        this.hasWhippedCream = builder.hasWhippedCream;
        this.sugarCount = builder.sugarCount;
    }
    
    public static class Builder {
        // 필수: 사이즈는 필수로 선택
        private final String size;
        
        // 선택사항들
        private boolean hasMilk = false;
        private boolean hasShot = false;
        private boolean hasWhippedCream = false;
        private int sugarCount = 0;
        
        public Builder(String size) {
            this.size = size;
        }
        
        public Builder addMilk() {
            this.hasMilk = true;
            return this;
        }
        
        public Builder addShot() {
            this.hasShot = true;
            return this;
        }
        
        public Builder addWhippedCream() {
            this.hasWhippedCream = true;
            return this;
        }
        
        public Builder sugar(int count) {
            this.sugarCount = count;
            return this;
        }
        
        public Coffee build() {
            return new Coffee(this);
        }
    }
    
    @Override
    public String toString() {
        return String.format("Coffee[size=%s, milk=%b, shot=%b, cream=%b, sugar=%d]",
            size, hasMilk, hasShot, hasWhippedCream, sugarCount);
    }
}

// 주문해봅시다!
public class CoffeeShop {
    public static void main(String[] args) {
        // 아메리카노 톨사이즈
        Coffee americano = new Coffee.Builder("Tall").build();
        
        // 카페라떼 - 우유 추가
        Coffee latte = new Coffee.Builder("Grande")
            .addMilk()
            .build();
        
        // 커스텀 커피 - 내 맘대로!
        Coffee custom = new Coffee.Builder("Venti")
            .addMilk()
            .addShot()
            .addWhippedCream()
            .sugar(2)
            .build();
        
        System.out.println(americano);
        System.out.println(latte);
        System.out.println(custom);
    }
}</code></pre>
<hr contenteditable="false" />
<h2>빌더 패턴의 장점</h2>
<p>(1) 가독성 최고: 뭘 설정하는지 명확해요</p>
<p><span style="color: #333333; text-align: start;">(2)<span> </span></span>유연성: 필요한 것만 골라서 설정 가능</p>
<p><span style="color: #333333; text-align: start;">(3)</span> 불변 객체: 한번 생성하면 안전하게 사용 가능</p>
<p><span style="color: #333333; text-align: start;">(4)</span> 유효성 검사: build() 메서드에서 검증 로직 추가 가능</p>
<pre class="bash" id="code_1765527139987"><code>public User build() {
    // 유효성 검사 추가 가능!
    if (name == null || name.isEmpty()) {
        throw new IllegalStateException("이름은 필수입니다!");
    }
    if (age &lt; 0) {
        throw new IllegalStateException("나이는 0보다 커야 합니다!");
    }
    return new User(this);
}</code></pre>
<p>&nbsp;</p>
<h2>Lombok으로 더 간단하게!</h2>
<p>사실 매번 Builder 클래스 작성하기 귀찮잖아요? Lombok 쓰면 어노테이션 하나로 끝입니다</p>
<pre class="bash" id="code_1765527247467"><code>import lombok.Builder;
import lombok.Getter;
import lombok.ToString;

@Getter
@Builder
@ToString
public class User {
    private String name;
    private int age;
    private String email;
    private String phone;
    private String address;
}

// 사용은 똑같아요!
User user = User.builder()
    .name("홍길동")
    .age(25)
    .email("hong@email.com")
    .build();</code></pre>
<p>&nbsp;</p>
<p>-&gt; Lombok이 알아서 Builder 코드를 만들어줍니다. 개발자는 편하고, 코드는 깔끔해요.</p>
<hr contenteditable="false" />
<h2>주의할 점</h2>
<p><span style="color: #333333; text-align: start;">(1)<span>&nbsp;</span></span> 필드가 4개 이하면 굳이 빌더 패턴 안 써도 돼요. 오버엔지니어링이 될 수 있어요.</p>
<p><span style="color: #333333; text-align: start;">(2)<span>&nbsp;</span></span> 빌더 객체 생성 비용이 있어서 성능이 정말 중요한 상황에서는 고려해야 해요.</p>
<p>(3) 팀 컨벤션에 따라 필수 필드 처리 방식을 정해두는 게 좋아요.</p>
<hr contenteditable="false" />
<h2>정리하면</h2>
<p>빌더 패턴은 복잡한 객체를 깔끔하게 생성할 수 있게 해주는 패턴입니다.</p>
<p>처음엔 코드가 좀 길어 보여도, 실제로 쓰다 보면 진짜 편합니다.</p>
<p>특히 생성자 매개변수가 많거나 선택적 매개변수가 많을 때 빛을 발해요.</p>
<hr contenteditable="false" />
<h2 style="text-align: center;">면접 한줄요약</h2>
<p>&nbsp;</p>
<p style="text-align: center;"><b>복잡한 객체 생성 과정을 단계별로 분리하고, 메서드 체이닝을 통해 가독성 높고 유연한 </b></p>
<p style="text-align: center;"><b>객체 생성을 가능하게 하는 생성 패턴입니다.</b></p>
<p>&nbsp;</p>