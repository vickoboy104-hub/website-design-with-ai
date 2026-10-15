JavaScript practical 3: A small service catalogue

Render an array of service objects as page content.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Our services
• Logo print: NGN 1500
• Name embroidery: NGN 2500
• Bag branding: NGN 2000

WHAT THE CODE DOES
[ ] and commas: Define an array containing several values.
{ name, price } and colon: Define an object with named properties for one service.
const, querySelector and #services: Keep the catalogue and find the destination list.
for...of: Repeat the block once for each service object.
createElement, li and append: Create an HTML list item and attach it to the list.
service.name and service.price: Read object properties using dot notation.
textContent and +: Construct and insert plain text, not interpreted HTML.
HTML main, h1 and ul: Provide a page heading and an initially empty unordered list.

TRY IT
Add a fourth object. The loop should show it without another append statement.

CHECK
Three list items appear.
Changing one price changes only that item.