JavaScript practical 4: A frequently asked questions control

Toggle extra information and keep its button state understandable.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Delivery information
[Show answer]
Click: Sample delivery time: 3 working days.
Button changes to [Hide answer]

WHAT THE CODE DOES
const versus let: References stay bound; open is reassigned after every click.
false, true and !: Boolean state and logical negation switch between closed and open.
hidden: Hide or reveal the answer element.
setAttribute and String(): Update the accessibility state as the text true or false.
? : conditional operator: Choose one button label according to the current state.
querySelector, event listener and textContent: Connect the existing HTML to the click behaviour and label.
HTML button, aria-controls, aria-expanded and hidden: Identify the controlled answer and starting closed state. A real button supports keyboard activation.

TRY IT
Write a different question and answer. Test using Tab and Enter only.

CHECK
First click reveals; second click hides.
aria-expanded matches the visible state.