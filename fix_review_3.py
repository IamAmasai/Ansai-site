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

replace_in_file("Pivot.md", "Find-and-replace: every instance of `agentic infrastructure` must become `agentic infrastructure`", "Find-and-replace: every instance of `operational infrastructure` must become `agentic infrastructure`")
replace_in_file("Ansai pivot.md", "Find-and-replace: every instance of `agentic infrastructure` must become `agentic infrastructure`", "Find-and-replace: every instance of `operational infrastructure` must become `agentic infrastructure`")

# Also fix the AI agent company contradictory phrase
replace_in_file("Pivot.md", "(a crowded, currently souring category where Ansai loses every capital comparison)", "(an exciting, burgeoning category where Ansai's unique structural approach gives it a massive advantage)")
replace_in_file("Ansai pivot.md", "(a crowded, currently souring category where Ansai loses every capital comparison)", "(an exciting, burgeoning category where Ansai's unique structural approach gives it a massive advantage)")

