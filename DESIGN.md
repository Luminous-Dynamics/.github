# 🎨 Design Standards

> "Design is how consciousness expresses itself through technology. Every pixel, every interaction, every moment is an opportunity to serve awareness."

This document defines design principles, standards, and practices for all user-facing work at Luminous Dynamics.

---

## 🎯 Design Philosophy

### Consciousness-First Design

**Design that serves awareness, not exploits attention:**

1. **Clarity Over Cleverness**
   - Users should immediately understand what to do
   - No hidden features or confusing patterns
   - Transparent about what's happening and why

2. **Intention Over Engagement**
   - Design for user goals, not platform metrics
   - No dark patterns or manipulation
   - Users should feel empowered, not hooked

3. **Calm Over Excitement**
   - Information when needed, silence otherwise
   - No unnecessary notifications or interruptions
   - Respect for user's attention and time

4. **Accessibility as Foundation**
   - Universal design from the start
   - Serve all bodies, all minds, all contexts
   - See [ACCESSIBILITY.md](./ACCESSIBILITY.md)

5. **Beauty in Service**
   - Aesthetics that support function
   - Delight emerges from clarity
   - Less is more (remove, don't add)

### Design as Care

Every design decision is an act of care:
- **Care for users**: Their time, attention, and goals
- **Care for contributors**: Clear patterns, documented decisions
- **Care for planet**: Efficient rendering, sustainable practices
- **Care for future**: Maintainable, evolvable systems

---

## 🧭 Core Design Principles

### 1. Clarity

**Users should never be confused.**

✅ **Do:**
```
Clear button: [Create New Federation]
Clear label: "Federation Name" with helper text: "A memorable name for your research group"
Clear feedback: "Federation created successfully. 3 participants joined."
```

❌ **Don't:**
```
Vague button: [Go]
No label: [_______ input field]
Silent success: [Form submits, page refreshes, no confirmation]
```

**Checklist:**
- [ ] Every action has a clear label
- [ ] Every form field has a label (not just placeholder)
- [ ] Every outcome has explicit feedback
- [ ] Help text explains non-obvious concepts

### 2. Consistency

**Similar things should work similarly.**

✅ **Do:**
- Primary action always blue, always on right
- Dangerous actions always red, always require confirmation
- Icons consistent across application (same icon = same meaning)

❌ **Don't:**
- Sometimes "Save" on left, sometimes on right
- Delete button red in one place, gray in another
- Same icon meaning different things in different contexts

**Checklist:**
- [ ] Design system components used throughout
- [ ] Patterns documented and reused
- [ ] New patterns only when existing ones don't fit

### 3. Feedback

**Users should always know what's happening.**

**States to Design:**
- **Idle**: Default state
- **Hover/Focus**: Interactive feedback
- **Active**: Currently interacting
- **Loading**: Waiting for response
- **Success**: Action completed successfully
- **Error**: Something went wrong
- **Disabled**: Temporarily unavailable

✅ **Good Feedback:**
```
[Button clicked]
→ Button shows spinner: "Creating federation..."
→ 2 seconds later: "✓ Federation created successfully"
→ Auto-dismiss after 5 seconds (or user can dismiss)
```

❌ **Bad Feedback:**
```
[Button clicked]
→ Nothing visible happens
→ Page eventually changes
→ User unsure if their action worked
```

### 4. Forgiveness

**Mistakes should be fixable.**

✅ **Do:**
- Undo/redo where appropriate
- Confirmation before destructive actions
- Auto-save drafts
- Restore from trash (don't immediately delete)

❌ **Don't:**
- Immediate permanent deletion
- No way to recover from mistakes
- Punish users for misclicks

**Confirmation Pattern:**
```
[Delete Federation button clicked]

Modal appears:
"Delete 'Climate Research' federation?"

This will permanently delete:
- 47 participants
- 3 months of training data
- All associated models

This action cannot be undone.

[Cancel]  [Delete Federation]
           ^^^^^^ Red, requires typing federation name to enable
```

### 5. Progressive Disclosure

**Show what's needed now, reveal complexity gradually.**

✅ **Good Progression:**
```
Basic view:
━━━━━━━━━━━━━━━━━━━━━━━
Federation: Climate Research
Participants: 47
Status: Active
[View Details]

Advanced view (after clicking):
━━━━━━━━━━━━━━━━━━━━━━━
Trust Layer: MATL/0TML
Byzantine Threshold: 0.3
Privacy Mode: Local-only
Created: 2025-01-10
Last Active: 2 minutes ago
[Advanced Settings]
```

❌ **Information Overload:**
```
All fields visible immediately:
- 20 configuration options
- Technical details user doesn't understand
- Overwhelmed on first view
```

---

## 🎨 Visual Design Standards

### Color Palette

**Primary Colors:**
```
Primary (Actions):    #0066CC (Blue)
Success:              #00A86B (Green)
Warning:              #FFB020 (Orange)
Error:                #E63946 (Red)
```

**Neutrals:**
```
Text Primary:         #1A1A1A (Near Black)
Text Secondary:       #6B6B6B (Gray)
Background:           #FFFFFF (White)
Background Alt:       #F5F5F5 (Light Gray)
Border:               #E0E0E0 (Medium Gray)
```

**Consciousness Colors (Mycelix, Terra Atlas):**
```
Trust:                #4ECDC4 (Teal)
Energy:               #FFE66D (Yellow)
Connection:           #A8DADC (Light Blue)
Growth:               #2A9D8F (Sea Green)
```

**Requirements:**
- All colors meet WCAG 2.1 AA contrast ratios
- Test combinations with contrast checker
- Provide dark mode alternatives
- Never use color alone to convey information

### Typography

**Font Stack:**
```css
/* Primary (body text) */
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto",
             "Helvetica Neue", Arial, sans-serif;

/* Monospace (code) */
font-family: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono",
             Consolas, monospace;
```

**Type Scale:**
```
H1: 32px / 2rem   - Page titles
H2: 24px / 1.5rem - Section headings
H3: 20px / 1.25rem - Subsection headings
H4: 18px / 1.125rem - Minor headings
Body: 16px / 1rem - Default text
Small: 14px / 0.875rem - Supporting text
Tiny: 12px / 0.75rem - Labels (use sparingly)
```

**Line Height:**
```
Headings: 1.2
Body: 1.6
Small: 1.4
```

**Requirements:**
- Minimum 16px body text (never smaller)
- Line length 50-75 characters for readability
- Sufficient line height for readability

### Spacing

**8px Grid System:**
```
Base unit: 8px

Spacing scale:
xs:   4px  (0.25rem) - Tight spacing
sm:   8px  (0.5rem)  - Small gaps
md:   16px (1rem)    - Default spacing
lg:   24px (1.5rem)  - Section spacing
xl:   32px (2rem)    - Major sections
2xl:  48px (3rem)    - Page sections
3xl:  64px (4rem)    - Page margins
```

**Usage:**
- Padding/margin in multiples of 8px
- Occasional 4px for tight layouts
- Never odd numbers (15px, 23px, etc.)

### Iconography

**Icon System:**
- Use consistent icon set (e.g., Heroicons, Feather)
- Regular weight: 24px × 24px
- Small: 16px × 16px
- Large: 32px × 32px

**Requirements:**
- Icons always paired with text labels (except universally understood)
- Consistent meaning across application
- Accessible (see [ACCESSIBILITY.md](./ACCESSIBILITY.md))

---

## ⚙️ Interaction Design

### Button Design

**Primary Button:**
```
Style: Blue background, white text, subtle shadow
Use: Main action on page (one per view)
Example: "Create Federation", "Start Training", "Save Changes"
```

**Secondary Button:**
```
Style: White background, blue border, blue text
Use: Alternative actions
Example: "Cancel", "View Details", "Learn More"
```

**Danger Button:**
```
Style: Red background, white text
Use: Destructive actions (requires confirmation)
Example: "Delete Federation", "Remove Participant"
```

**States:**
- Default
- Hover (slight darkening)
- Active (pressed state)
- Loading (spinner + "Loading..." text)
- Disabled (gray, reduced opacity, cursor: not-allowed)

### Form Design

**Best Practices:**

1. **Clear Labels**
```html
✅ Good:
<label for="federation-name">Federation Name</label>
<input
  id="federation-name"
  type="text"
  placeholder="e.g., Climate Research Network"
  aria-describedby="name-help"
/>
<span id="name-help">A memorable name for your research group</span>

❌ Bad:
<input type="text" placeholder="Federation Name" />
```

2. **Validation**
- Validate on blur (not every keystroke)
- Show errors clearly with red text and icon
- Explain how to fix ("Name must be 3-50 characters")
- Disable submit until form is valid

3. **Required Fields**
```html
<label for="name">
  Federation Name
  <span class="required" aria-label="required">*</span>
</label>
```

4. **Grouping**
- Related fields visually grouped
- Use fieldsets for radio/checkbox groups
- Progressive disclosure for advanced options

### Loading States

**For Fast Operations (<500ms):**
- No spinner (feels faster)
- Optimistic updates when possible

**For Medium Operations (500ms-3s):**
- Spinner on button
- Disable form to prevent double-submit

**For Long Operations (>3s):**
- Full-page spinner or skeleton loading
- Progress indicator if possible
- "This may take a minute..." message

**Example:**
```
Creating your federation...
[Progress bar showing 60%]

✓ Initializing trust layer
✓ Configuring privacy settings
→ Connecting participants (12/50)
  Setting up training environment

Estimated time remaining: 30 seconds
```

### Error Handling

**Hierarchy of Error Communication:**

1. **Inline (Field-Level)**
```
[Federation Name input field outlined in red]
⚠ Name must be at least 3 characters
```

2. **Form-Level**
```
⚠ Please fix 3 errors before submitting:
  • Federation name is too short
  • Trust threshold must be between 0 and 1
  • At least one participant required
```

3. **Toast/Alert (System-Level)**
```
❌ Federation creation failed
Network error: Could not connect to server
[Retry] [Contact Support]
```

**Error Message Guidelines:**
- Explain what went wrong (not just "Error")
- Suggest how to fix it
- Provide path forward (retry, contact support, documentation)
- Never blame the user ("You entered invalid data")
- Take responsibility ("We couldn't process this request")

---

## 📱 Responsive Design

### Breakpoints

```css
/* Mobile first approach */
Base:        0px    /* Mobile (< 640px) */
sm:        640px    /* Small tablet */
md:        768px    /* Tablet */
lg:       1024px    /* Desktop */
xl:       1280px    /* Large desktop */
2xl:      1536px    /* Extra large */
```

### Mobile Considerations

**Touch Targets:**
- Minimum 44px × 44px (preferably 48px)
- Adequate spacing between touch targets
- Large enough to tap with thumb

**Navigation:**
- Hamburger menu for complex navigation
- Bottom navigation for key actions (easier to reach)
- Avoid hover-dependent interactions

**Content:**
- Single column layout on mobile
- Images scale to container
- Tables convert to cards or scrollable
- Forms stack vertically

### Desktop Considerations

**Layout:**
- Multi-column layouts
- Sidebar navigation
- Hover states for additional info
- Keyboard shortcuts

**Density:**
- More information visible
- Tighter spacing acceptable
- Multi-step processes visible at once

---

## 🧪 Design Process

### 1. Research & Discovery

**Understand the Problem:**
- What are users trying to accomplish?
- What pain points exist in current flow?
- What are the constraints (technical, time, resources)?

**Methods:**
- User interviews (talk to actual users)
- Analytics review (what are users doing now?)
- Competitive analysis (how do others solve this?)
- Stakeholder input (business/technical requirements)

### 2. Ideation & Sketching

**Low-Fidelity Exploration:**
- Paper sketches or wireframes
- Multiple directions explored
- Focus on structure and flow, not visuals
- Collaborate with engineers (feasibility check)

**Key Questions:**
- What's the primary user goal?
- What's the critical path to accomplish it?
- What can we remove/simplify?

### 3. Prototyping

**Interactive Mockups:**
- Figma, Sketch, or code prototypes
- High enough fidelity to test with users
- Interactive (buttons work, flows connect)
- Not final visuals (speeds iteration)

### 4. User Testing

**Test with Real Users:**
- 5 users often enough to find major issues
- Give tasks, don't lead ("Create a new federation")
- Observe, don't explain
- Ask "what are you thinking?" not "do you like this?"

**Red Flags:**
- Users confused about what to do
- Users missing critical information
- Users making mistakes repeatedly
- Users expressing frustration

### 5. Refinement

**Iterate Based on Feedback:**
- Fix major issues first
- Refine visuals (color, typography, spacing)
- Polish interactions (transitions, feedback)
- Accessibility review (see [ACCESSIBILITY.md](./ACCESSIBILITY.md))

### 6. Implementation

**Collaborate with Engineers:**
- Provide detailed specs (spacing, colors, states)
- Review implementation (does it match design?)
- Fine-tune in browser (design != implementation)
- Test on real devices

### 7. Measurement

**After Launch:**
- Monitor analytics (are users succeeding?)
- Collect feedback (surveys, support tickets)
- Observe behavior (heatmaps, session recordings)
- Iterate continuously

---

## ✅ Design Review Checklist

### Before Sharing Design

- [ ] **User goal clear**: Can explain what user is trying to do
- [ ] **Primary action obvious**: Most important action stands out
- [ ] **All states designed**: Idle, hover, active, loading, error, success, disabled
- [ ] **Responsive**: Mobile and desktop layouts considered
- [ ] **Accessible**: Contrast ratios checked, keyboard navigation works
- [ ] **Consistent**: Uses existing patterns where appropriate
- [ ] **Copy written**: Not lorem ipsum (real content reveals issues)

### During Design Review

**Reviewers Ask:**
- What problem does this solve?
- How does this align with consciousness-first principles?
- Is this clear to someone unfamiliar with the context?
- What happens when things go wrong?
- How does this work on mobile?
- Is this accessible to screen readers?
- What's the performance impact?

**Designers Provide:**
- Context and goals
- User research insights
- Alternatives considered
- Prototype or interactive mockup
- Open questions seeking feedback

### After Implementation

- [ ] **Matches design**: Implemented as designed (or intentional changes documented)
- [ ] **Tested on devices**: Works on target browsers and screen sizes
- [ ] **Accessibility verified**: Screen reader tested, keyboard navigation works
- [ ] **Performance acceptable**: Loads quickly, animations smooth
- [ ] **Ready for users**: Monitoring in place to catch issues

---

## 🛠️ Design Tools & Resources

### Recommended Tools

**Design:**
- **Figma** (primary): Collaborative interface design
- **Excalidraw**: Quick wireframes and diagrams
- **Lucidchart**: Flow diagrams and user journeys

**Prototyping:**
- **Figma prototypes**: Interactive flows
- **CodeSandbox**: Quick code prototypes
- **Storybook**: Component library and states

**Testing:**
- **Maze**: Remote usability testing
- **Hotjar**: Heatmaps and session recordings
- **UserTesting**: Moderated user tests

**Accessibility:**
- **axe DevTools**: Automated accessibility testing
- **Contrast checker**: WCAG compliance
- **Screen readers**: NVDA (Windows), VoiceOver (Mac)

### Design System

**Component Library:**
- Maintained in Figma and code (Storybook)
- All states documented
- Usage guidelines for each component
- Accessibility notes

**Living Document:**
- This guide evolves based on learnings
- Suggest improvements via PR
- Discuss in #design Discord channel

---

## 💚 Consciousness-First UX Patterns

### Avoid Dark Patterns

❌ **Never:**
- **Confirmshaming**: "No thanks, I don't want to improve my research" (manipulative language)
- **Forced continuity**: Auto-renewing without clear notice
- **Hidden costs**: Fees revealed only at final step
- **Bait and switch**: Advertising one thing, delivering another
- **Trick questions**: Confusing language to get consent
- **Roach motel**: Easy to get in, hard to get out

✅ **Instead:**
- **Clear language**: "Continue without creating account"
- **Transparent renewal**: "Your trial ends in 3 days. Cancel anytime."
- **Upfront costs**: All fees visible from the start
- **Honest marketing**: Deliver what you promise
- **Plain language**: Clear yes/no questions
- **Easy exit**: Deletion and data export straightforward

### Respect Attention

**Notifications:**
- Default: off (users opt-in)
- User controls frequency and types
- Critical only (security, system status)
- Never for engagement ("You haven't visited in a while!")

**Interruptions:**
- No modals unless necessary
- Autoplaying media: never
- Dismissible messages
- Respect "do not disturb" modes

### Honor Agency

**User Control:**
- Users can undo, edit, delete their data
- Clear data export functionality
- Account deletion actually deletes (not just hides)
- No holding data hostage

**Transparency:**
- What data is collected (and why)
- How algorithms make decisions
- Where data is stored
- Who has access

---

## 📚 Related Resources

- **[ACCESSIBILITY.md](./ACCESSIBILITY.md)** - Accessibility standards and inclusive design
- **[STYLE_GUIDE.md](./STYLE_GUIDE.md)** - Documentation writing standards
- **[PERFORMANCE.md](./PERFORMANCE.md)** - Performance budgets and optimization
- **[CODE_REVIEW.md](./CODE_REVIEW.md)** - Review process (includes design review)

---

## 💬 Questions About Design?

- **Design feedback**: #design Discord channel
- **Accessibility questions**: See [ACCESSIBILITY.md](./ACCESSIBILITY.md)
- **Suggest improvements**: Open PR on this document
- **Design system**: Figma library (link in Discord)

---

**Last Updated**: 2025-01-14
**Maintained by**: Design Working Group

---

> "Every interface is an opportunity to serve users with clarity, respect their attention, and honor their agency. Design with consciousness, ship with care." 💚
