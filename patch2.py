import re

css_file = 'styles.css'
with open(css_file, 'r') as f:
    content = f.read()

# .display .ghost
content = content.replace('color: rgba(255, 255, 255, 0.34);', 'color: var(--text-dim);')

# .layer-diagram
content = content.replace('fill: rgba(255, 255, 255, 0.13);', 'fill: rgba(15, 23, 42, 0.05);')
content = content.replace('stroke: rgba(255, 255, 255, 0.3);', 'stroke: rgba(15, 23, 42, 0.15);')
content = content.replace('fill: #ffffff;', 'fill: var(--ink);')
content = content.replace('stroke: #ffffff;', 'stroke: var(--ink);')
content = content.replace('fill: rgba(255, 255, 255, 0.16);', 'fill: rgba(15, 23, 42, 0.08);')
content = content.replace('stroke: rgba(255, 255, 255, 0.35);', 'stroke: rgba(15, 23, 42, 0.2);')
content = content.replace('stroke: rgba(255, 255, 255, 0.4);', 'stroke: rgba(15, 23, 42, 0.25);')
content = content.replace('stroke: rgba(255, 255, 255, 0.7);', 'stroke: rgba(15, 23, 42, 0.5);')
content = content.replace('fill: rgba(255, 255, 255, 0.72);', 'fill: rgba(15, 23, 42, 0.7);')
content = content.replace('fill: rgba(255, 255, 255, 0.5);', 'fill: rgba(15, 23, 42, 0.5);')
content = content.replace('color: rgba(255, 255, 255, 0.66);', 'color: var(--text-secondary);')
content = content.replace('color: rgba(255, 255, 255, 0.6);', 'color: var(--text-secondary);')
content = content.replace('color: rgba(255, 255, 255, 0.82);', 'color: var(--text-primary);')

# .bento-featured specific
content = content.replace('color: #ffffff;', 'color: var(--ink);')
content = content.replace('.button-primary {\n  background: var(--accent);\n  color: var(--ink);', '.button-primary {\n  background: var(--accent);\n  color: #ffffff;')

with open(css_file, 'w') as f:
    f.write(content)
