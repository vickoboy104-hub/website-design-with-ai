HTML practical 4: A workshop registration form

Build correctly labelled fields and observe browser validation.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Register for a sewing workshop
First name  [Ada]
Email  [ada@example.com]
Your level  [Complete beginner]
[Try registration]
After submit: URL contains name=Ada

WHAT THE CODE DOES
main and h1: Identify the main content and form purpose.
form, action and method: Submit to index.html using GET; this demo only reloads with query values.
label and for: Connect a visible label to an input id.
input, id and name: Create a field, identify it and name the submitted value.
type="email" and required: Apply browser email-format and missing-value checks.
select and option: Offer a menu; value is the submitted choice.
textarea: Provides a multiline writing field.
button type="submit": Submits the enclosing form.

TRY IT
Add a labelled phone field using type="tel". Do not collect real personal information.

CHECK
Empty required fields are blocked.
A valid fictional entry appears in the URL, but is not stored.