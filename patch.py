import re

css_file = 'styles.css'
with open(css_file, 'r') as f:
    content = f.read()

new_root = """:root {
  /* Color - Startup Modern Theme */
  --field-white: #FFFFFF;
  --field-gray: #F9FAFB;
  --field-dawn: #F3F4F6;
  --ink: #0F172A;
  --ink-soft: #475569;
  --signal-orange: #F97316; /* Vibrant startup orange */
  --surface: #FFFFFF;

  --bg-primary: var(--field-white);
  --bg-secondary: var(--field-gray);
  --bg-tertiary: var(--field-dawn);
  
  --text-primary: var(--ink);
  --text-secondary: var(--ink-soft);
  --text-tertiary: var(--ink-soft);
  --text-dim: #9CA3AF;
  
  --border: rgba(15, 23, 42, 0.1);
  --border-strong: rgba(15, 23, 42, 0.2);

  /* Sole accent */
  --accent: var(--signal-orange);
  --accent-soft: rgba(249, 115, 22, 0.15);
  --accent-glow: rgba(249, 115, 22, 0.35);

  /* Shape */
  --radius-btn: 8px;
  --radius-card: 24px;

  /* Type */
  --font-sans: "DM Sans", "Inter Tight", sans-serif;
  --font-mono: "DM Mono", monospace;
}"""

content = re.sub(r':root\s*\{.*?\--font-mono:[^\}]+\}', new_root, content, flags=re.DOTALL)

with open(css_file, 'w') as f:
    f.write(content)
