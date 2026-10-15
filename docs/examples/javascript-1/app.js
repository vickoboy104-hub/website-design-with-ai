const nameField = document.querySelector('#name');
const button = document.querySelector('#greet');
const result = document.querySelector('#result');
button.addEventListener('click', function () {
  const name = nameField.value.trim();
  if (name === '') {
    result.textContent = 'Please enter your first name.';
    return;
  }
  result.textContent = 'Hello, ' + name + '!';
});