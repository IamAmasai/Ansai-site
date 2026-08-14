import re
import glob

def replace_in_file(path, old, new):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed in {path}")

replace_in_file("ansai-redesign-prompt.md", "agentic agentic infrastructure", "agentic infrastructure")

replace_in_file("index.html", "a agentic infrastructure", "an agentic infrastructure")

replace_in_file("Pivot.md", "| **\"agentic infrastructure\"** | digital infrastructure, data structure company |", "| **\"agentic infrastructure\"** | digital infrastructure, operational infrastructure, data structure company |")
replace_in_file("Ansai pivot.md", "| **\"agentic infrastructure\"** | digital infrastructure, data structure company |", "| **\"agentic infrastructure\"** | digital infrastructure, operational infrastructure, data structure company |")

replace_in_file("Pivot.md", "Find-and-replace: every instance of `agentic infrastructure` must become `agentic infrastructure`", "Find-and-replace: every instance of `digital infrastructure` must become `agentic infrastructure`")
replace_in_file("Ansai pivot.md", "Find-and-replace: every instance of `agentic infrastructure` must become `agentic infrastructure`", "Find-and-replace: every instance of `digital infrastructure` must become `agentic infrastructure`")

replace_in_file("Pivot.md", "- [ ] Zero instances of \"agentic infrastructure\" in shipped copy.", "- [ ] Zero instances of \"digital infrastructure\" in shipped copy.")
replace_in_file("Ansai pivot.md", "- [ ] Zero instances of \"agentic infrastructure\" in shipped copy.", "- [ ] Zero instances of \"digital infrastructure\" in shipped copy.")

replace_in_file("frameworks/group-identity.html", "where it reads \"agentic infrastructure\" and \"institutions,\"", "where it reads \"operational infrastructure\" and \"institutions,\"")

