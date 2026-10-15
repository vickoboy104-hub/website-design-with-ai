CSS practical 2: A product card with breathing room

Use the box model to make a merchandise card.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Canvas tote bag
Reusable bag for everyday essentials.
Sample price: NGN 6000
Rounded blue border
24 px of inner space

WHAT THE CODE DOES
* and box-sizing: Apply border-box sizing to all elements so declared width includes padding and border.
body and .card: Choose the page body and the card class.
padding and margin: Space inside the card versus space outside it.
border and border-radius: Draw an edge and round its corners.
max-width and background: Limit card width and fill its background.
.price and font-weight: Make the price paragraph bold.
HTML article, h1, p and class: Group a standalone product, name it, describe it and attach style hooks.

TRY IT
Change padding from 24px to 4px, observe, then restore it.

CHECK
Text never touches the border.
The price is bold.