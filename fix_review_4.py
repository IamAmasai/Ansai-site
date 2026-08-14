import re

def replace_in_file(path, old, new):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed in {path}")
    else:
        print(f"Not found in {path}: {old}")

replace_in_file("Pivot.md", '| "agentic infrastructure" | "agentic infrastructure" | Every instance, hero to FAQ |', '| "operational infrastructure" | "agentic infrastructure" | Every instance, hero to FAQ |')
replace_in_file("Ansai pivot.md", '| "agentic infrastructure" | "agentic infrastructure" | Every instance, hero to FAQ |', '| "operational infrastructure" | "agentic infrastructure" | Every instance, hero to FAQ |')
