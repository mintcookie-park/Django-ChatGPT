// register.html

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
      console.log(data);
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
