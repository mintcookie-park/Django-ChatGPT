function switchLoad() {
  let loaderContainer = document.querySelector(".loader-container");
  loaderContainer.classList.toggle("show");
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}
loginToken = getCookie("loginToken");
document.addEventListener("DOMContentLoaded", loadChat());

function loadChat() {
  fetch("http://127.0.0.1:8000/?token=" + loginToken + "&room=test")
    .then((response) => response.json())
    .then((data) => {
      // 요청이 성공적으로 완료된 후에 실행될 코드
      const response = document.getElementById("response");
      data.forEach((element) => {
        makeUserChatBox(element.prompt);
        makeAIChatBox(element.response);
        // const promptEl = document.createElement("li");
        // const responseEl = document.createElement("li");
        // promptEl.innerText = element.prompt;
        // responseEl.innerText = element.response;
        // response.append(promptEl, responseEl);
      });
      keepScrollDown();
    })
    .catch((error) => {
      // 요청 중 에러가 발생했을 때 실행될 코드
      console.error("요청 에러:", error);
    });
}

function askQuestion() {
  switchLoad();
  const questionInput = document.getElementById("question");
  const question = questionInput.value;
  questionInput.value = "";
  if (question) {
    makeUserChatBox(question);
    fetch("http://127.0.0.1:8000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt: question, room: "test", token: loginToken }),
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

// userChat이 들어갈 userChatBox를 만드는 함수
const makeUserChatBox = (userChat) => {
  const $chatScreen = document.querySelector(".chat-screen");
  const userChatBox = document.createElement("div");
  userChatBox.classList.add("user-chat");
  const userChatContent = document.createElement("div");
  userChatContent.classList.add("user-chat-content");
  userChatContent.innerText = userChat;
  userChatBox.appendChild(userChatContent);
  $chatScreen.appendChild(userChatBox);
  keepScrollDown();
};

// AIChat이 들어갈 AIChatBox를 만드는 함수
const makeAIChatBox = (aiChat) => {
  const $chatScreen = document.querySelector(".chat-screen");
  const aiChatBox = document.createElement("div");
  aiChatBox.classList.add("ai-chat");

  const aiImg = document.createElement("img");
  aiImg.classList.add("ai-img");
  aiImg.setAttribute("src", "asset/img/ai_img_cat.jpg");
  //   aiImg.addEventListener("click", changeAIImg);
  aiChatBox.appendChild(aiImg);

  const aiChatContent = document.createElement("div");
  aiChatContent.classList.add("ai-chat-content");
  aiChatContent.innerText = aiChat;
  aiChatBox.appendChild(aiChatContent);
  $chatScreen.appendChild(aiChatBox);
  keepScrollDown();
};

// 항상 가장 밑에 스크롤을 유지하는 함수
function keepScrollDown() {
  const $chatScreen = document.querySelector(".chat-screen");
  $chatScreen.scrollTop = $chatScreen.scrollHeight;
}
