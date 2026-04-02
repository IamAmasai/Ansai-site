# ANSAI

Brand & Design System Toolkit

*A precision specification for human-quality, LLM-assisted UI/UX design*

Version 1.0 · Confidential · Ansai Design System

---

## Preface

# How to Use This Toolkit with an LLM

This document is a precision design specification engineered to close
the gap between AI-generated and human-crafted interfaces. Paste the
relevant sections directly into your prompt. The more sections you
include, the closer the output will map to Ansai's visual language.

> *PROMPT TIP: Begin every LLM design prompt with: "You are a senior product designer working within the Ansai design system. Apply every specification in this document literally and without deviation. Do not invent new patterns — use only what is defined here."*

### Three-Layer Prompting Model

Layer 1 — Identity Layer: Paste Sections I and II (Brand Core +
Voice). This sets the emotional register and prevents generic, soulless
output.

Layer 2 — Visual Layer: Paste Sections III, IV, and V (Color, Type,
Spacing). This governs every pixel decision.

Layer 3 — Behavior Layer: Paste Sections VI and VII (Interaction +
Platform). This ensures the design feels alive, not static.

> *ANTI-AI-SLOP PRINCIPLE: If a generated design could have come from a generic Dribbble template, it has failed. Every Ansai screen must feel like it was authored by a specific human designer with a specific opinion.*

---

## Section I — Brand Core & Strategic Identity

Ansai is a tech-forward, premium ecosystem. Every design decision must
be traceable back to four founding pillars: Unified, Universal, Iconic,
and Conversational. If a design element does not serve at least one of
these pillars, it does not belong.

## Mission & Philosophy

Mission: To dismantle the "wall of knowledge" through simple,
bite-sized, and delightful user experiences. The mission is not
decoration — it is a filter. Any UI pattern that creates cognitive
overhead, forces the user to learn a new mental model, or obscures
information behind unnecessary steps directly contradicts Ansai's
reason for existing.

> *DESIGN PHILOSOPHY — LIQUID LOGIC: Software should behave like a living organism. It adapts in real-time to the user's environment, device state, and context. Rigidity is a design failure. Every layout, every type size, every color token must be built to respond.*

### Brand Personality: The Trusted Host

Ansai's personality is Professional yet approachable. Think of the
brand as a Trusted Host — the person who guides you through a complex
space with warmth, confidence, and zero condescension. When writing copy
for UI elements, error states, or onboarding flows, ask: "Would a
knowledgeable, kind person say this?" If not, rewrite it.

+———————————-+———————————–+
| **BRAND IS:**                    | **BRAND IS NOT:**                 |
|                                  |                                   |
| Confident without arrogance      | Corporate, stiff, or distant      |
|                                  |                                   |
| Warm without being casual        | Trendy slang or overfamiliar      |
|                                  |                                   |
| Direct without being blunt       | Cluttered with disclaimers        |
|                                  |                                   |
| Premium without exclusion        | Elitist or gatekeeping            |
+———————————-+———————————–+

### The Four Pillars — LLM Prompt Anchors

When prompting an LLM to design any Ansai screen, reference these
pillars explicitly in your prompt. They are not aspirational — they
are constraints.

> ——————– —————- —————————————- **PILLAR**           **DESIGN         **LLM PROMPT LANGUAGE** IMPLICATION** **Unified**          *Consistent      **"Use only the defined color tokens, tokens across    spacing scale, and type styles. Do not all surfaces*    introduce new values."** **Universal**        *Accessible on   **"The layout must work at 320px and any device, any  1440px. Every text element must pass condition*       APCA Lc 75+."** **Iconic**           *Instantly       **"Apply the Obsidian background, recognizable     Liquid Blue gradient for CTAs, and the visual           8pt grid without exception."** signature* **Conversational**   *Feels like a    **"Write all microcopy in second dialogue, not a  person. Use progressive disclosure — broadcast*       never dump all options on the user at once."** ——————– —————- —————————————-

---

## Section II — Voice, Tone & Microcopy

Microcopy is design. A button label, an error message, an empty state
— these are not afterthoughts. They are load-bearing elements of the
user experience. A pixel-perfect layout with clumsy copy feels like a
beautiful suit worn with dirty shoes.

## Voice Spectrum

Ansai's voice does not change — but the tone adjusts to context.
Think of it as a dial, not a switch.

+———————————-+———————————–+
| **ONBOARDING & CELEBRATION**     | **ERROR STATES & FRICTION**       |
|                                  |                                   |
| *Warm, slightly playful,         | *Calm, informative, never blaming |
| encouraging.*                    | the user.*                        |
|                                  |                                   |
| "You're in. Let's make this   | "Something went wrong on our     |
| work for you."                  | end. Try again or contact         |
|                                  | support."                        |
+———————————-+———————————–+

