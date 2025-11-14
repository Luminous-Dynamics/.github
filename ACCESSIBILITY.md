# ♿ Accessibility Standards

> "Technology that serves only some consciousness is technology that has failed its purpose. Accessibility is not an add-on—it is foundational."

This document defines accessibility standards across all Luminous Dynamics projects, ensuring our technology serves everyone.

---

## 🎯 Accessibility Philosophy

### Core Principles

1. **Universal Design**
   - Build for everyone from the start, not retrofit later
   - Accessibility features benefit all users, not just those with disabilities
   - Design for diversity of abilities, contexts, and technologies

2. **Nothing About Us Without Us**
   - Include people with disabilities in design and testing
   - Listen to lived experience over assumptions
   - Pay accessibility consultants and testers fairly

3. **Progressive Enhancement**
   - Core functionality works for everyone
   - Enhanced features layer on top
   - Graceful degradation when technologies aren't available

4. **Continuous Improvement**
   - Accessibility is never "done"
   - Regular audits and user feedback
   - Fix issues promptly when discovered

### Why Accessibility Matters

**Ethical Imperative:**
- Technology should empower, not exclude
- Disability rights are human rights
- Our values demand radical inclusion

**Legal Compliance:**
- ADA (Americans with Disabilities Act)
- Section 508 (US federal accessibility)
- WCAG 2.1 (Web Content Accessibility Guidelines)
- European Accessibility Act

**Better for Everyone:**
- Captions help in noisy environments
- Keyboard navigation speeds up power users
- Clear language aids non-native speakers
- High contrast helps in bright sunlight

**Broader Reach:**
- 15% of global population has some form of disability
- Aging populations experience changing abilities
- Situational disabilities (broken arm, bright sun, loud environment)

---

## 💻 Code Accessibility

### Readable, Understandable Code

**Principle:** Code is read far more than it's written. Make it accessible to diverse minds and skill levels.

**Best Practices:**

1. **Clear Naming**
   ```python
   # ✅ Good - Descriptive and clear
   def calculate_byzantine_resistance_score(participant_trust_history):
       """Calculate resistance to Byzantine attacks based on participant history."""
       pass

   # ❌ Bad - Cryptic abbreviations
   def calc_bzr(pth):
       pass
   ```

2. **Self-Documenting Code**
   ```javascript
   // ✅ Good - Intent is clear from code structure
   const activeParticipants = allParticipants.filter(p => p.isActive);
   const byzantineResistanceThreshold = activeParticipants.length * 0.3;

   // ❌ Bad - Requires comment to understand
   const x = ps.filter(p => p.a);  // Get active participants
   const t = x.length * 0.3;  // Byzantine threshold
   ```

3. **Consistent Patterns**
   - Use established patterns within the project
   - Follow language conventions and idioms
   - Document deviations from patterns with reasoning

