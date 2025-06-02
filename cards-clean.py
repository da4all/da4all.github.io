import os
import re

cards_dir = '_cards-copy'

def clean_multiline_keywords(front_matter):
    # Replace all non-standard quotes in the entire front matter
    front_matter = front_matter.replace('“', '"').replace('”', '"').replace('‘', '"').replace('’', '"')
    # Find the keywords block
    pattern = re.compile(
        r'(^keywords:\s*\n((?:[ \t]*-[^\n]*\n)+))',
        re.MULTILINE
    )
    def repl(match):
        block = match.group(2)
        keywords = [line.strip()[2:].strip() for line in block.splitlines() if line.strip().startswith('-')]
        # Convert to title case and wrap in double quotes if not already
        cleaned_keywords = []
        for k in keywords:
            #k = k.replace('“', '"').replace('”', '"')
            #k = k.replace('‘', "'").replace('’', "'")
            k = k.strip().title()
            if not (k.startswith('"') and k.endswith('"')):
                k = f'"{k.strip("\"")}"'
            cleaned_keywords.append(k)
        cleaned_keywords = sorted(set(cleaned_keywords))
        # Rebuild the block
        new_block = 'keywords:\n' + ''.join([f'  - {k}\n' for k in cleaned_keywords])
        return new_block
    return pattern.sub(repl, front_matter)

for filename in os.listdir(cards_dir):
    if filename.endswith('.md'):
        path = os.path.join(cards_dir, filename)
        with open(path, 'r') as f:
            content = f.read()
        # Only operate on the front matter
        match = re.match(r'(---\n.*?\n---)', content, re.DOTALL)
        if not match:
            continue  # No front matter, skip
        front_matter = match.group(1)
        new_front_matter = clean_multiline_keywords(front_matter)
        # Only write if changed
        if new_front_matter != front_matter:
            new_content = new_front_matter + content[len(front_matter):]
            with open(path, 'w') as f:
                f.write(new_content)
