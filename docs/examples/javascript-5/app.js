const classes = ['Baking basics', 'Bag sewing', 'Web design'];
const field = document.querySelector('#search');
const list = document.querySelector('#results');
function showClasses() {
  const query = field.value.trim().toLowerCase();
  const matches = classes.filter(function (name) {
    return name.toLowerCase().includes(query);
  });
  list.textContent = '';
  for (const name of matches) {
    const item = document.createElement('li');
    item.textContent = name;
    list.append(item);
  }
  if (matches.length === 0) list.textContent = 'No matching class.';
}
field.addEventListener('input', showClasses);
showClasses();