CSS practical 3: A flexible navigation bar

Arrange a studio name and navigation without fixed screen widths.

HOW TO RUN
Open index.html in Edge or Chrome. For VS Code practice, right-click index.html → Open with Live Server.

EXPECTED RESULT
Thread Studio     Services   Contact
Tailoring services
Practice contact: hello@example.com
Narrow screen: links wrap
Tab: a visible outline appears

WHAT THE CODE DOES
.bar, nav and comma: Apply the same rule to two selectors.
display: flex: Lay out direct children along an axis.
gap and flex-wrap: Add space and allow wrapping.
justify-content and align-items: Distribute items along the main axis and align them across it.
:hover and :focus-visible: Style pointer hover and visible keyboard focus.
outline, padding, color and background: Provide clear focus, space and colour cues.
HTML header, strong, nav, main, h1, p and a: Build a named studio header, navigation and two link targets; id matches each fragment.

TRY IT
Add a third navigation link and matching section id.

CHECK
Links wrap rather than overflow.
Both links work using Tab then Enter.