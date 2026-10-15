JavaScript practical 2: A printing cost calculator

Multiply a valid quantity by a fixed classroom unit price.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Print estimate
Number of flyers [50]  [Calculate]
Sample estimate: NGN 5000
1.5 or 0: helpful range error

WHAT THE CODE DOES
querySelector, const and addEventListener: Find controls, retain references and respond to a click.
function, parameters and return: Define a reusable calculation receiving quantity and price.
Number() and field.value: Convert a field string to a number; an empty string becomes 0 and is rejected by the range test.
Number.isInteger(), ! and ||: Reject a non-integer or any value outside the range.
<, > and *: Compare lower/upper limits and multiply values.
textContent and +: Show an error or join the label to the calculated total.
HTML number input, min and step: Suggest whole positive values; JavaScript still checks them. Label, button and live paragraph provide accessible interaction.

TRY IT
Change the sample price to 150 and calculate 20 flyers. Expected: 3000.

CHECK
50 gives 5000.
Empty, 0, 1.5 and 1001 are rejected.