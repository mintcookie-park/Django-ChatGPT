# DjangoDRF-ChatGPT
+ Django DRF로 ChatGPT API와 연동하는 프로젝트 repository입니다.

# 1. 프로젝트 목표
+ Django DRF와 ChatGPT API를 이용하여 영어학습 챗봇 서비스 구현

# 2. 개발 환경 및 배포 URL
2.1 개발 환경
- 기술 스택
  
+  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">

+  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">

+  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">

+  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

+  <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">

+  <img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white">

+  <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">

+  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">

+  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">

# 3. 프로젝트 구조와 개발 일정
3.1 ERD model

<img width="1933" alt="ERD구조" src="https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/46a8df2d-f50e-4190-b5df-f17a3e845bd2">

3.2 폴더 구조

```
django-chat
├── account
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── chat
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chatbot
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── venv
    ├── bin
    ├── include
    ├── lib
    └── pyvenv.cfg
```

3.3 개발 일정
+ 2023.11.21 ~ 2023.11.30

# 4. 페이지 화면
## 4.1 Main & 채팅
|Main|채팅|
|:---:|:---:|
|![메인](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/ba7de45b-ccb5-4863-aa62-da6104859737)|![채팅화면](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/4490752d-cabb-4a67-96c5-f661b3cfdd26)|

## 4.2 User 계정
|로그인|회원가입|
|:---:|:---:|
|![로그인](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/e49e6296-c50e-4b5f-ab82-01423646f812)|![회원가입](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/c6ad537e-d750-4cac-8695-9129bfab0e8b)|



# 5. 기능
## 5.1 URL 리스트
|URL|기능|
|:---|:---|
|'list'|채팅창 목록|
|'chatbot/chat'|채팅|
|'/account/register'|회원가입|
|'/account/login'|로그인|
|'/account/logout'|로그아웃|

## 5.2 세부 기능
+ 회원가입

  
![회원가입](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/7f9cac6f-b31f-406b-9e80-a0d7da9bc500)

```
document.getElementById("register-form").addEventListener("submit", function (e) {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  fetch("http://127.0.0.1:8000/account/register/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username: username, password: password }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.state) {
        alert("회원가입이 완료되었습니다.");
        window.location.replace("./login.html");
      } else {
        const error_msg = JSON.stringify(data.error);
        alert(error_msg);
      }
    })
    .catch((error) => {
      alert("회원가입 실패: " + error.message);
    });
});
```

입력된 username과 password로 새로운 User를 저장하고, 해당 user에 연결된 token을 생성한다. 정상적으로 회원가입이 된 경우에는 state가 True로 전달된다. front-end에서 state를 확인하고, true이면 로그인 페이지도 이동한다.

+ 로그인 로그아웃

|로그인|로그아웃|
|:---:|:---:|
|![로그인](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/b3925711-22fc-4ba1-b14a-5dfed670bfe3)|![로그아웃](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/b8b63e7e-4089-4c86-9507-cf8987174c95)|

```
function checkToken() {
  const loginToken = document.cookie.match("(^|;) ?" + "loginToken" + "=([^;]*)(;|$)");
  if (loginToken) {
    alert("이미 로그인된 상태입니다.");
    window.location.replace("./index.html");
  }
}
```

username과 password를 입력받아서 "/account/login/"로 POST 요청을 보낸다. 서버에서 로그인 인증에 성공하면 state True와 함께 해당 user의 token을 전달한다. 브라우저에서는 state가 ture인지 확인하고 username와 token을 쿠키에 저장한 후 메인 페이지로 이동한다.

```
function checkToken() {
  const loginToken = document.cookie.match("(^|;) ?" + "loginToken" + "=([^;]*)(;|$)");
  if (loginToken) {
    alert("이미 로그인된 상태입니다.");
    window.location.replace("./index.html");
  }
}
```
로그인 페이지로 이동하면 우선 쿠키에 token이 저장되어 있는지를 확인하여 현재 로그인 상태인지 체크한다. 만약 이미 로그인된 상태이면 alert로 이를 알려주고 메인 페이지로 이동한다.

+ 네비게이션 바

|로그인|로그아웃|
|:---:|:---:|
|![로그인_네비게이션바](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/1d4c02ff-ff37-44be-9635-19a5193810cb)|![로그아웃_네비게이션바](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/77cafab3-47f5-46f2-a1d9-274f0622e02f)|

```
const loginToken = getCookie("loginToken");
const navBtnList = document.querySelector(".nav-btn");
if (loginToken) {
  navBtnList.innerHTML = `
    <li class="nav-item">
        <span class="navbar-text"> 환영합니다 ${username} 님 | </span>
    </li>
    <li class="nav-item">
        <a class="nav-link" onclick="logout()" href="./index.html">로그아웃</a>
    </li>`;
} else {
  navBtnList.innerHTML = `
    <li class="nav-item">
        <a class="nav-link" href="./login.html">로그인</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="./register.html">회원가입</a>
    </li>
    `;
}
```

로그인이 성공적으로 이루어지면 브라우저 쿠키에 token과 username을 저장한다. 쿠키에 loginToken이 저장되어 있는지 확인하여 로그인 여부를 알 수 있고, 로그인 상태이면 네비게이션 바에 username과 함께 로그아웃 버튼을 출력한다. 로그아웃된 상태이면 로그인과 회원가입 버튼을 출력한다.


+ 채팅방 목록
  
|로그인 전|로그인 후|
|:---:|:---:|
|![채팅방목록_로그인전](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/2d436ee7-ef9d-442d-a860-d960560b2c5d)|![채팅방목록_로그인후](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/ff4dca9a-2dc0-4a15-95d0-965e17587b59)|