4. **Appropriate Abstraction**
   - Functions do one thing well
   - Classes have clear, focused responsibilities
   - Avoid over-engineering (YAGNI - You Ain't Gonna Need It)

### API Accessibility

**Principle:** APIs are user interfaces for developers. Make them intuitive, forgiving, and well-documented.

**Best Practices:**

1. **Intuitive Design**
   ```python
   # ✅ Good - Clear, expected API
   federation = Federation(name="health-research")
   federation.add_participant(participant_id="hospital-1")
   federation.start_training(model=my_model, epochs=10)

   # ❌ Bad - Unclear, unexpected API
   f = Fed()
   f.set("name", "health-research")
   f.p_add("hospital-1")
   f.go(my_model, 10)
   ```

2. **Helpful Error Messages**
   ```python
   # ✅ Good - Actionable error message
   raise ValueError(
       f"Byzantine threshold must be between 0 and 1. Got {threshold}. "
       f"This represents the maximum fraction of malicious participants the "
       f"system can tolerate. See docs: {DOCS_URL}/byzantine-tolerance"
   )

   # ❌ Bad - Cryptic error
   raise ValueError("Invalid threshold")
   ```

3. **Type Hints and Documentation**
   ```python
   from typing import List, Optional

   def create_federation(
       name: str,
       participants: List[str],
       byzantine_threshold: float = 0.3,
       privacy_mode: str = "local-only"
   ) -> Federation:
       """
       Create a new federated learning network.

       Args:
           name: Human-readable federation identifier
           participants: List of participant IDs to include
           byzantine_threshold: Fraction of malicious nodes tolerable (0-1).
               Default 0.3 means up to 30% of nodes can be malicious.
           privacy_mode: Data handling policy. Options:
               - "local-only": Data never leaves participant devices (default)
               - "encrypted-shared": Data shared with encryption

       Returns:
           Configured Federation instance ready for training

       Raises:
           ValueError: If byzantine_threshold not in range [0, 1]
           NetworkError: If unable to reach initial participants

       Example:
           >>> fed = create_federation(
           ...     name="healthcare",
           ...     participants=["hospital-1", "hospital-2"],
           ...     byzantine_threshold=0.2
           ... )
       """
   ```

4. **Sensible Defaults**
   - Most common use case works with minimal configuration
   - Defaults are safe and privacy-preserving
   - Advanced options available for power users

### Code Comments

**When to Comment:**
- **Why**, not *what* (code shows *what*, comments explain *why*)
- Complex algorithms that aren't immediately obvious
- Workarounds for bugs or limitations in dependencies
- TODOs with context and issue numbers

**When NOT to Comment:**
- Restating what code obviously does
- Commented-out code (use version control instead)
- Obsolete comments that don't match current code

**Examples:**

```python
# ✅ Good - Explains non-obvious reasoning
# Use exponential backoff instead of fixed retry to avoid thundering herd
# problem when many participants reconnect simultaneously after network partition
retry_delay = base_delay * (2 ** attempt_number)

# ❌ Bad - States the obvious
# Multiply base delay by 2 to the power of attempt number
retry_delay = base_delay * (2 ** attempt_number)
```

---

## 📖 Documentation Accessibility

### Writing for Screen Readers

**Best Practices:**

1. **Semantic HTML in Markdown**
   ```markdown
   ✅ Good - Proper heading hierarchy
   # Main Document Title
   ## Major Section
   ### Subsection

   ❌ Bad - Visual-only hierarchy
   # Main Document Title
   # Major Section (visually styled smaller)
   # Subsection (visually styled even smaller)
   ```

2. **Descriptive Link Text**
   ```markdown
   ✅ Good
   See the [installation guide](./install.md) for setup instructions.

   ❌ Bad
   For setup instructions, click [here](./install.md).
   ```

3. **Alt Text for Images**
   ```markdown
   ✅ Good - Descriptive alt text
   ![Architecture diagram showing three layers: Trust Layer (MATL/0TML) at bottom,
   Coordination Layer (Holochain) in middle, and Application Layer (Mycelix API)
   at top, with arrows showing data flow between layers](./diagrams/architecture.png)

   ❌ Bad - Missing or unhelpful alt text
   ![diagram](./diagrams/architecture.png)
   ```

4. **Table Headers**
   ```markdown
   ✅ Good - Clear headers
   | Feature | Mycelix | Traditional ML |
   |---------|---------|----------------|
   | Privacy | Local-only | Centralized |

   ❌ Bad - No headers
   | Mycelix | Local-only |
   | Traditional ML | Centralized |
   ```

### Clear, Simple Language

**Principle:** Accessible writing serves everyone—people with cognitive disabilities, non-native speakers, newcomers to the field.

**Best Practices:**

1. **Short Sentences**
   - Aim for 15-20 words per sentence
   - One idea per sentence
   - Break up long sentences with periods or lists

2. **Common Words**
   ```markdown
   ✅ Good
   The system checks if participants are trustworthy.

   ❌ Unnecessarily Complex
   The system adjudicates participant trustworthiness via heuristic evaluation.
   ```

3. **Active Voice**
   ```markdown
   ✅ Good - Active voice, clear actor
   The trust layer validates each participant's contribution.

   ❌ Bad - Passive voice, unclear actor
   Each participant's contribution is validated.
   ```

4. **Define Technical Terms**
   - Link to [GLOSSARY.md](./GLOSSARY.md) on first use
   - Provide brief definition inline when appropriate
   - Don't assume prior knowledge

5. **Logical Structure**
   - Use headings to organize content
   - Lists for related items
   - Tables for comparisons
   - Clear topic sentences in paragraphs

### Formatting for Readability

1. **White Space**
   - Short paragraphs (3-5 sentences max)
   - Blank lines between paragraphs
   - Don't wall-of-text

2. **Lists and Structure**
   ```markdown
   ✅ Good - Scannable list
   Prerequisites:
   - Node.js 18+
   - 4GB RAM
   - Git

   ❌ Bad - Dense paragraph
   Prerequisites: You'll need Node.js 18 or higher and at least 4GB of
   RAM and Git installed on your system.
   ```

3. **Code Formatting**
   - Always use syntax highlighting (specify language)
   - Keep code examples < 30 lines when possible
   - Add comments for non-obvious code
   - Show expected output

---

## 🎨 UI/UX Accessibility

### WCAG 2.1 Compliance

**Target:** WCAG 2.1 Level AA compliance (minimum)

**Key Requirements:**

#### 1. Perceivable

**Color Contrast:**
- **Text:** 4.5:1 contrast ratio (normal text), 3:1 (large text)
- **UI Components:** 3:1 contrast ratio for interactive elements
- **Tools:** [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

```css
/* ✅ Good - Meets 4.5:1 contrast */
.text {
  color: #1a1a1a;  /* Dark gray */
  background: #ffffff;  /* White */
}

/* ❌ Bad - Only 2.1:1 contrast */
.text {
  color: #999999;  /* Light gray */
  background: #ffffff;  /* White */
}
```

**Non-Color Information:**
```html
✅ Good - Error shown with icon + color + text
<div class="error" role="alert">
  <svg aria-hidden="true">❌</svg>
  <span>Error: Invalid federation name</span>
</div>

❌ Bad - Error shown only with red color
<div style="color: red;">Invalid federation name</div>
```

**Alternative Text:**
- All images have descriptive alt text
- Decorative images use `alt=""` or `aria-hidden="true"`
- Complex images (charts, diagrams) have extended descriptions

#### 2. Operable

**Keyboard Navigation:**
- All functionality available via keyboard
- Logical tab order
- Visible focus indicators
- No keyboard traps

```html
✅ Good - Keyboard accessible
<button onclick="startFederation()">Start Training</button>

✅ Also Good - Custom element with keyboard support
<div role="button" tabindex="0"
     onclick="startFederation()"
     onkeypress="handleKeyPress(event)">
  Start Training
</div>

❌ Bad - Not keyboard accessible
<div onclick="startFederation()">Start Training</div>
```

**Focus Indicators:**
```css
/* ✅ Good - Clear focus indicator */
button:focus {
  outline: 3px solid #0066cc;
  outline-offset: 2px;
}

/* ❌ Bad - Removed focus indicator */
button:focus {
  outline: none;
}
```

**Skip Links:**
```html
<!-- Allow keyboard users to skip repetitive navigation -->
<a href="#main-content" class="skip-link">
  Skip to main content
</a>
```

#### 3. Understandable

**Clear Labels:**
```html
✅ Good - Explicit label association
<label for="federation-name">Federation Name:</label>
<input id="federation-name" type="text" required />

❌ Bad - Placeholder as label
<input type="text" placeholder="Federation Name" />
```

**Error Identification:**
```html
✅ Good - Clear, specific error messages
<div role="alert" id="name-error">
  Error: Federation name must be 3-50 characters.
  Current length: 2 characters.
</div>
<input id="federation-name"
       aria-describedby="name-error"
       aria-invalid="true" />

❌ Bad - Generic error
<span>Invalid input</span>
```

**Consistent Navigation:**
- Navigation appears in same location on all pages
- Interactive elements behave consistently
- Terms used consistently throughout interface

#### 4. Robust

**Valid HTML:**
- No errors in HTML validation
- Proper nesting of elements
- Closed tags and quoted attributes

**ARIA When Needed:**
```html
<!-- Custom component needs ARIA to be accessible -->
<div role="progressbar"
     aria-valuenow="65"
     aria-valuemin="0"
     aria-valuemax="100"
     aria-label="Training progress">
  <div class="progress-bar" style="width: 65%"></div>
</div>
```

**Semantic HTML First:**
```html
✅ Good - Semantic HTML
<button>Submit</button>
<nav>...</nav>
<main>...</main>

❌ Bad - Div soup
<div class="button" onclick="...">Submit</div>
<div class="nav">...</div>
<div class="main">...</div>
```

---

## 🧪 Testing Accessibility

### Manual Testing Checklist

- [ ] **Keyboard Only:** Navigate entire interface with only keyboard (no mouse)
- [ ] **Screen Reader:** Test with NVDA (Windows), JAWS (Windows), or VoiceOver (Mac/iOS)
- [ ] **Zoom:** Test at 200% zoom (should not break layout or hide content)
- [ ] **Color Contrast:** Check all text and UI elements with contrast checker
- [ ] **Focus Indicators:** Verify all interactive elements have visible focus states
- [ ] **Error Messages:** Trigger validation errors, confirm they're clear and associated
- [ ] **Forms:** Complete all forms using only keyboard and screen reader
- [ ] **Alternative Text:** Verify all images have appropriate alt text

### Automated Testing Tools

**Browser Extensions:**
- [axe DevTools](https://www.deque.com/axe/devtools/) - Comprehensive accessibility testing
- [WAVE](https://wave.webaim.org/) - Visual feedback on accessibility issues
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Built into Chrome DevTools

**Command Line:**
```bash
# axe-core for automated testing
npm install --save-dev axe-core

# Pa11y for CI/CD integration
npm install --save-dev pa11y
pa11y https://localhost:3000
```

**Continuous Integration:**
```yaml
# .github/workflows/accessibility.yml
name: Accessibility Tests

on: [push, pull_request]

jobs:
  a11y:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Pa11y
        run: |
          npm install -g pa11y
          pa11y-ci --sitemap https://yoursite.com/sitemap.xml
```

### Screen Reader Testing

**Recommended Screen Readers:**
- **Windows:** NVDA (free, open source) or JAWS
- **macOS:** VoiceOver (built-in)
- **Linux:** Orca (free, open source)
- **iOS:** VoiceOver (built-in)
- **Android:** TalkBack (built-in)

**What to Test:**
1. Can you understand page structure from headings?
2. Are form fields clearly labeled?
3. Do error messages make sense in context?
4. Can you complete all tasks without seeing the screen?
5. Are dynamic updates announced appropriately?

**VoiceOver Quick Start (macOS):**
- Enable: Cmd + F5
- Navigate: Control + Option + Arrow Keys
- Web Rotor: Control + Option + U (browse headings, links, etc.)

**NVDA Quick Start (Windows):**
- Download: [nvaccess.org](https://www.nvaccess.org/)
- Start Reading: NVDA + Down Arrow
- Elements List: NVDA + F7 (browse headings, links, etc.)

---

## 📱 Project-Specific Guidelines

### Web Applications (Terra Atlas, Visualizers)

**Required:**
- WCAG 2.1 Level AA compliance
- Keyboard navigation for all features
- Screen reader tested on 2+ platforms
- Color contrast meets standards
- Responsive design (works at 200% zoom)
- Focus management for single-page apps

**Recommended:**
- WCAG 2.1 Level AAA where feasible
- Dark mode support (helps light sensitivity)
- Font size controls
- Reduced motion support (`prefers-reduced-motion`)

**Example: Reduced Motion:**
```css
/* Respect user's motion preferences */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Command Line Tools (Mycelix CLI, Deployment Scripts)

**Required:**
- Clear, descriptive command names
- Comprehensive help text (`--help`)
- Progress indicators for long operations
- Error messages that suggest solutions
- Examples in documentation

**Example: Good CLI Output:**
```bash
$ mycelix init my-federation

✓ Created federation directory: ./my-federation
✓ Initialized trust layer (MATL/0TML)
✓ Generated configuration: ./my-federation/config.yml

Next steps:
  1. cd my-federation
  2. Edit config.yml to customize settings
  3. Run: mycelix start

Documentation: https://docs.mycelix.org/getting-started
```

### APIs and Libraries

**Required:**
- Type hints (Python) or TypeScript definitions
- Comprehensive docstrings/JSDoc
- Example code in documentation
- Helpful error messages with solutions
- Semantic versioning (SemVer)

**Example: Helpful API Error:**
```python
class FederationError(Exception):
    """Raised when federation operations fail."""

    def __init__(self, message, suggestion=None, docs_url=None):
        self.message = message
        self.suggestion = suggestion
        self.docs_url = docs_url

        full_message = message
        if suggestion:
            full_message += f"\n\nSuggestion: {suggestion}"
        if docs_url:
            full_message += f"\n\nDocs: {docs_url}"

        super().__init__(full_message)

# Usage
raise FederationError(
    "Failed to connect to participant 'hospital-1'",
    suggestion="Check that the participant is online and the network is reachable",
    docs_url="https://docs.mycelix.org/troubleshooting/connectivity"
)
```

### Documentation Sites

**Required:**
- Readable at 200% zoom without horizontal scrolling
- Semantic HTML (proper heading hierarchy)
- Clear navigation with skip links
- Search functionality
- Mobile-responsive design
- Alt text for all images

**Recommended:**
- Dark mode option
- Font size controls
- Print-friendly styles
- Breadcrumb navigation
- Table of contents for long pages

---

## 🎓 Accessibility Resources

### Learning

**Foundational:**
- [WebAIM: Introduction to Web Accessibility](https://webaim.org/intro/)
- [W3C Web Accessibility Initiative (WAI)](https://www.w3.org/WAI/)
- [The A11Y Project](https://www.a11yproject.com/) - Community-driven accessibility resources

**WCAG Standards:**
- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [How to Meet WCAG 2 (Customizable Quick Reference)](https://www.w3.org/WAI/WCAG21/quickref/)

**Courses:**
- [Web Accessibility by Google (Udacity)](https://www.udacity.com/course/web-accessibility--ud891) - Free
- [Digital Accessibility Foundations (W3Cx)](https://www.edx.org/course/web-accessibility-introduction) - Free

### Testing Tools

- [axe DevTools](https://www.deque.com/axe/devtools/) - Browser extension for automated testing
- [WAVE](https://wave.webaim.org/) - Web accessibility evaluation tool
- [Color Contrast Analyzer](https://www.tpgi.com/color-contrast-checker/) - Desktop app for checking contrast
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Automated testing in Chrome
- [Pa11y](https://pa11y.org/) - Automated testing for CI/CD

### Design Resources

- [Inclusive Components](https://inclusive-components.design/) - Accessible component patterns
- [Accessible Color Palette Builder](https://toolness.github.io/accessible-color-matrix/)
- [Material Design Accessibility](https://material.io/design/usability/accessibility.html)

### Community

- [WebAIM Discussion List](https://webaim.org/discussion/)
- [A11y Slack Community](https://web-a11y.slack.com/)
- [#a11y on Twitter](https://twitter.com/hashtag/a11y)

---

## 🛠️ Implementing Accessibility

### For Developers

**Before You Code:**
1. Review [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
2. Check existing patterns in [Inclusive Components](https://inclusive-components.design/)
3. Plan keyboard navigation flow
4. Consider screen reader experience

**While You Code:**
1. Use semantic HTML elements
2. Add ARIA only when semantic HTML isn't enough
3. Test keyboard navigation frequently
4. Run automated tests (axe, Lighthouse)

**Before You Submit PR:**
1. Run full accessibility test suite
2. Manual keyboard navigation test
3. Screen reader test (at least one platform)
4. Color contrast verification
5. Zoom to 200% and verify layout

### For Designers

**Design Phase:**
1. Ensure color contrast meets 4.5:1 (text) and 3:1 (UI)
2. Design visible focus states for all interactive elements
3. Provide text alternatives for visual information
4. Consider keyboard-only navigation in user flows
5. Use standard UI patterns (don't reinvent controls)

**Deliverables:**
1. Color contrast ratios documented in design system
2. Focus state designs for all interactive elements
3. Alt text guidance for imagery
4. Keyboard interaction specifications
5. Error state designs with clear messaging

### For Content Creators

**Writing:**
1. Use clear, simple language (see [STYLE_GUIDE.md](./STYLE_GUIDE.md))
2. Organize with headings (H2, H3, not visual styling)
3. Write descriptive link text ("installation guide" not "click here")
4. Provide alt text for all images

**Formatting:**
1. Use lists for related items
2. Use tables only for tabular data (include headers)
3. Break up long paragraphs
4. Avoid walls of text

---

## ✅ Accessibility Review Checklist

### For Pull Requests

When reviewing PRs that touch UI, documentation, or APIs:

**Code:**
- [ ] Semantic HTML used appropriately
- [ ] ARIA attributes used correctly (or not needed)
- [ ] Keyboard navigation works for all interactive elements
- [ ] Focus indicators visible and clear
- [ ] Color is not the only means of conveying information

**Documentation:**
- [ ] Heading hierarchy is logical (no skipped levels)
- [ ] Links have descriptive text
- [ ] Images have alt text (or `alt=""` if decorative)
- [ ] Code examples have syntax highlighting
- [ ] Tables have headers

**Testing:**
- [ ] Automated tests pass (axe, Pa11y, Lighthouse)
- [ ] Manual keyboard test completed
- [ ] Screen reader tested (specify which: NVDA, VoiceOver, etc.)
- [ ] Zoom to 200% verified
- [ ] Color contrast checked

---

## 🚨 Reporting Accessibility Issues

### How to Report

**GitHub Issues:**
1. Use label: `accessibility`
2. Specify WCAG criterion if known (e.g., "WCAG 2.1.1 - Keyboard")
3. Describe barrier and affected users
4. Suggest solution if you have one

**Template:**
```markdown
**Accessibility Barrier:** [Brief description]

**WCAG Criterion:** [e.g., 2.4.7 Focus Visible]

**Affected Users:** [e.g., keyboard-only users, screen reader users]

**Steps to Reproduce:**
1.
2.
3.

**Expected Behavior:** [What should happen]

**Actual Behavior:** [What currently happens]

**Suggested Solution:** [If you have one]

**Assistive Technology:** [Screen reader, browser, OS if relevant]
```

### Priority Levels

**P0 - Critical (Fix within 1 week):**
- Cannot complete core functionality with assistive tech
- Violates legal requirements (ADA, Section 508)
- Affects large number of users

**P1 - High (Fix within 1 month):**
- Significant barrier to some users
- Workaround exists but is difficult
- WCAG Level A or AA violation

**P2 - Medium (Fix within 3 months):**
- Minor barrier with easy workaround
- WCAG Level AAA violation
- Enhancement for better experience

**P3 - Low (Fix when capacity allows):**
- Nice-to-have improvement
- Affects very small edge case
- Enhancement beyond WCAG requirements

---

## 💚 Accessibility as Practice

### It's a Journey

- **Start where you are** - Some accessibility is better than none
- **Learn continuously** - Disability experience teaches us daily
- **Fix issues promptly** - When barriers are discovered, prioritize them
- **Build it in from the start** - Far easier than retrofitting

### Disability Justice Lens

Accessibility is part of broader disability justice:
- **Leadership:** Center disabled people in decisions
- **Collective access:** We all have access needs, support each other
- **Sustainability:** Build for long-term use and maintenance
- **Commitment to cross-disability solidarity:** Not just one type of disability

### Our Commitment

At Luminous Dynamics, we commit to:
- WCAG 2.1 Level AA minimum across all projects
- Include people with disabilities in design and testing
- Fix accessibility issues with high priority
- Continuous learning and improvement
- Document and share what we learn

---

## 📚 Related Resources

- **[STYLE_GUIDE.md](./STYLE_GUIDE.md)** - Documentation writing standards
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - How to contribute code
- **[CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)** - Community standards
- **[INCLUSIVE.md](./INCLUSION.md)** - Broader inclusion practices (if exists)

---

## 💬 Questions?

- **GitHub Discussions:** [Accessibility category](https://github.com/orgs/Luminous-Dynamics/discussions)
- **Email:** accessibility@luminous-dynamics.org
- **Suggest improvements:** Open PR on this document

---

**Last Updated**: 2025-01-14
**Maintained by**: Accessibility Working Group

---

> "When we design for disability, we design for humanity. Everyone benefits from accessible technology." 💚
