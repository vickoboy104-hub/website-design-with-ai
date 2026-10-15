JavaScript practical 1: A visitor greeting on a page

Read a name from a field and update the page safely.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Welcome to our workshop
First name [Ada]  [Greet me]
Hello, Ada!
Empty name: Please enter your first name.

WHAT THE CODE DOES
const and =: Create a binding to a value; the binding is not reassigned here.
document.querySelector and #: Find an element by its id in the DOM, the browser representation of HTML.
addEventListener, click and function: Run the enclosed instructions when the button is clicked.
value and trim(): Read field text and remove outer whitespace.
if, === and return: Test strict equality with empty text and stop early if it is missing.
textContent and +: Set text safely and join strings; typed HTML is not executed.
HTML label, input, button, p and aria-live: Collect a name, trigger an action and announce changing text politely; main and h1 identify the page.

TRY IT
Change the greeting wording. Try a name containing <b> and observe literal text.

CHECK
Ada produces Hello, Ada!.
Spaces only produce the missing-name message.