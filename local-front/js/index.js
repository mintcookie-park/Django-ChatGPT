// index.html

function logout() {
  document.cookie = `
  loginToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;
  User=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;
  `;
}
