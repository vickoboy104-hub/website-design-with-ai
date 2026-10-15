const button = document.querySelector('#toggle');
const answer = document.querySelector('#answer');
let open = false;
button.addEventListener('click', function () {
  open = !open;
  answer.hidden = !open;
  button.setAttribute('aria-expanded', String(open));
  button.textContent = open ? 'Hide answer' : 'Show answer';
});