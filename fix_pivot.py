import os
import glob
import re

def process_text(text):
    text = text.replace("| **\"agentic infrastructure\"** | agentic infrastructure, data structure company |", "| **\"agentic infrastructure\"** | digital infrastructure, data structure company |")
    return text

for path in ['Pivot.md', 'Ansai pivot.md']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = process_text(content)
    
    if content != new_content:
        print(f"Updated {path}")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