+———————————-+———————————–+
| **DATA-HEAVY / ANALYTICAL        | **DESTRUCTIVE ACTIONS**           |
| SCREENS**                        |                                   |
|                                  | *Serious, clear, respects the     |
| *Precise, efficient, zero        | weight of the moment.*            |
| fluff.*                          |                                   |
|                                  | "This will permanently delete    |
| "47 results · Sorted by         | your account and all data. This   |
| relevance"                      | cannot be undone."               |
+———————————-+———————————–+

## Microcopy Rules

These are non-negotiable. They apply to every word in the product:
buttons, tooltips, placeholders, confirmation dialogs, push
notifications, and email subjects.

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Write button labels as verb +    | Don't use ambiguous single       |
| noun: "Save Changes", "Add    | words: "OK", "Submit",        |
| Payment Method", "Export       | "Yes". They give no information |
| Report".                        | about what will happen.           |
+———————————-+———————————–+

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Empty states must include a      | Never leave an empty state blank  |
| heading, a single-sentence       | or with only a sad illustration.  |
| explanation, and one clear CTA:  | Silence is not design — it's   |
| "No saved items yet. Browse the | abandonment.                      |
| catalog to start building your   |                                   |
| list. \[Explore Now\]"          |                                   |
+———————————-+———————————–+

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Error messages must say what     | Never show raw error codes or     |
| happened AND what the user can   | developer messages to end users.  |
| do: "Your session expired.      | Never say "An error occurred"   |
| Please sign in again."          | with no next step.                |
+———————————-+———————————–+

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Placeholder text should give a   | Never use placeholder text to     |
| real example: "e.g.,            | replace a label. Placeholders     |
| hello@name.com" or "e.g.,      | disappear on focus — labels     |
| London, UK".                    | provide persistent context.       |
+———————————-+———————————–+

---

## Section III — The Ansai Palette: Color System

Ansai uses a Semantic Token System. Colors are never referenced by hex
code in design specs or in code — they are referenced by their role.
This ensures consistent meaning across light mode, dark mode,
high-contrast mode, and future themes.

> *LLM INSTRUCTION: Never hardcode hex values. Always reference colors by their semantic token name (e.g., ansai-bg-primary, ansai-action-gradient). This allows theme switching without redesigning every screen.*

## Primary Surfaces

+—–+—————+———————————————–+
|     | **Ansai       | The dominant background for all app screens   |
|     | Obsidian ·    | and dark-mode web surfaces. NOT pure black    |
|     | ansai         | — chosen specifically to prevent halation   |
|     | -bg-primary** | (light-bleed glow) on high-brightness OLED    |
|     |               | displays. Use for: main backgrounds, card     |
|     | **#0D1117**   | surfaces, modal backdrops.                    |
+—–+—————+———————————————–+

+—–+—————+———————————————–+
|     | **Deep Navy · | Secondary surface, used for layered cards,    |
|     | ansai-b       | drawers, and elevated panels. Provides depth  |
|     | g-secondary** | without introducing a competing color. Use    |
|     |               | for: bottom sheets, sidebar backgrounds,      |
|     | **#131B25**   | hover states on Obsidian surfaces.            |
+—–+—————+———————————————–+

+—–+—————+———————————————–+
|     | **Surface     | Tertiary surface for data cards and list      |
|     | Card ·        | items. Gives visual separation without high   |
|     | an            | contrast noise. Use for: list rows, data      |
|     | sai-bg-card** | tiles, feature cards.                         |
|     |               |                                               |
|     | **#1A2332**   |                                               |
+—–+—————+———————————————–+

## Action & Brand Gradient

The Liquid Blue-to-Cyan gradient is the single most recognizable Ansai
design element. It must be used sparingly and purposefully — its power
comes from restraint. When everything glows, nothing does.

+—–+—————+———————————————–+
|     | **Gradient    | Primary CTA gradient start (left/top). Use    |
|     | Start ·       | exclusively for Primary Action Buttons and    |
|     | ansai-        | Progress Indicators.                          |
|     | action-from** |                                               |
|     |               |                                               |
|     | **#D03660**   |                                               |
+—–+—————+———————————————–+

