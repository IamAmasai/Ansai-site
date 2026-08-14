import re

css_file = 'styles.css'
with open(css_file, 'r') as f:
    content = f.read()

# Replace hardcoded var names with the new ones
content = content.replace('var(--signal-clay)', 'var(--accent)')
content = content.replace('var(--field-blush)', 'var(--bg-primary)')
content = content.replace('var(--field-sand)', 'var(--bg-secondary)')
content = content.replace('var(--field-dawn)', 'var(--bg-tertiary)')

# Also replace that specific rgba for the header
content = content.replace('rgba(246, 233, 228, 0.88)', 'rgba(255, 255, 255, 0.88)')

with open(css_file, 'w') as f:
    f.write(content)
