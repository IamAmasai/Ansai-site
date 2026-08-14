import os
import glob
import re

def process_text(text):
    text = text.replace("We build the infrastructure that lets them use it.", "We build the agentic infrastructure that lets them use it.")
    text = text.replace("Ansai builds the infrastructure that lets African organizations", "Ansai builds the agentic infrastructure that lets African organizations")
    text = text.replace("Ansai builds agentic infrastructure for African organizations", "Ansai builds agent-native infrastructure for African organizations")
    text = text.replace("Agentic infrastructure", "Agentic Infrastructure")
    
    return text

for path in glob.glob('**/*.html', recursive=True):
    if 'node_modules' in path or '.git' in path: continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = process_text(content)
    
    if content != new_content:
        print(f"Updated {path}")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