+—–+—————+———————————————–+
|     | **Gradient    | Primary CTA gradient end (right/bottom).      |
|     | End ·         | Applied as: background:                       |
|     | ansa          | linear-gradient(135deg, #D03660, #D73B53);    |
|     | i-action-to** |                                               |
|     |               |                                               |
|     | **#D73B53**   |                                               |
+—–+—————+———————————————–+

+—–+—————+———————————————–+
|     | **Liquid Cyan | Standalone accent for active states, links,   |
|     | ·             | highlights, and decorative dividers. Use at   |
|     | ansai-acc     | 60–80% opacity on dark surfaces for subtle   |
|     | ent-primary** | glow effects.                                 |
|     |               |                                               |
|     | **#4DCFEA**   |                                               |
+—–+—————+———————————————–+

## Text & Neutral Scale

+—–+—————+———————————————–+
|     | **White ·     | Primary text on all dark surfaces. Body copy, |
|     | ansai-t       | headings, button labels.                      |
|     | ext-primary** |                                               |
|     |               |                                               |
|     | **#FFFFFF**   |                                               |
+—–+—————+———————————————–+

+—–+—————+———————————————–+
|     | **Muted ·     | Secondary text: captions, metadata,           |
|     | ansai-tex     | placeholder labels, timestamps.               |
|     | t-secondary** |                                               |
|     |               |                                               |
|     | **#8B9BB4**   |                                               |
+—–+—————+———————————————–+

+—–+—————+———————————————–+
|     | **Disabled ·  | Disabled UI states, inactive tab labels.      |
|     | ansai-te      | Never use for content a user might need to    |
|     | xt-disabled** | read.                                         |
|     |               |                                               |
|     | **#4A5568**   |                                               |
+—–+—————+———————————————–+

## Semantic Feedback Colors

+—–+—————+———————————————–+
|     | **Success ·   | Confirmations, completed states, positive     |
|     | ansai-seman   | data trends.                                  |
|     | tic-success** |                                               |
|     |               |                                               |
|     | **#38A169**   |                                               |
+—–+—————+———————————————–+

+—–+—————+———————————————–+
|     | **Warning ·   | Alerts that need user attention but are not   |
|     | ansai-seman   | failures. Use sparingly.                      |
|     | tic-warning** |                                               |
|     |               |                                               |
|     | **#D69E2E**   |                                               |
+—–+—————+———————————————–+

+—–+—————+———————————————–+
|     | **Error ·     | Validation errors, destructive action         |
|     | ansai-sem     | confirmations. Never use for emphasis or      |
|     | antic-error** | decoration.                                   |
|     |               |                                               |
|     | **#E53E3E**   |                                               |
+—–+—————+———————————————–+

## Accessibility Standards

> *MANDATORY: All text must pass APCA (Advanced Perceptual Contrast Algorithm) standards. Use the APCA Lc score, not the outdated WCAG 2.x ratio. Target: Lc 75+ for body text, Lc 60+ for large headings (18pt+). In High-Contrast Solar Mode (triggered in bright ambient light), push all scores to Lc 90+.*

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Test every text/background       | Do not use WCAG 2.x contrast      |
| combination using the APCA       | ratios as the primary             |
| contrast calculator. White       | accessibility test. APCA is       |
| (#FFFFFF) on Obsidian (#0D1117)  | perceptually uniform and models   |
| achieves Lc \~106 — excellent. | real human vision — WCAG 2.x    |
| Muted blue (#8B9BB4) on Obsidian | systematically fails for          |
| achieves Lc \~58 — use only    | dark-mode interfaces and large    |
| for decorative or non-essential  | text.                             |
| text.                            |                                   |
+———————————-+———————————–+

---

## Section IV — Typography System

Typography is the primary vehicle for credibility. A poorly set type
hierarchy signals amateur craft before the user reads a single word.
Ansai type is precise, intentional, and never decorative for its own
sake.

### Primary Typeface: Ansai Flex

Ansai Flex is a variable font with multiple registered axes. Variable
fonts allow a single font file to handle the full range of weights,
widths, and optical sizes — eliminating the need for separate Bold,
Light, Condensed files. This directly reduces page load weight and
enables biometric adaptation.

> ——————— —————————— —————————- **PROPERTY**          **VALUE / TOKEN**              **USAGE / NOTE** **Font File**         **AnsaiFlex-Variable.woff2**   *Single variable font — no separate weight files* **Width Axis (wdth)** **85% for headlines**          *Condensed Impact rule — authority without consuming vertical space* **Optical Size        **Adaptive: 12–72**           *Expands counter-spaces as (opsz)**                                             user moves device away from face* **Weight Range**      **300–800**                   *Light to ExtraBold across one continuous axis* **Fallback Stack**    **system-ui, -apple-system**   *Never fall back to Arial or Helvetica — too neutral* ——————— —————————— —————————-

### Type Scale — The Hierarchy

Every type size has one job. Do not promote body text to heading size
for emphasis. Do not use heading styles for supporting copy. Use weight,
color, and spacing — not size — for emphasis within a scale level.

> ————- ———— ———— ———— ———————– **ROLE**      **SIZE       **WEIGHT**   **LINE       **USE CASE** RANGE**                   HEIGHT** **Display     32–72px     Bold / 800   1.1×         Hero areas, splash (H1)**                                               screens. Set wdth to 85%. **Heading     23–32px     SemiBold /   1.2×         Section titles, modal (H2)**                     600                       headers, card titles. **Heading     18–22px     Medium / 500 1.3×         Subsection labels, form (H3)**                                               group headers. **Body 1**    16–18px     Regular /    1.5×         Primary content. 400                       Minimum 17pt iOS / 18sp Android. **Body 2**    14–16px     Regular /    1.5×         Secondary content, 400                       descriptions, annotations. **Label**     12–14px     Medium / 500 1.4×         Buttons, tab labels, metadata. Slightly heavier for touch clarity. **Caption**   10–12px     Regular /    1.4×         Timestamps, legal text. 400                       Never use below 10px. ————- ———— ———— ———— ———————–

## Biometric Optical Sizing

Ansai implements Adaptive Optical Sizing via device sensor integration.
As a user holds the device further away (detected via front-facing
camera or gyroscope), the font's opsz axis increases, opening up
counter-spaces and increasing x-height for legibility without changing
the layout.

> *LLM INSTRUCTION: When designing screens, always specify font sizes using the full variable range, not a fixed point. Write: "Display heading: 48px (range 32–72, opsz auto)" not "Display heading: 48px". This signals to developers that the type is adaptive, not static.*

## Typographic Anti-Patterns

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Use weight and color for         | Never use italics for UI          |
| emphasis within a paragraph:     | emphasis. Never underline text    |
| "ansai-text-primary at Body 1   | that is not a hyperlink. Never    |
| Regular, with a specific term in | use all-caps for body copy longer |
| Medium weight and                | than 4 words.                     |
| ansai-accent-primary color."    |                                   |
+———————————-+———————————–+

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Set justified text only in       | Never justify (full-justify) body |
| multi-column print layouts. In   | text in digital UI. Irregular     |
| all digital interfaces, use      | word-spacing creates "rivers"   |
| left-align for body copy,        | of whitespace that disrupt        |
| center-align for display         | reading flow on variable-width    |
| headlines and CTAs only.         | screens.                          |
+———————————-+———————————–+

---

## Section V — Spatial Design: The 8pt Soft-Grid

Spatial design is invisible when done correctly. When done incorrectly,
it announces itself as tightness, crowding, or arbitrary placement.
Ansai's spatial system is built on a single, non-negotiable rule: every
dimension is a multiple of 8.

## The Grid System

> ——————— ——————— —————————- **PROPERTY**          **VALUE / TOKEN**     **USAGE / NOTE** **Base Unit**         **8px**               *The atomic unit. Every value traces back to this.* **Micro Spacing**     **4px**               *Exception only — used for internal component padding (e.g., icon-to-label gap).* **Component Padding** **16px / 24px**       *Standard inner padding for cards, inputs, and containers.* **Section Spacing**   **32px / 48px**       *Vertical separation between distinct UI sections.* **Screen Margin**     **16px (mobile) /     *Safe zone from screen edge 24px (tablet) / 32px+ to content.* (desktop)** **Column Gutter**     **16px**              *Horizontal gap between grid columns.* ——————— ——————— —————————-

## Soft-Grid vs. Hard-Grid

Ansai's grid is Soft, not Hard. A hard grid snaps elements to fixed
column positions. A soft grid defines the space between elements,
allowing fluid transitions on foldable displays, waterfall screens, and
unusual aspect ratios.

> *PRACTICAL RULE: Define spacing as gap between components, not margin from edge. This translates directly to modern CSS Flexbox and Grid implementations: use gap: 16px on containers, not margin-right on individual items. This prevents spacing collapse on wrapping layouts.*

## The Visual Tail Rule

Always ensure a partial element is visible at the bottom of the viewport
fold. This is the single most reliable signal to a user that more
content exists below, without resorting to explicit "scroll down"
arrows or instructions.

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Crop the last visible card or    | Never end a screen at a clean,    |
| text block at approximately 60%  | full element boundary. A perfect, |
| of its height at the fold. Test  | flush bottom edge signals to the  |
| at the exact screen heights of   | user that they have reached the   |
| the five most-used devices for   | end — even when they haven't.  |
| your audience.                   |                                   |
+———————————-+———————————–+

## Atomic Design Structure

Ansai follows the Atomic Design methodology. This is not optional — it
is the scaffolding that allows the design system to scale without
breaking. When prompting an LLM to create a new screen, specify which
atomic level you are designing at.

> ————– —————- —————————————— **LEVEL**      **EXAMPLE**      **LLM PROMPT INSTRUCTION** **Atom**       Button, Input,   "Design only the component itself. No Icon, Tag        surrounding context. Specify: default, hover, active, disabled, and error states." **Molecule**   Search bar,      "Combine defined atoms. Do not introduce Card, Form group new atoms — use only what exists in the Ansai library." **Organism**   Navigation bar,  "Compose molecules into a functional UI Feed section,    section. Ensure the 8pt grid is maintained Auth panel       at all component boundaries." **Template**   Screen wireframe "Lay out organisms into a full screen without real content. Focus on spatial rhythm, fold behavior, and thumb-zone accessibility." **Page**       Live screen with "Populate the template with real or content          representative content. Apply the Visual Tail Rule. Check the Three-Tap Rule." ————– —————- ——————————————

---

## Section VI — Interaction Design & Motion

A screen is not finished when it looks correct. A screen is finished
when it feels correct. Motion and haptics are not enhancement layers —
they are primary communication channels. They confirm actions, indicate
status, and signal causality between inputs and outcomes.

## The 50ms Feedback Rule

> *MANDATORY: Every user interaction — tap, swipe, toggle, long-press — must produce a visual or textual acknowledgment within 50 milliseconds. At 50ms, feedback feels instantaneous. At 100ms, users perceive a slight lag. At 200ms+, they question whether their action registered. 50ms is not a guideline. It is the contract.* ——————— ——————— —————————- **PROPERTY**          **VALUE / TOKEN**     **USAGE / NOTE** **Tap feedback**      **\< 50ms**           *Button state change (pressed → depressed visual)* **Toggle animation**  **150–200ms**        *State transition with spring easing* **Page transition**   **280–320ms**        *Spatial spring — origin to destination* **Loading skeleton**  **Immediate**         *Skeleton UI must appear before any network call completes* **Error display**     **\< 100ms after      *Inline error, not modal — failure**             never block the UI* **Success             **250ms after         *Brief, then auto-dismiss confirmation**        completion**          — never require user dismissal for non-critical success* ——————— ——————— —————————-

### Spatial Springs — Motion Physics

Ansai uses Spatial Spring animations exclusively for transitions. Linear
animations feel mechanical and robotic. Ease-in-out feels arbitrary.
Springs mirror the physics of the real world — objects accelerate and
decelerate according to mass and tension, not a predetermined curve.

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Use spring physics for all       | Never use linear transitions for  |
| transitions: CSS spring()        | element movement. Never use       |
| function, Framer Motion spring   | ease-in alone (elements that      |
| config, or React Native Animated | accelerate and never decelerate   |
| with spring. Recommended config: | feel violent). Never use CSS      |
| stiffness: 300, damping: 24,     | transition: all — always        |
| mass: 1.                         | specify the exact property.       |
+———————————-+———————————–+

> *CODE REFERENCE — CSS Spring Approximation: transition: transform 280ms cubic-bezier(0.34, 1.56, 0.64, 1); — This cubic-bezier approximates a spring with slight overshoot, which feels alive. The overshoot (value \> 1 in the Y axis) is intentional and critical.*

## Haptic Margins

As users scroll into empty zones or hit boundaries (top of list, bottom
of page, edge of carousel), implement tactile resistance: a subtle
haptic pulse that gives digital whitespace a physical presence. This is
not a gimmick — it is a spatial communication layer for users who are
navigating without looking at the screen.

> ——————— ———————————– —————————- **PROPERTY**          **VALUE / TOKEN**                   **USAGE / NOTE** **Boundary            **UIImpactFeedbackGenerator         *Top/bottom of scroll, resistance**          (light)**                           pull-to-refresh* **Destructive         **UINotificationFeedbackGenerator   *Delete confirm, action**              (warning)**                         irreversible toggle* **Success             **UINotificationFeedbackGenerator   *Payment complete, form confirmation**        (success)**                         submission* **Selection change**  **UISelectionFeedbackGenerator**    *Picker wheel, segmented control tap* **Error state**       **UINotificationFeedbackGenerator   *Form validation failure, (error)**                           auth failure* ——————— ———————————– —————————-

## Motion Principles

Motion must always serve a purpose. The three legitimate purposes
are: 1) Causality — showing the relationship between input and output.
2) Spatial orientation — telling the user where a new element came
from or where it went. 3) Status — communicating that the system is
working.

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Elements entering the screen     | Never animate elements in from    |
| should animate from their        | nowhere — floating in from      |
| logical origin: a bottom sheet   | off-screen in a direction         |
| rises from the bottom, a         | unrelated to any spatial logic is |
| settings panel slides in from    | disorienting. Never loop          |
| the right, a detail view expands | animations without a specific     |
| from the tapped element.         | status-communication purpose.     |
+———————————-+———————————–+

