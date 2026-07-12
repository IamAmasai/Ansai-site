I have loaded tasteskill v2 (experimental) as my only source of design rules.

Brief:
- Site: Ansai Technologies marketing site (the live repo, vanilla HTML/CSS/JS)
- Mode: overhaul on the visual layer, preserve on copy and IA. Do not touch URL structure, nav labels, or the locked terms "digital infrastructure" and "organizations"
- Product: Ansai, the structural digital infrastructure layer for African organizations. First live product is EduManage, a multi-tenant school management platform
- Audience: decision-makers at Kenyan and African organizations (schools, institutions, SMEs) evaluating trust-first B2B infrastructure, not a consumer or agency audience
- Vibe words: confident, structural, restrained, trust-first B2B, not agency-playful, not consumer-flashy
- References: none external, the brand mark itself is the primary reference, see logo section below
- Avoid: orange or any color outside the locked palette below as a base or accent, three-equal-card feature rows, rainbow or multi-hue icon sets, decorative status dots, autoplaying carousels, em-dashes anywhere in copy, centered hero, section-numbering eyebrows

Locked decisions, do not re-litigate these, implement them:

Design tokens
- --navy: #111C27 (page background)
- --blue: #1C5CF5 (sole accent, used identically everywhere: CTAs, icons, featured tiles, links)
- --teal: #2DE8E8 (reserved for the logo mark only, must not appear anywhere else on the page)
- --white: #ffffff (primary text on dark)
- --muted: #8B98A8 (secondary text on dark)
- --muted-dim: #5A6C82 / #7A8595 (tertiary text, labels)
- Corner radius: 8px on buttons, 20px on cards, one scale per element type, no exceptions
- Nav: single line, max 80px height, default 64px

Hero
- Pattern: Asymmetric Split Hero. Headline and CTA left-aligned, not centered
- Right side: solid blue (--blue) panel that bleeds past its own column edge in a deliberate overlap, not a boxed-in image slot
- Headline max 2 lines desktop, subtext max 20 words and 4 lines, primary CTA visible without scroll
- No tagline, trust strip, or pricing teaser inside the hero itself, those live in sections below it

Feature grid
- Pattern: Bento Grid, exact cell count for the content, no empty filler tiles
- Every cell is its own rounded card (20px radius) with real gaps between tiles, never flush edges
- Cells differ in material, not just color: at most one cell uses the fully saturated --blue fill, the rest use a soft blue-tinted surface (rgba(28,92,245,0.09)) or the page's neutral surface
- No three-equal-card default, vary tile size (one larger tile, smaller tiles around it)

Icon row
- Use the GlassIcons component provided (GlassIcons.jsx, GlassIcons.css), already re-skinned to a single hue with tint-only depth variation, no per-item color prop, do not reintroduce multi-hue icons

Motion budget, homepage only
- One scroll-triggered fade/rise reveal on the bento grid cells, via IntersectionObserver, fires once, staggered by roughly 0.08s per cell
- Nothing else animates on load or on a loop
- Do not add CardSwap or Stepper to the homepage, both are reserved for future pages (case studies, onboarding) with actual sequential content to justify them

Step 1. Declare your design read in one sentence and the three dial values with one-line reasoning each. Given the brief above, expect variance around 7 to 8 for the asymmetric hero and bento, motion around 3 to 4 given the single-reveal budget, density around 3 to 4. Stop and wait for confirmation before writing code.

Step 2 (after confirmation). Implement the hero, bento feature grid, and icon row exactly as specified above. Reuse existing page sections and copy untouched except where the locked tokens require a color or radius change. Do not invent new sections, new copy, or new components beyond what's listed.

Step 3. Run in writing, every box marked pass or fail with a one-line justification:
- Em-dash audit: zero em-dashes anywhere in output, headlines, labels, body, alt text
- Color Consistency Lock: --blue is the only accent, used identically in every section, --teal appears nowhere outside the logo
- Shape Consistency Lock: 8px buttons and 20px cards applied everywhere, no exceptions
- Bento Cell Count: cell count matches content count exactly, no empty tiles
- Motion Motivated: the single reveal animation is justified in one sentence, no other motion shipped
- No Duplicate CTA Intent: one label per intent across nav, hero, and footer
- Button Contrast Check: every CTA text passes WCAG AA against its background
