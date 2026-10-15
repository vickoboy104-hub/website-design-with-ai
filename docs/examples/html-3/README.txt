HTML practical 3: An event information page

Make an event page with a working internal link and meaningful image text.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Community Reading Day
See event details
[Three-book illustration]
Bring a book to share.
Event details
20 March 2027 • Community Hall

WHAT THE CODE DOES
header, main and section: Group introductory, main and related section content.
h1, h2 and p: Supply the visible heading hierarchy and paragraph.
a and href="#details": Link to the element whose id is details; a short page may barely scroll.
figure and figcaption: Keep an illustration and its caption together.
img, src and alt: Load an image file and provide equivalent useful text.
width and height: Reserve the image dimensions; CSS can later make it responsive.
time and datetime: Show a human-readable date with a machine-readable value.
id: Identifies this section uniquely on the page.

TRY IT
Change the event and date in both visible text and datetime. Check that they agree.

CHECK
The image appears.
The link changes the URL fragment to #details.