---

## Section VII — Platform Standards: Web vs. App

Ansai ships on two distinct surface types, each with its own conventions
and user expectations. A design that is correct for the web may be wrong
for the app, and vice versa. The following specifications are not
interchangeable.

### Ansai Web — The Glossy Brochure

Web surfaces are the first contact many users have with Ansai. They must
communicate premium quality, brand confidence, and product clarity
within 3 seconds of page load. Every web screen is both a marketing
surface and a functional interface.

> ——————— ——————— —————————- **PROPERTY**          **VALUE / TOKEN**     **USAGE / NOTE** **Max Content Width** **1280px centered**   *Content should never span the full width of a large monitor* **Screen Margin**     **24px mobile / 48px  *Generous margins signal tablet / 64px+        premium quality* desktop** **Paragraph Width**   **60–75ch            *Optimal reading line (characters)**        length. Never exceed 80ch.* **Primary             **Sticky top bar,     *Disappears on scroll-down, Navigation**          max-height 64px**     reappears on scroll-up* **Hero Image**        **Full-bleed, above   *No stock photo aesthetics fold, host-supplied   — images must feel real* photography** **CTA Placement**     **Above fold AND      *Two anchors — never after the primary     assume the user will scroll* value proposition** **Font Loading**      **font-display: swap  *Never block render on font with FOUT             load* mitigation** ——————— ——————— —————————- *WEB DESIGN PRINCIPLE: Lead with photography. Rich, host-supplied-style imagery anchors each listing or feature and gives the brand a human face. Stock photography is immediately recognizable and erodes trust. Commission or curate real-world images. If no real image is available, use a high-quality procedural illustration — not a generic icon.*

