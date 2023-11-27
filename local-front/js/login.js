// login.html

checkToken();

function setTokenToCookie(token) {
  const cookieString = `loginToken=${token}; path=/;`;
  document.cookie = cookieString;
}
function setUserToCookie(username) {
  const cookieString = `User=${username}; path=/;`;
  document.cookie = cookieString;
}

function checkToken() {
  const loginToken = document.cookie.match("(^|;) ?" + "loginToken" + "=([^;]*)(;|$)");
  if (loginToken) {
    alert("이미 로그인된 상태입니다.");
    window.location.replace("./index.html");
  }
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

const csrfToken = getCookie("csrftoken");
document.getElementById("login-form").addEventListener("submit", function (e) {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  fetch("http://127.0.0.1:8000/account/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({ username: username, password: password }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.state) {
        alert(`로그인 성공 : ${data.username}`);
        setTokenToCookie(data.token);
        setUserToCookie(data.username);
        window.location.replace("./index.html");
      } else {
        alert(data.message);
      }
    })
    .catch((error) => {
      alert("로그인 실패: " + error.message);
    });
});
