const container = document.getElementById('container');
const registerBtn = document.getElementById('register_sudo');
const loginBtn = document.getElementById('login_sudo');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});