### Ansai App — The Native OS

The app must feel indistinguishable from a first-party OS application.
Users have been trained by years of using Apple and Google's own apps.
Any deviation from native conventions requires conscious, justified
intent — not accident.

> ——————— ———————— —————————- **PROPERTY**          **VALUE / TOKEN**        **USAGE / NOTE** **Navigation          **Bottom Navigation      *Home, Saved, Activity, Pattern**             Bar**                    Profile — 4 tabs maximum* **Tab Bar Height**    **49pt (iOS) / 56dp      *Plus safe area inset — (Android)**              never cover the home indicator* **Hit Target Size**   **44pt × 44pt minimum**  *All tappable elements, including icons without visible backgrounds* **Screen Edge         **16pt (iOS) / 16dp      *Standard side margin for Margin**              (Android)**              all content* **Back Navigation**   **System-native          *Never override the gesture + header back    swipe-back gesture* button** **Modal               **Bottom sheet for       *Full-screen modal for Presentation**        contextual actions**     complete new tasks* **Keyboard Behavior** **KeyboardAvoidingView / *Content must shift up, adjustResize**           never be obscured by keyboard* **Safe Areas**        **Honor all system safe  *Never place interactive areas**                  elements behind notches or home indicators* ——————— ———————— —————————-

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Use Progressive Disclosure for   | Never front-load all options onto |
| complex features. The first      | a single screen.                  |
| screen shows the primary action. | "Feature-stuffed" screens are   |
| Secondary controls live in       | the fastest way to make a premium |
| overflow menus, expandable       | product feel cheap. If a user     |
| sections, or subsequent steps    | needs to see it immediately, it   |
| — revealed on demand.          | belongs on the primary surface.   |
|                                  | If not, hide it.                  |
+———————————-+———————————–+

