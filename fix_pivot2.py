import re

def replace_in_file(path, old, new):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed in {path}")
    elif re.search(old, content):
        content = re.sub(old, new, content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed (regex) in {path}")
    else:
        print(f"Not found in {path}: {old}")

replace_in_file("Pivot.md", r'Find-and-replace: every instance of `operational infrastructure` must become `agentic infrastructure`', 'Find-and-replace: every instance of `operational infrastructure` must become `agentic infrastructure`')
replace_in_file("Ansai pivot.md", r'Find-and-replace: every instance of `operational infrastructure` must become `agentic infrastructure`', 'Find-and-replace: every instance of `operational infrastructure` must become `agentic infrastructure`')