로그인이 성공적으로 이루어지면 메인화면으로 연결된다. 로그인된 상태에서는 메인화면에 해당 유저가 생성한 채팅방 목록이 출력되며, 클릭하여 해당 채팅방으로 이동할 수 있다.
로그인되지 않은 상태에서는 채팅방 목록이 출력되지 않는다.

+ 채팅
  
|불러오기|채팅|
|:---:|:---:|
|![채팅불러오기](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/a4f449b7-5a0b-4fa7-8801-af8b71a53b01)|![채팅_채팅](https://github.com/mintcookie-park/Django-ChatGPT/assets/79849531/58ea9bb1-f4c6-4a1d-bd0e-25407e976075)|



```
function loadChat() {
  fetch("http://127.0.0.1:8000/?room=" + room)
    .then((response) => response.json())
    .then((data) => {
      // 요청이 성공적으로 완료된 후에 실행될 코드
      const response = document.getElementById("response");
      data.forEach((element) => {
        makeUserChatBox(element.prompt);
        makeAIChatBox(element.response);
      });
      keepScrollDown();
    })
    .catch((error) => {
      // 요청 중 에러가 발생했을 때 실행될 코드
      console.error("요청 에러:", error);
    });
}
```

채팅방 목록에서 하나를 선택하면, 서버의 '/chatbot/chat/'으로 GET 요청을 보내서 현재 로그인된 유저와 선택된 채팅방 정보를 전달한다. 서버에서는 유저와 채팅방 이름으로 선택한 채팅방을 찾고, 해당 채팅방에 연결된 모든 메시지를 DB로부터 시간순으로 찾아 브라우저로 전달한다. 브라우저에서는 prompt와 response를 구분하여 UserChatBox와 AIChatBox를 생성하고, keepScrollDown 함수를 통해 채팅 화면을 아래로 스크롤하여 가장 최신 메시지가 출력되도록 한다.

```
function askQuestion() {
  switchLoad();
  const questionInput = document.getElementById("question");
  const question = questionInput.value;
  questionInput.value = "";
  if (question) {
    makeUserChatBox(question);
    fetch("http://127.0.0.1:8000/?room=" + room, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt: question, token: loginToken }),
    })
      .then((response) => response.json())
      .then((data) => {
        switchLoad();
        makeAIChatBox(data[0]["response"]);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
}
```
채팅을 입력하고 제출하면 해당 element의 value를 post로 서버에 전달한다. 이때 제출 후 답변이 출력되기 전까지 switchLoad() 함수를 통해 loading modal을 화면에 출력한다.

# 6. 향후 개선 사항
## 6.1 코드 에러
+ 채팅화면 CSS

  채팅 화면은 HTML, CSS, JavaScript를 이용한 지난 프로젝트를 활용하였다. 이때 bootstrap을 적용하지 않고 순수 CSS로 제작하였기 때문에 이번 프로젝트에서 bootstrap을 적용했을 때 여러 오차가 발생하였다. 그 중 채팅 화면에  서 네비게이션 바를 적용을 못한 문제와 채팅 입력창의 가운데 정렬이 안 맞는 문제가 있었습니다.

## 6.2 코드 개선
+ DB 중복 요청

  브라우저에서 GET으로 채팅화면을 불러오는 요청을 하면, 서버에서는 DB로 해당 채팅방에 속하는 모든 메시지를 가져온다. 이때 채팅 화면을 새로고침하게 될 경우, 매번 서버에서 DB 요청을 하게 된다. 쿠키를 통해서 새로운 채팅방으로의 이동인지, 현재 채팅방에서의 새로고침인지를 확인할 수 있는 방법이 필요하다.

+ JavaScript 파일 구조

  현재 각 HTML 페이지 별로 개별 js 파일이 연결되여 작동되고 있다. 따라서 getToken과 같은 함수들이 중복되어 선언된다. DOM build, function Modul과 같이 기능을 기준으로 구분하는 새로운 파일 구조화 작업이 필요하다.

## 6.3 추가 기능 구현
+ 채팅방 추가 및 삭제

  메인 화면에 출력되는 채팅방 목록 중 일부 채팅방을 삭제하거나 새로 만드는 기능이 구현되어 있지 않다. 기존 채팅방을 불러오는 기능 이외에도 생성, 삭제, 이름 수정과 같은 기능의 구현이 필요하다.
  
+ OAuth 2.0

  본 프로젝트에서는 유저 인증 과정에서 django rest_framework의 authentication 기능을 사용하였다. OAuth 2.0과 같은 외부 프로토콜을 사용한다면 제 3자 서비스로부터의 소셜 로그인 기능을 구현할 수 있을 것이다.
  
# 7. 개발 과정에서 느낀 점

각 페이지에서 정보를 어떤 방법으로 서버와 주고 받을 지에 대한 고민을 할때 가장 어려웠다. 기능 구현에 중점을 두고 프로젝트를 진행했어서 현재 확장성과 효율 부분에서 다소 아쉬웠다. 특히 내장된 기능을 충분히 활용하지 못한 점과 보안상 취약한 부분이 많다는 점이 느껴졌다.

이번 프로젝트에서 Django Rest Framework의 기본 구조를 이해할 수 있었다. 아쉬운 부분이 있는 만큼 앞으로 보안과 확장성 부분을 더 공부해야 된다는 걸 깨닫고 다음 공부는 이 부분들을 중점으로 계획을 수립하고 있다.