---

## Section VIII — Ethical Guardrails & Anti-Pattern Ban

Ansai builds trust by respecting user autonomy. Dark patterns are not
clever design — they are a betrayal of the Trusted Host relationship.
Every banned pattern below has a business case, which is why each one
must be explicitly prohibited. The short-term conversion lift from dark
patterns is real. The long-term trust erosion is real and larger.

## Banned Dark Patterns

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Cancellation flow: Match the     | ROACH MOTEL: Making it easy to    |
| signup flow exactly in terms of  | subscribe and deliberately        |
| steps and friction. Cancellation | difficult to cancel. Hiding the   |
| must be completable in the same  | cancel button behind support      |
| number of taps as signup, from   | tickets, waiting periods, or      |
| the same location in Settings.   | confusing navigation.             |
+———————————-+———————————–+

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Opt-out copy: "I don't want    | CONFIRMSHAMING: Guilt-language in |
| updates" or "No thanks".      | dismiss buttons: "No thanks,     |
| Neutral, factual language that   | I'd rather stay slow", "No, I  |
| respects the user's decision    | don't want to save money", "I  |
| without emotional manipulation.  | prefer to be uninformed". This   |
|                                  | is manipulation, not design.      |
+———————————-+———————————–+

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Reveal all costs before the user | HIDDEN FEES: Any cost —         |
| reaches the checkout screen.     | subscription renewal price,       |
| Show the total including taxes,  | service fee, processing charge    |
| fees, and recurring charges on   | — that appears for the first    |
| the product page.                | time at checkout. This is a       |
|                                  | design failure and a trust        |
|                                  | killer.                           |
+———————————-+———————————–+

