CSS practical 5: A readable enquiry form

Style labels and controls without changing their behaviour.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Ask about a class
First name
[                         ]
Your question
[                         ]
[Try the form]

WHAT THE CODE DOES
:root, --brand and var(): Define and reuse a custom colour property.
box-sizing, width and max-width: Keep controls within the form width including their padding.
display: block and margin-top: Put each label on its own line and separate fields.
font: inherit: Use the surrounding font in controls.
padding, color, background and border: Give comfortable controls and a distinct button.
:focus-visible and outline: Show which control the keyboard is using.
HTML form, label, input, textarea and button: Use the same field-and-label rules from HTML 4; the default button type in a form is submit.

TRY IT
Change --brand to #166649. Test keyboard focus and empty submission again.

CHECK
Labels are above their fields.
Controls fit a narrow screen.