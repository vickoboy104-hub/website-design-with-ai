const field = document.querySelector('#quantity');
const result = document.querySelector('#result');
function totalFor(quantity, price) {
  return quantity * price;
}
document.querySelector('#calculate').addEventListener('click', function () {
  const quantity = Number(field.value);
  if (!Number.isInteger(quantity) || quantity < 1 || quantity > 1000) {
    result.textContent = 'Enter a whole number from 1 to 1000.';
    return;
  }
  result.textContent = 'Sample estimate: NGN ' + totalFor(quantity, 100);
});