+———————————-+———————————–+
| **✓ DO**                         | **✗ DON'T**                      |
|                                  |                                   |
| Pre-select the option that is    | TRICK QUESTIONS: Pre-selected     |
| best for the user (not best for  | checkboxes that sign the user up  |
| the business). If there is no    | for marketing, auto-renewal, or   |
| objectively better default,      | data sharing. The intent is       |
| leave all options unselected.    | deliberate confusion — this is  |
|                                  | not tolerated.                    |
+———————————-+———————————–+

## The Three-Tap Rule

> *MANDATORY: If a user cannot complete their primary objective within three taps from the relevant starting screen, the feature is a design failure. Count the taps. If it's four or more, simplify. This rule has no exceptions. It applies to: placing an order, messaging a host, saving a listing, editing profile information, and contacting support.*

The Three-Tap Rule is a forcing function, not a constraint on
complexity. Complex features can still be accessible in three taps if
the information architecture is well-designed. The rule eliminates the
lazy default of burying features deep in menus.

## Transparent Pricing Standard

> ——————— ——————— —————————- **PROPERTY**          **VALUE / TOKEN**     **USAGE / NOTE** **Price Display**     **Full price          *Show on product card, not including all fees**  just at checkout* **Subscription        **Clearly stated on   *"Renews at \$X/month. Renewal**             upgrade screen**      Cancel anytime in Settings."* **Trial Periods**     **End date +          *"Free until \[date\]. Then post-trial price      \$X/month, no commitment."* clearly stated** **Promotional         **Show original +     *Never show only the Pricing**             promotional price**   promotional price without context* **Currency**          **Use the user's     *Provide an option to switch local currency by     — never force a single default**             currency* ——————— ——————— —————————-

---

## Section IX — Master LLM Prompt Templates

These are battle-tested prompt structures engineered to produce
Ansai-quality output from any capable LLM. Copy, fill in the bracketed
variables, and paste. Each template builds on the specifications defined
in the preceding sections.

### Template A: New Screen Design

+———————————————————————–+
| **You are a senior product designer at Ansai. Design the \[SCREEN     |
| NAME\] screen for the \[iOS/Android/Web\] platform.**                 |
|                                                                       |
| **CONSTRAINTS — apply every rule literally:**                       |
|                                                                       |
| • Background: #0D1117 (Ansai Obsidian). No pure black.                |
|                                                                       |
| • Primary CTA: Linear gradient #D03660 → #D73B53. Used ONLY for the   |
| single primary action.                                                |
|                                                                       |
| • Typography: Ansai Flex variable font. Headlines at wdth 85%, Body 1 |
| minimum 17pt.                                                         |
|                                                                       |
| • Spacing: All values are multiples of 8px. Screen margin: 16pt.      |
|                                                                       |
| • Three-Tap Rule: The primary action \[STATE THE ACTION\] must be     |
| reachable in 3 taps.                                                  |
|                                                                       |
| • Visual Tail: Ensure a partial element is visible at the fold.       |
|                                                                       |
| • Accessibility: All text must meet APCA Lc 75+ for body, 60+ for     |
| headings.                                                             |
|                                                                       |
| DELIVERABLE: \[Figma annotations / HTML+CSS / React component /       |
| Detailed spec doc\]                                                   |
+———————————————————————–+

### Template B: Component Design (Atom Level)

