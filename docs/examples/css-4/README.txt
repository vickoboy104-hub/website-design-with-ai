CSS practical 4: A responsive course card grid

Display training options in one column on a phone and three on a wide screen.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Weekend classes
Wide: Sewing | Baking | Web design
Narrow: Sewing
               Baking
               Web design

WHAT THE CODE DOES
display: grid and gap: Create a grid with spacing between cells.
@media and min-width: Apply the enclosed rule when the viewport is at least 700 CSS pixels wide.
grid-template-columns: Define the columns.
repeat(3, 1fr): Create three equal fractional columns.
body and article rules: Set type and breathing room; give each card a fill.
HTML main, h1, div, article, h2 and p: Name the page, group the layout and describe each course; .courses selects the div.

TRY IT
Add a fourth course. Observe the second row at wide sizes.

CHECK
Below 700px: one column.
At 700px or wider: three columns.