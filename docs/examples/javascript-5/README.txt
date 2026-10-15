JavaScript practical 5: A catalogue search page

Filter visible services as the visitor types.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Find a class
Search classes [web]
• Web design
Search [zzz]: No matching class.

WHAT THE CODE DOES
array, const and selectors: Store names and locate the search field and result list.
function showClasses and its final call: Define the update routine and run it once for the initial full list.
trim and toLowerCase: Normalise the query; normalise each name too.
filter, callback, return and includes: Keep names containing the query and return a new array.
textContent = empty string: Clear old results before creating the next set.
for...of, createElement and append: Render each match as a list item.
length, === and if: Show useful feedback when there are zero matches.
input event and HTML type="search": Update while the visitor types; label and aria-live explain the field and changing results.

TRY IT
Add Photography to the array. Search with upper-case letters and verify it still works.

CHECK
Empty search shows all three.
web shows only Web design.
zzz shows the empty-result message.