+———————————————————————–+
| **Design the Ansai \[COMPONENT NAME\] component. Output as a React    |
| component using only Tailwind utility classes.**                      |
|                                                                       |
| STATES TO INCLUDE: Default · Hover · Active/Pressed · Disabled ·      |
| Error/Destructive (if applicable) · Loading (if applicable)           |
|                                                                       |
| **HARD CONSTRAINTS:**                                                 |
|                                                                       |
| • Hit target: minimum 44×44pt for all interactive elements.           |
|                                                                       |
| • Motion: Use spring easing (cubic-bezier(0.34, 1.56, 0.64, 1)) for   |
| state transitions.                                                    |
|                                                                       |
| • Feedback: State change must be visible within 50ms of interaction.  |
|                                                                       |
| • Colors: Use only tokens defined in the Ansai color system. No       |
| ad-hoc hex values.                                                    |
|                                                                       |
| • Typography: Label style (12–14px, Medium weight) for button text.  |
| Body 1 for inputs.                                                    |
+———————————————————————–+

### Template C: Copy & Microcopy

+———————————————————————–+
| **Write Ansai microcopy for the following UI elements. Apply the      |
| Trusted Host voice: confident, warm, direct, never condescending.**   |
|                                                                       |
| ELEMENTS NEEDED: \[List: e.g., Empty state for Saved tab / Error for  |
| failed payment / Success for booking confirmed / CTA for premium      |
| upsell\]                                                              |
|                                                                       |
| **RULES:**                                                            |
|                                                                       |
| • Button labels: Verb + noun. Max 3 words.                            |
|                                                                       |
| • Error messages: Say what happened + what to do next. Max 2          |
| sentences.                                                            |
|                                                                       |
| • Empty states: Heading + single explanation sentence + CTA.          |
|                                                                       |
| • No confirmshaming. No guilt language. No passive voice.             |
|                                                                       |
| • All prices disclosed upfront. No "starting from" without the      |
| actual range.                                                         |
+———————————————————————–+

---

## Section X — Design Review Checklist

This checklist is the final gate before any design moves from approved
to shipped. It is used by human designers reviewing LLM output, and can
also be pasted directly into an LLM prompt as a self-evaluation
instruction.

> *LLM SELF-EVALUATION INSTRUCTION: "Before presenting your design, evaluate it against every item in the following checklist. For each item, state whether it passes or fails and explain why. If any item fails, revise the design before presenting."*

## Visual Foundation

☐ Background uses Ansai Obsidian (#0D1117), not pure black (#000000).

☐ All color values reference semantic tokens, not hardcoded hex values.

☐ Primary CTA uses the Liquid gradient (#D03660 → #D73B53) and appears
exactly once per screen.

☐ Secondary actions use text or ghost button styles — never gradient.

☐ All text combinations pass APCA Lc 75+ (body) or 60+ (headlines).

☐ No color has been introduced that does not exist in the Ansai palette.

# Typography

☐ Headlines use Condensed Impact rule (wdth 85%).

☐ Body copy is minimum 17pt (iOS) / 18sp (Android).

☐ No more than three distinct type sizes appear in any one section.

☐ Emphasis uses weight or color — not italics, not underline, not size
increase.

☐ Body text is left-aligned. No full-justification on digital surfaces.

## Spatial & Layout

☐ All spacing values are multiples of 8px (4px exceptions documented and
justified).

☐ Screen margins are 16pt (mobile), 24pt (tablet), 32pt+ (desktop).

☐ The Visual Tail is present: a partial element is visible at the fold.

☐ No element sits outside the 8pt soft-grid without explicit
justification.

☐ All interactive elements have a minimum 44×44pt hit target.

# Interaction & Motion

☐ Every interactive element has documented default, hover, active, and
disabled states.

☐ All transitions use spring easing — no linear, no ease-in-out.

☐ Transition durations: micro (50–100ms), standard (150–280ms), page
(280–320ms).

☐ Haptic events are specified for boundary reaches and destructive
actions.

☐ No looping animations exist without a status-communication purpose.

## Microcopy & Ethics

☐ All button labels follow Verb + Noun format.

☐ Error messages state what happened and what the user can do next.

☐ Empty states include heading + explanation + CTA.

☐ No confirmshaming language exists anywhere in the design.

☐ The Three-Tap Rule is satisfied for the primary user objective.

☐ All costs are disclosed before the checkout screen.

☐ Cancellation is as accessible as signup.

## The Anti-AI-Slop Final Test

> *Ask this question of every design before it ships: Could this screen have come from a generic Dribbble template or a default LLM output? If the honest answer is "yes" or "maybe", it is not ready. Ansai designs must feel authored — like a specific human designer made a specific set of decisions for a specific reason. If you cannot name the decisions and the reasons, the design is not done.*

*Ansai Brand & Design System Toolkit · Version 1.0 · Confidential*
