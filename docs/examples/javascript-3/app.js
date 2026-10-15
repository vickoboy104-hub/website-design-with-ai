const services = [
  { name: 'Logo print', price: 1500 },
  { name: 'Name embroidery', price: 2500 },
  { name: 'Bag branding', price: 2000 }
];
const list = document.querySelector('#services');
for (const service of services) {
  const item = document.createElement('li');
  item.textContent = service.name + ': NGN ' + service.price;
  list.append(item);
}